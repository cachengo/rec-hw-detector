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

import re

class HWType(object):
    def __init__(self):
        self.by_path = '/dev/disk/by-path'
        self.matches = {}
        self.hwtype = 'Generic'
        self.vendor_name = 'Generic'
        self.productfamily = 'Unknown'
        self.disk_map = {'os' : '', 'osd': []}

    def get_disk_by_name(self, name):
        return self.disk_map.get(name, None)

    @property
    def vendor(self):
        return self.vendor_name

    @property
    def product_family(self):
        return self.productfamily

    @property
    def hw_type(self):
        return self.hwtype

    def match(self, info):
        criteria_matches = 0
        for key, value in self.matches.iteritems():
            #Exact match has more value than regexp
            if info.get(key, '') == value:
                criteria_matches += 10
            elif re.match(value, info.get(key, '')):
                criteria_matches += 1
            else:
                criteria_matches = 0
                break

        return criteria_matches
