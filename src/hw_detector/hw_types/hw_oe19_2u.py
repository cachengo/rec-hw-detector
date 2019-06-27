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

class HWOE192U(NokiaHWType):
    def __init__(self):
        super(HWOE192U, self).__init__()
        self.matches = {'Board Product' : 'AE-SER2U-A/AF1804.*'}
        self.hwtype = 'OE192U'
        self.productfamily = 'OE19'
        self.disk_map = {'os' : '%s/pci-0000:00:11.5-ata-3' %self.by_path,
                         'osd': ['%s/pci-0000:00:17.0-ata-1' %self.by_path,
                                 '%s/pci-0000:00:17.0-ata-2' %self.by_path,
                                 '%s/pci-0000:00:17.0-ata-3' %self.by_path,
                                 '%s/pci-0000:00:17.0-ata-4' %self.by_path
                                ]
                        }

