from aiodav.app import create_app


async def app(aiohttp_client):
    aiohttp_app = create_app()
    client = aiohttp_client(aiohttp_app)
    return client
