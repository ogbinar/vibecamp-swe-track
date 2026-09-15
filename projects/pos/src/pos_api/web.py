"""Air-owned pages for the neutral POS starting checkpoint."""

import air
from fastapi import FastAPI


def stock_summary() -> str:
    """Name the visible baseline without inventing learner-owned stock rows."""
    return "No stock records yet. Your M2 model and migration will make them durable."


def create_web_router() -> air.AirRouter:
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def pos_home() -> air.Main:
        return air.Main(
            air.H1("Point of sale"),
            air.P("A cashier needs stock and carts to survive an application restart."),
            air.P(stock_summary(), id_="stock-status"),
        )

    @router.get("/app/stock")
    def stock_page() -> air.Main:
        return air.Main(air.H1("Stock"), air.P(stock_summary(), id_="stock-status"))

    @router.get("/app/checkout")
    def checkout_page() -> air.Main:
        return air.Main(
            air.H1("Checkout checkpoint"),
            air.P(
                "Atomic inventory, payment, and receipt behavior remains your M3 implementation."
            ),
            air.P("The optional cashier display name remains the single fixed M4 change."),
        )

    @router.get("/app/operator")
    def operator_page() -> air.Main:
        return air.Main(
            air.H1("Tenant-aware operator checkpoint"),
            air.P(
                "Tenant selection, isolation, audit, readiness, and recovery remain your M10 work."
            ),
        )

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
