from social_api.app import create_app
from social_api.settings import Settings
from social_api.web import compose_app

api = create_app(Settings())
app = compose_app(api)
