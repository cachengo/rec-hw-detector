# Copyright 2019 Nokia

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hw_detector.hw_ipmi_lib as hw_ipmi_lib
import hw_detector.hw_types as hw_types

info = {}

def get_match(info):
    matches = {}

    for hw in hw_types.types:
        amount = hw.match(info)
        if amount != 0:
            matches[hw.hw_type] = amount

    if matches:
        return sorted(matches, key=matches.get, reverse=True)[0]

    return 'Unknown'

def get_info(ipmi_addr=None, ipmi_user=None, ipmi_pass=None, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    global info
    if is_virtual(detect_virtual):
        return {'Board Product' : 'VIRTUAL'}
    if info.get(ipmi_addr, False):
        return info[ipmi_addr]
    if ipmi_addr:
        info[ipmi_addr] = hw_ipmi_lib.get_ipmi_info(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level)
    else:
        return hw_ipmi_lib.get_local_ipmi_info()
    if ipmi_addr and not info.get(ipmi_addr):
        info[ipmi_addr] = {}

    return info[ipmi_addr]

def get_type(ipmi_addr=None, ipmi_user=None, ipmi_pass=None, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    info = get_info(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual)
    if not info:
        return 'Unknown'

    matches = get_match(info)
    return matches

def is_virtual(detect_virtual):
    if not detect_virtual:
        return False
    with open('/proc/cpuinfo') as f:
        for line in f.readlines():
            if line.startswith('flags') and 'hypervisor' in  line:
                return True
    return False

def _get_hw_with_hw_type(hw_type):
    for hw in hw_types.types:
        if hw.hw_type == hw_type:
            return hw

def get_product_family(hw_type):
    hw = _get_hw_with_hw_type(hw_type)
    if hw:
        return hw.product_family
    return None


def get_vendor(hw_type):
    hw = _get_hw_with_hw_type(hw_type)
    if hw:
        return hw.vendor
    return None

def hd_with_type(hw_type, hd_type):
    hw = _get_hw_with_hw_type(hw_type)
    if hw:
        return hw.get_disk_by_name(hd_type)
    #Default behaviour hardware that is not detected
    return None

def os_hd(hw_type):
    disk = hd_with_type(hw_type, 'os')
    return disk if disk else '/dev/sda'
