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

import os
import sys
import inspect
import hw_detector.hw_type as hwbase_type

def _import_classes(module_name, module_type):
    classes = []
    try:
        __import__(module_name)
    except ImportError as e:
        print("Failed import in {0} skipping {1}".format(module_name, e))
        return None
    module = sys.modules[module_name]
    for obj_name in dir(module):
        # Skip objects that are meant to be private.
        if obj_name.startswith('_'):
            continue
        elif obj_name == module_type.__name__:
            continue
        itm = getattr(module, obj_name)
        if inspect.isclass(itm) and issubclass(itm, module_type):
            classes.append(itm)
    return classes

def get_libs(directory, module_type):
    classes = []
    if directory not in sys.path:
            sys.path.append(directory)

    for fname in os.listdir(directory):
        root, ext = os.path.splitext(fname)
        if ext != '.py' or root == '__init__':
            continue
        module_name = "%s" % (root)
        for iclass in _import_classes(module_name, module_type):
            classes.append(iclass())
    return classes

types = get_libs('%s/hw_types' % os.path.dirname(hwbase_type.__file__), hwbase_type.HWType)
