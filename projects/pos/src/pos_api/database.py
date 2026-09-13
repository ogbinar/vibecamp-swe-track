from sqlalchemy import Engine, create_engine


def build_engine(database_url: str) -> Engine:
    """Build the application-owned engine once during assembly."""
    return create_engine(database_url, pool_pre_ping=True)
