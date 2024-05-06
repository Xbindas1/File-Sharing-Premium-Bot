# Xbindas
# Don't Remove Credit 🥺
# Telegram Channel @Xbindas
# Backup Channel @Xbindas
# Developer @Xbindas_Owner





from aiohttp import web
from .route import routes


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app





# Xbindas 
# Don't Remove Credit 🥺
# Telegram Channel @Xbindas
# Backup Channel @Xbindas
# Developer @Xbindas_Owner
