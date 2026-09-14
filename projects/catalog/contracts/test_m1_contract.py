"""Opt-in black-box contract for M1; implementation is intentionally absent."""

from collections.abc import AsyncIterator

import pytest
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient

from catalog_api.app import create_app
from catalog_api.settings import Settings


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app: FastAPI = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="M1 Contract Catalog", environment="test", _env_file=None
        )
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


async def create_product(client: AsyncClient, sku: str, name: str = "Keyboard") -> None:
    response = await client.post("/products", json={"sku": sku, "name": name, "price": "19.99"})
    assert response.status_code == 201


@pytest.mark.anyio
async def test_create_and_retrieve_product(client: AsyncClient) -> None:
    response = await client.post(
        "/products", json={"sku": "KB-1", "name": "Keyboard", "price": "19.99"}
    )
    assert response.status_code == 201
    assert response.headers["location"] == "/products/KB-1"
    assert response.json() == {
        "sku": "KB-1",
        "name": "Keyboard",
        "price": "19.99",
        "active": True,
        "retirement_reason": None,
    }
    assert (await client.get("/products/KB-1")).json() == response.json()


@pytest.mark.anyio
async def test_duplicate_identity_is_a_conflict(client: AsyncClient) -> None:
    await create_product(client, "KB-1")
    response = await client.post(
        "/products", json={"sku": "KB-1", "name": "Other", "price": "20.00"}
    )
    assert response.status_code == 409
    assert response.json()["error"]["code"] == "product_exists"


@pytest.mark.anyio
async def test_missing_product_uses_stable_error(client: AsyncClient) -> None:
    response = await client.get("/products/MISSING")
    assert response.status_code == 404
    assert response.json() == {
        "error": {"code": "product_not_found", "message": "Product was not found"}
    }


@pytest.mark.anyio
async def test_replace_is_complete_and_atomic(client: AsyncClient) -> None:
    await create_product(client, "KB-1")
    invalid = await client.put("/products/KB-1", json={"name": "New name"})
    assert invalid.status_code == 422
    assert (await client.get("/products/KB-1")).json()["name"] == "Keyboard"
    replaced = await client.put("/products/KB-1", json={"name": "Quiet Keyboard", "price": "24.50"})
    assert replaced.status_code == 200
    assert replaced.json()["price"] == "24.50"


@pytest.mark.anyio
async def test_retirement_is_idempotent(client: AsyncClient) -> None:
    await create_product(client, "KB-1")
    first = await client.post("/products/KB-1/retire", json={"reason": "Discontinued"})
    second = await client.post("/products/KB-1/retire", json={"reason": "Discontinued"})
    assert first.status_code == second.status_code == 200
    assert first.json() == second.json()
    assert first.json()["active"] is False


@pytest.mark.anyio
async def test_list_is_bounded_and_stably_ordered(client: AsyncClient) -> None:
    for sku in ("C", "A", "B"):
        await create_product(client, sku)
    first = await client.get("/products", params={"limit": 2})
    assert first.status_code == 200
    assert [item["sku"] for item in first.json()["items"]] == ["A", "B"]
    assert first.json()["next"] == "B"
    final = await client.get("/products", params={"limit": 2, "after": "B"})
    assert [item["sku"] for item in final.json()["items"]] == ["C"]
    assert final.json()["next"] is None


@pytest.mark.anyio
async def test_invalid_price_and_limit_are_rejected(client: AsyncClient) -> None:
    product = await client.post(
        "/products", json={"sku": "KB-1", "name": "Keyboard", "price": "-1.00"}
    )
    page = await client.get("/products", params={"limit": 101})
    assert product.status_code == page.status_code == 422


def test_openapi_preserves_public_fields() -> None:
    app = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Contract", environment="test", _env_file=None
        )
    )
    schema = app.openapi()
    assert "/products" in schema["paths"]
    assert "/products/{sku}" in schema["paths"]
    product = schema["components"]["schemas"]["ProductResponse"]
    assert {"sku", "name", "price", "active", "retirement_reason"} <= set(product["properties"])
