from aiohttp.web import run_app

from aiodav.app import create_app

if __name__ == '__main__':
    run_app(create_app(()))