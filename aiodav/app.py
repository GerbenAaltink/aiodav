import pathlib
from typing import Iterable

import aiohttp_jinja2
import jinja2
from aiohttp import web

from aiodav.user import User
from aiodav.views.browser import BrowserView


def create_app(users: Iterable[User] = None) -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(
            pathlib.Path(__file__).parent.joinpath("templates")
        ),
    )
    app.router.add_view("/browser{tail:.+}", BrowserView)
    if not users:
        users = [User("admin", "admin", "/home/gerben")]
    app["users"] = users
    return app
