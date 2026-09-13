from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from ecommerce_api.database import build_database
from ecommerce_api.settings import Settings


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(title=settings.service_name)
    database = build_database(settings.database_url)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": settings.service_name}

    @app.get("/ready")
    def ready() -> dict[str, str]:
        try:
            with database.engine.connect() as connection:
                connection.execute(text("SELECT 1"))
        except SQLAlchemyError as exc:
            raise HTTPException(status_code=503, detail="database unavailable") from exc
        return {"status": "ready"}

    return app
