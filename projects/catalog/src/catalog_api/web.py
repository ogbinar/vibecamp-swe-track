"""Air-owned HTML pages and forms for the Catalog starter."""

import air

from catalog_api.models import ProductDraft
from catalog_api.service import sample_product


class ProductDraftForm(air.AirForm[ProductDraft]):
    """Validate a product draft without supplying M1 persistence behavior."""


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


def draft_page(form: ProductDraftForm, message: str | None = None) -> air.Html:
    """Render the form, preserving submitted values and safe validation errors."""
    content: list[str | air.BaseTag | air.SafeStr | int | float] = [
        air.H1("Check a product draft"),
        air.P("Validate what a catalog client would send before building storage."),
    ]
    if message:
        content.append(air.P(message, role="status"))
    content.append(
        air.Form(
            air.Raw(form.render()),
            air.Button("Check draft", type="submit"),
            action="/app/products/draft",
            method="post",
        )
    )
    content.append(air.P(air.A("Back to catalog", href="/")))
    return layout(*content)


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
            air.P(air.A("Check a product draft", href="/app/products/draft")),
        )

    @router.get("/app/products/draft")
    def product_draft() -> air.Html:
        return draft_page(ProductDraftForm())

    @router.post("/app/products/draft")
    async def check_product_draft(request: air.Request) -> air.Html:
        form = await ProductDraftForm.from_request(request)
        if not form.is_valid:
            return draft_page(form)
        draft = form.data
        return draft_page(
            ProductDraftForm(initial_data=form.save_data()),
            f"Draft {draft.sku} is valid. Nothing was saved.",
        )

    return router
