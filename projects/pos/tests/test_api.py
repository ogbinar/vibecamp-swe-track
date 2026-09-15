from collections.abc import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from pos_api.app import create_app
from pos_api.settings import Settings
from pos_api.web import compose_app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app: FastAPI = create_app(
        Settings(service_name="Test POS", database_url="postgresql+psycopg://invalid")
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_health_does_not_claim_database_readiness(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "Test POS"}


@pytest.mark.anyio
async def test_air_stock_checkpoint_does_not_pollute_openapi() -> None:
    api = create_app(Settings(service_name="Test POS", database_url="postgresql+psycopg://invalid"))
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        page = await client.get("/app/stock")
        schema = (await client.get("/openapi.json")).json()
    assert page.status_code == 200
    assert page.headers["content-type"].startswith("text/html")
    assert "No stock records yet" in page.text
    assert "/app/stock" not in schema["paths"]
    assert "/health" in schema["paths"]
