import json
import os
from functools import partial

import yaml
from aiohttp import web
from yaml import Loader

from messenger.domain.UserSettingsManager import UserSettingsManager
from routes import setup_routes
from messenger.components.middleware import middleware

working_directory = os.getcwd()
print(UserSettingsManager(partial(yaml.load, Loader=Loader), working_directory + '/messenger/user_settings.yaml').get_all())

app = web.Application(middlewares=[middleware])
setup_routes(app, "/v1")
web.run_app(app)
