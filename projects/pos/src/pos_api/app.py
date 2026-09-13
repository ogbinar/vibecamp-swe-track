from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from pos_api.database import build_engine
from pos_api.settings import Settings


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(title=settings.service_name)
    engine = build_engine(settings.database_url)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "service": settings.service_name}

    @app.get("/ready")
    def ready() -> dict[str, str]:
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))
        except SQLAlchemyError as exc:
            raise HTTPException(status_code=503, detail="database unavailable") from exc
        return {"status": "ready"}

    return app
