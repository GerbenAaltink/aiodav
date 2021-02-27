import pathlib
from time import strftime, gmtime


def safe_url(prefix: str, path: pathlib.Path) -> str:
    uri = path.name
    # parts = '/' + prefix + uri
    return uri


def unixdate2iso8601(d):
    tz = timezone / 3600  # can it be fractional?
    tz = "%+03d" % tz
    return strftime("%Y-%m-%dT%H:%M:%S", localtime(d)) + tz + ":00"


def unixdate2httpdate(d):
    return strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime(d))
