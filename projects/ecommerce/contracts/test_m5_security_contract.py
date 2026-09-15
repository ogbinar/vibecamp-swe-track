"""Opt-in M5 black-box contract; identity implementation is learner work."""

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
def app() -> FastAPI:
    return create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Security Contract",
            database_url="postgresql+psycopg://unused",
            _env_file=None,
        )
    )


@pytest.fixture
async def client(app: FastAPI) -> AsyncIterator[AsyncClient]:
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


def assert_route_exists(app: FastAPI, path: str, method: str) -> None:
    assert any(route.path == path and method in (route.methods or set()) for route in app.routes), (
        f"Implement {method} {path} before testing its security behavior"
    )


@pytest.mark.anyio
async def test_registration_never_accepts_a_client_role(app: FastAPI, client: AsyncClient) -> None:
    assert_route_exists(app, "/registrations", "POST")
    response = await client.post(
        "/registrations",
        json={"email": "alice@example.test", "password": "synthetic passphrase", "role": "admin"},
    )
    assert response.status_code == 201
    assert response.json()["role"] == "customer"


@pytest.mark.anyio
async def test_login_failure_does_not_enumerate_identity(app: FastAPI, client: AsyncClient) -> None:
    assert_route_exists(app, "/sessions", "POST")
    unknown = await client.post(
        "/sessions", json={"email": "unknown@example.test", "password": "wrong"}
    )
    known = await client.post(
        "/sessions", json={"email": "alice@example.test", "password": "wrong"}
    )
    assert (unknown.status_code, unknown.json()) == (known.status_code, known.json())


@pytest.mark.anyio
async def test_customer_cannot_read_another_customers_order(
    app: FastAPI, client: AsyncClient
) -> None:
    assert_route_exists(app, "/orders/{order_id}", "GET")
    response = await client.get("/orders/order-owned-by-bob", headers={"X-Test-Actor": "alice"})
    assert response.status_code in {403, 404}


@pytest.mark.anyio
async def test_forbidden_transition_does_not_change_order(
    app: FastAPI, client: AsyncClient
) -> None:
    assert_route_exists(app, "/orders/{order_id}/transition", "POST")
    assert_route_exists(app, "/orders/{order_id}", "GET")
    denied = await client.post(
        "/orders/fulfilled-order/transition",
        json={"command": "pay"},
        headers={"X-Test-Actor": "alice"},
    )
    assert denied.status_code == 409
    current = await client.get("/orders/fulfilled-order", headers={"X-Test-Actor": "alice"})
    assert current.json()["state"] == "fulfilled"
