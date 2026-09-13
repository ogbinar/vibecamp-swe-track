"""FastAPI application factory and the starter's two HTTP endpoints."""

from decimal import Decimal

from fastapi import FastAPI

from catalog_api.models import HealthResponse, ProductResponse
from catalog_api.settings import Settings


def create_app(settings: Settings) -> FastAPI:
    """Create an application whose configuration is explicit and testable."""
    app = FastAPI(title=settings.service_name)

    @app.get("/health", response_model=HealthResponse)
    def health() -> HealthResponse:
        return HealthResponse(status="ok", service=settings.service_name)

    @app.get("/products/sample", response_model=ProductResponse)
    def sample_product() -> ProductResponse:
        return ProductResponse(sku="VC-001", name="Mechanical Keyboard", price=Decimal("19.99"))

    return app
