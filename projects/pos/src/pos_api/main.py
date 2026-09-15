from pos_api.app import create_app
from pos_api.settings import Settings
from pos_api.web import compose_app

api = create_app(Settings())
app = compose_app(api)
