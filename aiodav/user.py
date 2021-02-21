import base64
import pathlib

from aiodav.entry import Entry


class User:
    username = "admin"
    password = "admin"
    root = "/"

    def __init__(self, username, password, root=None):
        self.username = username
        self.password = password
        self.root = root or "/"

    def __str__(self) -> str:
        return f"{self.username}:{self.password}"

    @property
    def base64(self) -> str:
        return base64.b64encode(str(self).encode()).decode()

    @property
    def path(self) -> pathlib.Path:
        return pathlib.Path(self.root)

    def joinpath(self, glue: str = None) -> Entry:
        return Entry(self.path.joinpath(glue))
