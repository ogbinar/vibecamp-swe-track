"""One ASGI entry point: Air pages over the existing FastAPI backend."""

import air

from catalog_api.app import create_app
from catalog_api.settings import Settings
from catalog_api.web import create_web_router

api = create_app(Settings())
app = air.Air(fastapi_app=api)
app.include_router(create_web_router(), include_in_schema=False)
