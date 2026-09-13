from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from booking_api.app import create_app
from booking_api.settings import Settings


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app = create_app(
        Settings(
            service_name="Booking Test", database_url="postgresql+psycopg://unused", _env_file=None
        )
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_health_is_process_only(client: AsyncClient) -> None:
    assert (await client.get("/health")).json() == {"status": "ok", "service": "Booking Test"}
