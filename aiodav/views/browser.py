import pathlib

import aiohttp_jinja2
from aiohttp.web import View
from aiohttp.web_fileresponse import FileResponse
from aiohttp.web_response import json_response

from aiodav import User
from aiodav.utils import safe_url


class BrowserView(View):
    async def resolve_user(self) -> User:
        return User(username="admin", password="admin", root="/home")

    async def get(self):

        user = await self.resolve_user()

        root = pathlib.Path(self.request.match_info.get("tail"))
        print(root)

        if root.is_file():
            return FileResponse(root)

        files = []
        for file_ in root.joinpath(self.request.match_info.get("tail")).glob("*"):
            files.append(
                dict(
                    name=file_.name,
                    parent=file_.name,
                    uri=safe_url("browser", file_),
                    root=root,
                )
            )

        context = dict(
            tail=self.request.match_info.get("tail"),
            request=self.request,
            files=files,
            path=root,
        )
        return aiohttp_jinja2.render_template("browser.html", self.request, context)
