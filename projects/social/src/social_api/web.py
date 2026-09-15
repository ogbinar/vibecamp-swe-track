"""Air page for the neutral social feed checkpoint."""

import air
from fastapi import FastAPI

from social_lab.feed import CountingProfiles, Post, render_feed


def sample_feed() -> list[dict[str, str]]:
    """Reuse the measured feed seam; database optimization remains learner work."""
    return render_feed(
        [Post("ada", "A small correct feed comes before cache or realtime.")],
        CountingProfiles({"ada": "Ada"}),
    )


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
            ),
            air.P("Measurement, cache, and realtime transport remain learner work."),
        )

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
