import os

import pytest
from sqlalchemy import create_engine, text


@pytest.mark.skipif(not os.getenv("ECOMMERCE_TEST_DATABASE_URL"), reason="PostgreSQL not requested")
def test_postgres_is_reachable() -> None:
    with create_engine(os.environ["ECOMMERCE_TEST_DATABASE_URL"]).connect() as connection:
        assert connection.execute(text("SELECT 1")).scalar_one() == 1
