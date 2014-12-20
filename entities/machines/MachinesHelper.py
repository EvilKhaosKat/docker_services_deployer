from entities.machines.Machine import Machine


def get_machines_urls_from_settings():
    return ["localhost"]

def get_all_machines():
    machines_urls = get_machines_urls_from_settings()
    machines = []

    for machine_url in machines_urls:
        machine = Machine(machine_url)

    return machines