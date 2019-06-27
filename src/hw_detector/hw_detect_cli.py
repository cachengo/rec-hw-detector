#!/usr/bin/python

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

import sys
import argparse
import pprint
import hw_detector.hw_detect_lib as hw
from hw_detector.hw_exception import HWException

def dump_data(data):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)

def local_dump(args):
    data = hw.get_local_hw_data()
    dump_data(data)

def remote_dump(args):
    ip = args.ip
    user = args.user
    passw = args.passwd
    priv = args.priv
    try:
        data = hw.get_hw_data(ip, user, passw, priv, False)
    except HWException as e:
        data = "Detect failed: {}".format(str(e))
    dump_data(data)

def main():
    parser = argparse.ArgumentParser(description='HW detector cli')
    subparsers = parser.add_subparsers()
    local_group = subparsers.add_parser('local')
    remote_group = subparsers.add_parser('remote')

    remote_group.add_argument('--ip', type=str, required=True, help='IP')
    remote_group.add_argument('--user', type=str, required=True, help='User')
    remote_group.add_argument('--passwd', type=str, required=True, help='Password')
    remote_group.add_argument('--priv', type=str, required=False, default='ADMINISTRATOR', help='Privilege level (default: ADMINISTRATOR)')
    local_group.set_defaults(func=local_dump)
    remote_group.set_defaults(func=remote_dump)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)
if __name__ == '__main__':
    main()
