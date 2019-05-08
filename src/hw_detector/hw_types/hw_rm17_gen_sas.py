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

from hw_detector.hw_types.hw_rm17 import HWRM17

class HWRM17GENSAS(HWRM17):
    def __init__(self):
        super(HWRM17GENSAS, self).__init__()
        self.matches = {'Board Product' : 'AR-D51BP10.*'}
        self.hwtype = 'RM17GENSAS'
