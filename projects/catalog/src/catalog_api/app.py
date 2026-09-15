"""FastAPI backend factory for the catalog's JSON and operational routes."""

from fastapi import FastAPI

from catalog_api.models import HealthResponse, ProductResponse
from catalog_api.service import sample_product
from catalog_api.settings import Settings


def create_app(settings: Settings) -> FastAPI:
    """Create an application whose configuration is explicit and testable."""
    app = FastAPI(title=settings.service_name)

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok", service=settings.service_name)

    @app.get("/products/sample", response_model=ProductResponse)
    def get_sample_product() -> ProductResponse:
        return sample_product()

    return app
