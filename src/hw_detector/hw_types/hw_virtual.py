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

from hw_detector.hw_type import HWType


class HWVirtual(HWType):
    def __init__(self):
        super(HWVirtual, self).__init__()
        self.matches = {'Board Product' : 'VIRTUAL'} # Not used
        self.hwtype = 'VIRTUAL'
        self.disk_map = {'os': '%s/pci-0000:00:0a.0-scsi-0:0:0:0' %self.by_path,
                         'osd' : ['%s/pci-0000:00:0a.0-scsi-0:0:0:1' %self.by_path,
                                  '%s/pci-0000:00:0a.0-scsi-0:0:0:2' %self.by_path,
                                  '%s/pci-0000:00:0a.0-scsi-0:0:0:3' %self.by_path
                                 ]
                        }

