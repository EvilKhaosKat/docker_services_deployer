from docker import Client
from entities.machines.Machine import Machine

localhost_base_url_ip = "tcp://127.0.0.1:2375"
localhost_base_url_unix = 'unix://var/run/docker.sock'

client = Client(base_url=localhost_base_url_unix)
print(str(client.info()))

machine = Machine(localhost_base_url_unix)
print(str(machine))