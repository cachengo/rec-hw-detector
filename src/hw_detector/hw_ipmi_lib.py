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

import subprocess
import os

from hw_detector.hw_exception import HWException

def get_ipmi_info(ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level='ADMINISTRATOR'):
    command = "ipmitool -I lanplus -H %s  -U %s -P %s -L %s fru print 0" % (ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level)
    info = ipmi_info(command)

    command = "ipmitool -I lanplus -H %s  -U %s -P %s -L %s lan print" % (ipmi_addr, ipmi_user, ipmi_pass, ipmi_priv_level)
    info.update(ipmi_info(command))

    return info

def _load_ipmi_drivers():
    with open(os.devnull, 'w') as devnull:
        subprocess.call('modprobe ipmi_msghandler', stderr=devnull, shell=True)
        subprocess.call('modprobe ipmi_devintf', stderr=devnull, shell=True)
        subprocess.call('modprobe ipmi_si', stderr=devnull, shell=True)

def get_local_ipmi_info():
    _load_ipmi_drivers()
    info = ipmi_info("ipmitool fru print 0")
    info.update(ipmi_info("ipmitool lan print"))
    return info

def ipmi_info(command):
    out = None
    p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, _ = p.communicate()

    if p.returncode:
        raise HWException(out)

    info = {}
    for line in out.split('\n'):
        spl = line.find(':')
        if spl == -1:
            continue
        else:
            key = line[0:spl].strip()
            if key == '':
                continue
            info[line[0:spl].strip()] = line[spl+1:].strip()
    return info
