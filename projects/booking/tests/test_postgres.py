import os
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier

import pytest
from sqlalchemy import Connection, Engine, create_engine, text


def run_on_two_connections_at_barrier[T](
    engine: Engine, action: Callable[[Connection], T]
) -> list[T]:
    """Coordinate setup mechanics while leaving booking behavior to the learner."""
    barrier = Barrier(2, timeout=5)

    def run() -> T:
        with engine.connect() as connection:
            barrier.wait()
            return action(connection)

    with ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run) for _ in range(2)]
        return [future.result(timeout=10) for future in futures]


@pytest.mark.skipif(not os.getenv("BOOKING_TEST_DATABASE_URL"), reason="PostgreSQL not requested")
def test_two_independent_connections_are_available() -> None:
    engine = create_engine(os.environ["BOOKING_TEST_DATABASE_URL"])
    backend_ids = run_on_two_connections_at_barrier(
        engine,
        lambda connection: connection.execute(text("SELECT pg_backend_pid()")).scalar_one(),
    )
    assert len(set(backend_ids)) == 2
