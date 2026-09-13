"""Public-boundary tests for the M0 catalog starter."""

from collections.abc import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from pydantic import ValidationError

from catalog_api.app import create_app
from catalog_api.settings import Settings


@pytest.fixture
def anyio_backend() -> str:
    """Keep this starter on Python's built-in asyncio backend."""
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    settings = Settings(service_name="Test Catalog", environment="test", _env_file=None)
    app: FastAPI = create_app(settings)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_health_reports_liveness(client: AsyncClient) -> None:
    response = await client.get("/health")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("application/json")
    assert response.json() == {"status": "ok", "service": "Test Catalog"}


@pytest.mark.anyio
async def test_sample_product_has_typed_public_shape(client: AsyncClient) -> None:
    response = await client.get("/products/sample")

    assert response.status_code == 200
    assert response.json() == {
        "sku": "VC-001",
        "name": "Mechanical Keyboard",
        "price": "19.99",
    }


def test_service_name_is_required(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CATALOG_SERVICE_NAME", raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_empty_service_name_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(service_name="", _env_file=None)
