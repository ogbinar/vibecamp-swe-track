from dataclasses import dataclass

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker


@dataclass(frozen=True)
class Database:
    engine: Engine
    sessions: sessionmaker[Session]


def build_database(url: str) -> Database:
    engine = create_engine(url, pool_pre_ping=True)
    return Database(engine, sessionmaker(engine, expire_on_commit=False))
