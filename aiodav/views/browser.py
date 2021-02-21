import aiohttp_jinja2
from aiohttp.web import View
from aiohttp.web_response import json_response

from aiodav import User
from aiodav.utils import safe_url


class BrowserView(View):

    async def resolve_user(self) -> User:
        return User(username='admin', password='admin', root='/')

    async def get(self):

        user = await self.resolve_user()
        root = user.joinpath(self.request.match_info.get('tail'))


        files = []
        for file_ in root.joinpath(self.request.match_info.get('tail')).glob('*'):
            files.append(dict(
                name= file_.name,
                parent= file_.name,
                uri= safe_url('browser', file_),
                root=root
            ))

        location = root

        print(dict(
            a=self.request.raw_path,
            b=self.request.path,
            c=self.request.match_info,
            d=self.request.path_qs,
            e=self.request.host,
            location=location
        ))
        context = dict(
            tail=self.request.match_info.get('tail'),
            request=self.request,
            files=files,
            path=root

        )
        return aiohttp_jinja2.render_template(
            'browser.html',
            self.request,
            context
        )