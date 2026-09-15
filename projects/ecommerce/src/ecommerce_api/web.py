"""Air page for the neutral ecommerce shell."""

import air
from fastapi import FastAPI


def create_web_router() -> air.AirRouter:
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def shop_home() -> air.Main:
        return air.Main(
            air.H1("Shop"),
            air.P("Customers need accounts, orders, and uncertain payments handled safely."),
            air.P("Identity, order, payment, and job behavior remain learner work."),
        )

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
