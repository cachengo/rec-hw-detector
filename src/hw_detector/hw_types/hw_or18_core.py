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

class HWOR18CORE(NokiaHWType):
    def __init__(self):
        super(HWOR18CORE, self).__init__()
        self.matches = {'Board Product' : 'AO-SER2U-AS/AF2115.01',
                        'Product Name' : 'Compute',   # Misleading but Controller is storage controller
                        'Product Part Number' : 'HYV-S-NCAC0211010'}
        self.hwtype = 'OR18CORE'
        self.productfamily = 'OR18'
        self.disk_map = {'os' : '%s/pci-0000:00:11.5-ata-5' %self.by_path,
                         'osd': ['%s/pci-0000:00:11.5-ata-6' %self.by_path
                                ]
                        }
