"""Public response models for the catalog API."""

from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """A small liveness response."""

    status: Literal["ok"]
    service: str


class ProductResponse(BaseModel):
    """The one sample product supplied by the M0 starter."""

    sku: str = Field(min_length=1)
    name: str = Field(min_length=1)
    price: Decimal = Field(gt=0, decimal_places=2)
