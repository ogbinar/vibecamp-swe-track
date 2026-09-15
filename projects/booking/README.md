# Booking launch kit for M8

The in-memory observation path correctly reserves one seat once. The opt-in concurrency
harness coordinates two requests so they both observe the final seat.

```bash
uv sync --locked
cp .env.example .env
docker compose up -d --wait
uv run --locked alembic upgrade head
uv run --locked alembic current
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
BOOKING_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5434/vibecamp_booking uv run --locked pytest
PYTHONPATH=src uv run --locked pytest challenges/test_double_booking.py -q
```

Expected: PostgreSQL is current, API and two-connection seam tests pass, then
the challenge fails deterministically with
two confirmations and negative remaining inventory. Record the interleaving
before inspecting `reserve_at_barrier`.

Start the application with
`uv run --locked fastapi dev src/booking_api/main.py --port 8003`. Open `/` or
`/app/bookings` to see the Air final-seat checkpoint. It displays the neutral
starting state; the learner-owned database coordination remains absent.

Rerunning is the reset: each test creates new in-memory inventory. Use exactly
two workers for the deterministic exercise. A larger stress run is evidence
only after the two-worker failure is understood. The learner must move the
invariant into PostgreSQL and choose constraints, isolation, locking, and retry
behavior; this in-memory fixture is not the solution.

Add sequential reservation routes at the comment in `src/booking_api/app.py`.
After that path is green, extend `tests/test_postgres.py` into a coordinated
two-connection race; do not reuse one connection and call it concurrency.

Pause with `docker compose stop`. If startup fails, inspect `docker compose ps`
and `docker compose logs postgres`. To erase only this course database, export
the exact URL from `.env`, run
`uv run python scripts/reset.py --confirm-destroy-course-data`, and then
`uv run --locked alembic upgrade head`.
