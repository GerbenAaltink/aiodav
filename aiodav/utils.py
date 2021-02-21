import pathlib


def safe_url(prefix: str, path: pathlib.Path) -> str:
    uri = path.name
    #parts = '/' + prefix + uri
    return uri