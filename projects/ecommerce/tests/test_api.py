from collections.abc import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from ecommerce_api.app import create_app
from ecommerce_api.settings import Settings


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app: FastAPI = create_app(
        Settings(
            service_name="Test Shop",
            database_url="postgresql+psycopg://unused",
            _env_file=None,
        )
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_anonymous_health_is_green(client: AsyncClient) -> None:
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


@pytest.mark.anyio
async def test_identity_routes_are_intentionally_absent(client: AsyncClient) -> None:
    assert (await client.post("/login", json={})).status_code == 404
