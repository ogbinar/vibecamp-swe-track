from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from booking_api.app import create_app
from booking_api.settings import Settings
from booking_api.web import compose_app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Booking Test", database_url="postgresql+psycopg://unused", _env_file=None
        )
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_health_is_process_only(client: AsyncClient) -> None:
    assert (await client.get("/health")).json() == {"status": "ok", "service": "Booking Test"}


@pytest.mark.anyio
async def test_air_booking_page_keeps_the_race_as_learner_work() -> None:
    api = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Booking Test", database_url="postgresql+psycopg://unused", _env_file=None
        )
    )
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/app/bookings")
        schema = (await client.get("/openapi.json")).json()
    assert response.status_code == 200
    assert "Starting inventory: 1 seat; 0 confirmed" in response.text
    assert "/app/bookings" not in schema["paths"]
