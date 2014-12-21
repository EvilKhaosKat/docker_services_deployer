import json


class Command():
    name = ""
    json = None

    def __init__(self, command_name, json_filename):
        self.name = command_name
        self.json = json.loads(open(json_filename).read())


command = Command("command_1", "test_json.json")
print(str(command.json))


