import pathlib
from typing import Iterable

from aiohttp import web

from aiodav.user import User


def create_app(root: str = "/", users: Iterable[User] = None) -> web.Application:
    app = web.Application()
    app["root"] = pathlib.Path(root)
    app['users'] = users
    return app
