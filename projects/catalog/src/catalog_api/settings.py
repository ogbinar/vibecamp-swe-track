"""Validated configuration loaded from environment variables."""

from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings required before the application can start."""

    model_config = SettingsConfigDict(env_file=".env", env_prefix="CATALOG_", extra="ignore")

    service_name: str = Field(default=..., min_length=1)
    environment: Literal["development", "test", "production"] = "development"
