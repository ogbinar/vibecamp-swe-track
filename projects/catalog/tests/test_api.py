"""Public-boundary tests for the M0 catalog starter."""

from collections.abc import AsyncIterator

import air
import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from pydantic import ValidationError

from catalog_api.app import create_app
from catalog_api.settings import Settings
from catalog_api.web import create_web_router


@pytest.fixture
def anyio_backend() -> str:
    """Keep this starter on Python's built-in asyncio backend."""
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    settings = Settings(  # type: ignore[call-arg]
        service_name="Test Catalog", environment="test", _env_file=None
    )
    app: FastAPI = create_app(settings)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.fixture
async def composed_client() -> AsyncIterator[AsyncClient]:
    settings = Settings(  # type: ignore[call-arg]
        service_name="Test Catalog", environment="test", _env_file=None
    )
    api = create_app(settings)
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
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
        Settings(_env_file=None)  # type: ignore[call-arg]


def test_empty_service_name_is_rejected() -> None:
    with pytest.raises(ValidationError):
        Settings(  # type: ignore[call-arg]
            service_name="", _env_file=None
        )


@pytest.mark.anyio
async def test_air_page_and_fastapi_api_share_the_sample_product(
    composed_client: AsyncClient,
) -> None:
    page = await composed_client.get("/")
    api = await composed_client.get("/products/sample")

    assert page.status_code == api.status_code == 200
    assert page.headers["content-type"].startswith("text/html")
    assert api.headers["content-type"].startswith("application/json")
    assert api.json()["name"] in page.text


@pytest.mark.anyio
async def test_air_routes_stay_out_of_openapi(composed_client: AsyncClient) -> None:
    schema = (await composed_client.get("/openapi.json")).json()

    assert "/health" in schema["paths"]
    assert "/products/sample" in schema["paths"]
    assert "/" not in schema["paths"]
    assert "/app/products/draft" not in schema["paths"]


@pytest.mark.anyio
async def test_invalid_air_form_preserves_safe_values(composed_client: AsyncClient) -> None:
    form_page = await composed_client.get("/app/products/draft")
    token = form_page.text.split('name="csrf_token" value="', 1)[1].split('"', 1)[0]
    response = await composed_client.post(
        "/app/products/draft",
        data={"csrf_token": token, "sku": "SAFE-1", "name": "Keyboard", "price": "-1"},
    )

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert 'value="SAFE-1"' in response.text
    assert 'value="-1"' in response.text
    assert "greater than the minimum" in response.text


@pytest.mark.anyio
async def test_valid_air_form_does_not_persist_a_learner_solution(
    composed_client: AsyncClient,
) -> None:
    form_page = await composed_client.get("/app/products/draft")
    token = form_page.text.split('name="csrf_token" value="', 1)[1].split('"', 1)[0]
    response = await composed_client.post(
        "/app/products/draft",
        data={"csrf_token": token, "sku": "SAFE-1", "name": "Keyboard", "price": "19.99"},
    )

    assert response.status_code == 200
    assert "Draft SAFE-1 is valid. Nothing was saved." in response.text
    assert (await composed_client.get("/products/SAFE-1")).status_code == 404
