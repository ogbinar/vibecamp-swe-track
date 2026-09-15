from booking_api.app import create_app
from booking_api.settings import Settings
from booking_api.web import compose_app

api = create_app(Settings())
app = compose_app(api)
