"""Small shared use cases called directly by page and API handlers."""

from decimal import Decimal

from catalog_api.models import ProductResponse


def sample_product() -> ProductResponse:
    """Return the starter product without coupling it to a transport."""
    return ProductResponse(sku="VC-001", name="Mechanical Keyboard", price=Decimal("19.99"))
