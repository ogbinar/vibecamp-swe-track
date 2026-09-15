"""Air pages and earned fragments over neutral ecommerce seams."""

import air
from fastapi import FastAPI

from ecommerce_api.provider_fake import FakeProvider


def payment_status(operation_id: str) -> str:
    """Use the deterministic provider boundary without creating order state."""
    return FakeProvider().lookup(operation_id=operation_id)


def create_web_router() -> air.AirRouter:
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def shop_home() -> air.Main:
        return air.Main(
            air.H1("Shop"),
            air.P("Customers need accounts, orders, and uncertain payments handled safely."),
            air.P(air.A("Account sign-in checkpoint", href="/app/login")),
            air.P(air.A("Order ownership checkpoint", href="/app/orders")),
            air.P(air.A("Payment status checkpoint", href="/app/payments/example")),
        )

    @router.get("/app/login")
    def login_page() -> air.Main:
        return air.Main(
            air.H1("Sign in"),
            air.P("The secure cookie session and identity checks remain your M5 implementation."),
        )

    @router.get("/app/orders")
    def orders_page() -> air.Main:
        return air.Main(
            air.H1("Your orders"),
            air.P(
                "Authentication, ownership checks, and safe order state remain "
                "your M5 implementation."
            ),
        )

    @router.get("/app/payments/{operation_id}")
    def payment_page(operation_id: str) -> air.Main:
        return air.Main(
            air.H1("Payment status"),
            air.P("A timeout can leave the result unknown; lookup must reconcile the fact."),
            air.Div(
                air.P(payment_status(operation_id)),
                id_="payment-status",
                hx_get=f"/app/payments/{operation_id}/status",
                hx_trigger="every 2s",
                hx_swap="innerHTML",
            ),
        )

    @router.get("/app/payments/{operation_id}/status")
    def payment_status_fragment(operation_id: str) -> air.P:
        return air.P(payment_status(operation_id), data_operation_id=operation_id)

    @router.get("/app/jobs")
    def jobs_page() -> air.Main:
        return air.Main(
            air.H1("Accepted work"),
            air.P("The durable outbox and worker state remain your M7 implementation."),
        )

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
