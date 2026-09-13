from ecommerce_api.app import create_app
from ecommerce_api.settings import Settings

app = create_app(Settings())
