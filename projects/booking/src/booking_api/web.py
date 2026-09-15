"""Air-owned page for the booking concurrency checkpoint."""

import air
from fastapi import FastAPI

from booking_lab.reservations import final_seat_inventory


def booking_summary() -> str:
    inventory = final_seat_inventory()
    return f"Starting inventory: {inventory.remaining} seat; {inventory.confirmed} confirmed."


def create_web_router() -> air.AirRouter:
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def booking_home() -> air.Main:
        return air.Main(
            air.H1("Booking"),
            air.P("Two buyers can see the same final seat before either confirms it."),
            air.P(booking_summary(), id_="booking-status"),
        )

    @router.get("/app/bookings")
    def bookings_page() -> air.Main:
        return air.Main(air.H1("Final-seat checkpoint"), air.P(booking_summary()))

    return router


def compose_app(api: FastAPI) -> air.Air:
    app = air.Air(fastapi_app=api)
    app.include_router(create_web_router(), include_in_schema=False)
    return app
