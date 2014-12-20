from entities.machines.Machine import Machine


localhost_base_url_ip = "tcp://127.0.0.1:2375"
localhost_base_url_unix = 'unix://var/run/docker.sock'

def get_machines_urls_from_settings():
    return ["localhost"]

def get_all_machines():
    machines_urls = get_machines_urls_from_settings()
    machines = []

    for machine_url in machines_urls:
        machine = Machine(machine_url)

    return machines