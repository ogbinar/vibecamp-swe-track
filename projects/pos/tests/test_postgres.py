import os

import pytest
from sqlalchemy import create_engine, text


@pytest.mark.skipif(not os.getenv("POS_TEST_DATABASE_URL"), reason="PostgreSQL not requested")
def test_postgres_is_real_and_reachable() -> None:
    engine = create_engine(os.environ["POS_TEST_DATABASE_URL"])
    with engine.connect() as connection:
        assert connection.execute(text("SELECT current_setting('server_version')")).scalar_one()
