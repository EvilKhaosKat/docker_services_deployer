from docker import Client


class Machine:
    name = ""
    base_url = ""
    docker = None

    def __init__(self, base_url, name=""):
        """

        :param base_url:
        :param name:

        :type base_url: str
        :type name: str
        :return:
        """
        self.base_url = base_url
        self.docker = Client(base_url=base_url)
        self.name = name

    def __str__(self):
        return "Machine(name={name}, base_url={base_url})".format(name=self.name, base_url=self.base_url)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.base_url == other.base_url


