import os

import pytest
from sqlalchemy import create_engine, event, text


@pytest.mark.skipif(not os.getenv("SOCIAL_TEST_DATABASE_URL"), reason="PostgreSQL not requested")
def test_query_capture_and_explain_seams() -> None:
    engine = create_engine(os.environ["SOCIAL_TEST_DATABASE_URL"])
    statements: list[str] = []

    @event.listens_for(engine, "before_cursor_execute")
    def capture(
        _conn: object,
        _cursor: object,
        statement: str,
        _parameters: object,
        _context: object,
        _many: bool,
    ) -> None:
        statements.append(statement)

    with engine.connect() as connection:
        plan = connection.execute(text("EXPLAIN SELECT 1")).all()
    assert plan
    assert any("EXPLAIN" in statement for statement in statements)
