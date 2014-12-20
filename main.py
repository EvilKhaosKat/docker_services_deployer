from docker import Client
from entities.machines.Machine import Machine
from entities.machines.MachinesHelper import localhost_base_url_unix


client = Client(base_url=localhost_base_url_unix)
print(str(client.info()))

machine = Machine(localhost_base_url_unix)
print(str(machine))