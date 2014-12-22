import json
from entities.machines.Machine import Machine


localhost_base_url_ip = "tcp://127.0.0.1:2375"
localhost_base_url_unix = 'unix://var/run/docker.sock'


def parse_machines_file(content):
    machines_file = json.loads(content) # TODO use load and read file directly?
    machines_json = machines_file.get("machines")

    # TODO what should we do if Machine object creation fails? For instance if base_url isn't available
    return map(lambda machine_json: Machine(machine_json.get("base_url"), machine_json.get("name")), machines_json)


def get_machines_from_settings(machines_filename="machines.json"):
    machines_file = open(machines_filename)
    return parse_machines_file(machines_file.read())


def get_available_machine(machines):
    return min(machines, key=lambda machine: len(machine.docker.containers()))