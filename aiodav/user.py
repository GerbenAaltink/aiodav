import pathlib


class User:
    username = "admin"
    password = "admin"
    root = "/"

    def __init__(self, username, password, root=None):
        self.username = username
        self.password = password
        self.root = root or "/"

    @property
    def path(self)  -> pathlib.Path:
        return pathlib.Path(self.root)

    def joinpath(self, glue: str) -> pathlib.Path:
        return self.path.joinpath(glue)
