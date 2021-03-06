# Copyright 2020 DeChainy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import os

from dechainy.controller import Controller
import dechainy.exceptions as exceptions


class TestServer(unittest.TestCase):

    @unittest.skipIf(os.getuid(), reason='Root for BCC')
    def test_run(self):
        controller = Controller()
        with self.assertRaises(exceptions.PluginNotFoundException):
            controller.get_probe('plugin0', 'probe0')


if __name__ == '__main__':
    unittest.main()
