import pathlib

from aiohttp import web


def create_app(root="/", users=None):
    app = web.Application()
    app["root"] = pathlib.Path(root)
    return app
