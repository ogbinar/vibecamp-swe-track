from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="ECOMMERCE_")
    service_name: str = Field(default=..., min_length=1)
    database_url: str = Field(default=..., min_length=1)
