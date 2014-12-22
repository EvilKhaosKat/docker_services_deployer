import unittest
from entities.machines import MachinesHelper
from entities.machines.Machine import Machine


class MachineTests(unittest.TestCase):
    def test_parse_machines_file(self):
        content = '{ \
                       "machines": [ \
                           { \
                               "name": "local_machine_1", \
                               "base_url": "unix://var/run/docker.sock" \
                           }, \
                           {\
                               "name": "remote_machine_1",\
                               "base_url": "tcp://127.0.0.1:8000" \
                           }\
                       ]\
                   }\
                  '

        machines = MachinesHelper.parse_machines_file(content)

        self.assertEquals([Machine("unix://var/run/docker.sock"), Machine("tcp://127.0.0.1:8000")], machines)