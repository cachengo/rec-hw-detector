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

import hw_detector.hw_utils as hw_utils

def get_local_hw_type():
    return hw_utils.get_type()

def get_hw_type(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    return hw_utils.get_type(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual)

def get_os_hd(hw_type):
    return hw_utils.os_hd(hw_type)

def get_hd_with_usage(hw_type, hd_type):
    return hw_utils.hd_with_type(hw_type, hd_type)

def get_local_os_hd():
    return get_os_hd(get_local_hw_type())

def get_local_osd_hd():
    return get_hd_with_usage(get_local_hw_type(), 'osd')

def get_remote_os_hd(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    return get_os_hd(get_hw_type(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual))

def get_vendor(hw_type):
    return hw_utils.get_vendor(hw_type)

def get_product_family(hw_type):
    return hw_utils.get_product_family(hw_type)

def _populate_data(hw_type, data_source, ipmi_addr=None, ipmi_user=None, ipmi_pass=None, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    data = {}
    data['hw_type'] = hw_type
    data['os_hd'] = get_os_hd(hw_type)
    data['osd_hd'] = get_hd_with_usage(hw_type, 'osd')
    data['vendor'] = get_vendor(hw_type)
    data['product_family'] = get_product_family(hw_type)
    data['info'] = hw_utils.get_info(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual)
    data['data_source'] = data_source
    if data_source == 'remote':
        data['ipmi_addr'] = ipmi_addr
        data['ipmi_user'] = ipmi_user
        data['ipmi_pass'] = ipmi_pass
        data['ipmi_priv_level'] = ipmi_priv_level
    return data

def get_local_hw_data():
    hw_type = get_local_hw_type()
    return _populate_data(hw_type, 'local')

def get_hw_data(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level='ADMINISTRATOR', detect_virtual=True):
    hw_type = get_hw_type(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual)
    return _populate_data(hw_type, 'remote', ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level, detect_virtual)
