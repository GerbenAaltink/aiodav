import pathlib


class User:
    username = "admin"
    password = "admin"
    root = "/"

    def __init__(self, username, password, root=None):
        self.username = username
        self.password = password
        self.root = root or "/"

    def path(self, glue):
        return pathlib.Path(self.root).joinpath(glue)
