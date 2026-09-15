"""Air-owned HTML page for the neutral Catalog starter."""

import air

from catalog_api.service import sample_product


def layout(*children: str | air.BaseTag | air.SafeStr | int | float) -> air.Html:
    """Render the small shared page shell with Air Tags."""
    return air.Html(
        air.Head(
            air.Title("VibeCamp Catalog"),
            air.Meta(charset="utf-8"),
            air.Meta(name="viewport", content="width=device-width, initial-scale=1"),
        ),
        air.Body(air.Main(*children)),
        lang="en",
    )


def create_web_router() -> air.AirRouter:
    """Create an isolated, OpenAPI-excluded page router."""
    router = air.AirRouter(include_in_schema=False)

    @router.get("/")
    def catalog_page() -> air.Html:
        product = sample_product()
        return layout(
            air.H1("Catalog"),
            air.P("A storefront needs one dependable place to see what it can sell."),
            air.Ul(
                air.Li(
                    air.Strong(product.name),
                    f" — {product.sku} — {product.price:.2f}",
                )
            ),
        )

    return router
