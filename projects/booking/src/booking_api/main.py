from booking_api.app import create_app
from booking_api.settings import Settings

app = create_app(Settings())
