"""Test-only SQL statement counter for M2 query-shape evidence."""

from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import Engine, event


@contextmanager
def count_statements(engine: Engine) -> Iterator[list[str]]:
    statements: list[str] = []

    def capture(
        _connection: object,
        _cursor: object,
        statement: str,
        _parameters: object,
        _context: object,
        _executemany: bool,
    ) -> None:
        statements.append(statement)

    event.listen(engine, "before_cursor_execute", capture)
    try:
        yield statements
    finally:
        event.remove(engine, "before_cursor_execute", capture)
