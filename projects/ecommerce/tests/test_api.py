from collections.abc import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from ecommerce_api.app import create_app
from ecommerce_api.settings import Settings
from ecommerce_api.web import compose_app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app: FastAPI = create_app(
        Settings(  # type: ignore[call-arg]
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


@pytest.mark.anyio
async def test_air_shell_preserves_learner_owned_routes() -> None:
    api = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Test Shop",
            database_url="postgresql+psycopg://unused",
            _env_file=None,
        )
    )
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        page = await client.get("/")
        schema = (await client.get("/openapi.json")).json()
        identity = await client.post("/login", json={})
        payment = await client.get("/app/payments/payment-1")
        jobs = await client.get("/app/jobs")
    assert page.status_code == 200
    assert "remain learner work" in page.text
    assert identity.status_code == 404
    assert payment.status_code == jobs.status_code == 404
    assert all(not path.startswith("/app/") for path in schema["paths"])
