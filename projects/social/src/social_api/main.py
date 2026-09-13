from social_api.app import create_app
from social_api.settings import Settings

app = create_app(Settings())
