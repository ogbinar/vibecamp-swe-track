from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Learner models inherit here so Alembic can see one metadata registry."""
