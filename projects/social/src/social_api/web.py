"""Air feed pages and the bounded server-sent-event transport checkpoint."""

from collections.abc import AsyncIterator

import air
from fastapi import FastAPI

from social_lab.feed import CountingProfiles, Post, render_feed


def sample_feed() -> list[dict[str, str]]:
    """Reuse the measured feed seam; database optimization remains learner work."""
    return render_feed(
        [Post("ada", "A small correct feed comes before cache or realtime.")],
        CountingProfiles({"ada": "Ada"}),
    )


async def feed_events() -> AsyncIterator[str]:
    """Emit one non-durable event; reconnect and gap policy remain learner work."""
    for item in sample_feed():
        yield str(air.Article(air.Strong(item["author"]), air.P(item["text"])))


def create_web_router() -> air.AirRouter:
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def social_home() -> air.Main:
        items = sample_feed()
        return air.Main(
            air.H1("Social feed"),
            air.P("The feed must stay correct and fast as posts and readers grow."),
            air.Section(
                *(air.Article(air.Strong(item["author"]), air.P(item["text"])) for item in items),
                id_="feed",
                hx_ext="sse",
                sse_connect="/app/feed/events",
                sse_swap="message",
                hx_swap="beforeend",
            ),
        )

    @router.get("/app/feed")
    def feed_fragment() -> air.Section:
        return air.Section(
            *(
                air.Article(air.Strong(item["author"]), air.P(item["text"]))
                for item in sample_feed()
            )
        )

    @router.get("/app/feed/events")
    def feed_event_stream() -> air.SSEResponse:
        return air.SSEResponse(feed_events())

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
