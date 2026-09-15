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
async def test_air_pages_preserve_the_learner_identity_boundary() -> None:
    api = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Test Shop",
            database_url="postgresql+psycopg://unused",
            _env_file=None,
        )
    )
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        login = await client.get("/app/login")
        orders = await client.get("/app/orders")
        fragment = await client.get("/app/payments/payment-1/status")
        schema = (await client.get("/openapi.json")).json()
        identity = await client.post("/login", json={})
    assert login.status_code == fragment.status_code == 200
    assert "remain your M5 implementation" in login.text
    assert "remain your M5 implementation" in orders.text
    assert "unknown" in fragment.text
    assert identity.status_code == 404
    assert all(not path.startswith("/app/") for path in schema["paths"])


@pytest.mark.anyio
async def test_payment_page_earns_one_htmx_fragment_without_custom_javascript() -> None:
    api = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Test Shop",
            database_url="postgresql+psycopg://unused",
            _env_file=None,
        )
    )
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/app/payments/payment-1")
    assert 'hx-get="/app/payments/payment-1/status"' in response.text
    assert 'hx-trigger="every 2s"' in response.text
    assert "<script" not in response.text
