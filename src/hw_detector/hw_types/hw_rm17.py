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

from hw_detector.nokia_hw_type import NokiaHWType

class HWRM17(NokiaHWType):
    def __init__(self):
        super(HWRM17, self).__init__()
        self.matches = {'Board Product' : 'S2BP-MB (dual 10G LoM)'}
        self.hwtype = 'RM17'
        self.productfamily = 'HW17'
        self.disk_map = {'os' : '%s/pci-0000:81:00.0-sas-phy0-lun-0' %self.by_path,
                         'osd': ['%s/pci-0000:81:00.0-sas-phy1-lun-0' %self.by_path,
                                 '%s/pci-0000:81:00.0-sas-phy2-lun-0' %self.by_path,
                                 '%s/pci-0000:81:00.0-sas-phy3-lun-0' %self.by_path
                                ]
                        }
