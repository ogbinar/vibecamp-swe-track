from ecommerce_api.app import create_app
from ecommerce_api.settings import Settings
from ecommerce_api.web import compose_app

api = create_app(Settings())
app = compose_app(api)
