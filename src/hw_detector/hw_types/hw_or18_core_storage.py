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

class HWOR18CORESTORAGE(NokiaHWType):
    def __init__(self):
        super(HWOR18CORESTORAGE, self).__init__()
        self.matches = {'Board Product' : 'AO-SER2U-AS/AF2115.01',
                        'Product Name' : 'Controller'}
        self.hwtype = 'OR18CORESTORAGE'
        self.productfamily = 'OR18'
        self.disk_map = {'os' : '%s/pci-0000:3b:00.0-scsi-0:2:0:0' %self.by_path,
                         'osd': ['%s/pci-0000:18:00.0-nvme-1' %self.by_path,
                                 '%s/pci-0000:19:00.0-nvme-1' %self.by_path
                                ]
                        }
