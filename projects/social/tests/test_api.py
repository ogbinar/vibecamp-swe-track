from collections.abc import AsyncIterator

import pytest
from httpx import ASGITransport, AsyncClient

from social_api.app import create_app
from social_api.settings import Settings
from social_api.web import compose_app


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture
async def client() -> AsyncIterator[AsyncClient]:
    app = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Social Test", database_url="postgresql+psycopg://unused", _env_file=None
        )
    )
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as value:
        yield value


@pytest.mark.anyio
async def test_health_is_process_only(client: AsyncClient) -> None:
    assert (await client.get("/health")).json() == {"status": "ok", "service": "Social Test"}


@pytest.mark.anyio
async def test_air_feed_is_html_only_and_transport_is_absent() -> None:
    api = create_app(
        Settings(  # type: ignore[call-arg]
            service_name="Social Test", database_url="postgresql+psycopg://unused", _env_file=None
        )
    )
    app = compose_app(api)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        page = await client.get("/")
        event = await client.get("/app/feed/events")
        schema = (await client.get("/openapi.json")).json()
    assert page.status_code == 200
    assert "A small correct feed" in page.text
    assert "realtime transport remain learner work" in page.text
    assert "sse-connect" not in page.text
    assert event.status_code == 404
    assert all(not path.startswith("/app/") for path in schema["paths"])
