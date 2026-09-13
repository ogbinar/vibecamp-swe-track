"""ASGI entry point used by FastAPI and Uvicorn."""

from catalog_api.app import create_app
from catalog_api.settings import Settings

app = create_app(Settings())
