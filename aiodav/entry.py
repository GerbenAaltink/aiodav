import pathlib
from pathlib import PosixPath


class Entry(pathlib.PosixPath):
    @property
    def name(self):
        if not super().name:
            return "/"
        return super().name

    @property
    def parent(self):
        return Entry(super().parent)

    @property
    def parents(self):
        if self is self.parent:
            return self
        return self.parent

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
