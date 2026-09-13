from pos_api.app import create_app
from pos_api.settings import Settings

app = create_app(Settings())
