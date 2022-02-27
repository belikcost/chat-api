from aiohttp import web
from routes import setup_routes
from messenger.components.middleware import middleware

app = web.Application(middlewares=[middleware])
setup_routes(app, "/v1")
web.run_app(app)
