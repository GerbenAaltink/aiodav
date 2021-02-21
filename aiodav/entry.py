import pathlib
from pathlib import PosixPath


class Entry(pathlib.PosixPath):

    _flavor = PosixPath

    @property
    def name(self):
        if not super().name:
            return "/"
        return super().name

    @property
    def as_url(self):
        return super().name

    def relative_path(self, root):
        return self.relative_to(root)

    def joinpath(self, glob="*"):
        return Entry(super().joinpath(glob))

    def glob(self, prefix=None):
        if prefix is None:
            prefix = "*"
        return [Entry(entry) for entry in super().glob(prefix)]