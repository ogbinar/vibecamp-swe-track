# Social launch kit for M9

The in-memory observation feed is correct. The opt-in workload exposes one profile lookup per
post—the shape of an N+1 query problem—using a stable call count instead of a
fragile wall-clock threshold.

```bash
uv sync --locked
cp .env.example .env
docker compose up -d --wait
uv run --locked alembic upgrade head
uv run --locked alembic current
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
SOCIAL_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5435/vibecamp_social uv run --locked pytest
PYTHONPATH=src uv run --locked python scripts/seed_reference.py
PYTHONPATH=src uv run --locked pytest challenges/test_query_budget.py -q
```

Expected: the migration is current, health/query-capture checks pass, the seed
script prints the fixed workload, and the query-budget challenge reports 100
calls where at most two are allowed. The fixed dataset has 100 posts: 70 from
one high-fan-out author and 30 spread across nine authors. Rerunning creates
clean deterministic data.

Start the application with
`uv run --locked fastapi dev src/social_api/main.py --port 8004`. Open `/` for
the Air feed or request `/app/feed/events` to observe one non-durable server-
sent event. Query repair, caching authority, reconnect/gap policy, and the
learner-built feed remain absent.

This fixture teaches measurement shape; PostgreSQL remains the required source
of truth for the milestone. The learner must reproduce the issue with real
SQLAlchemy queries and `EXPLAIN`, then decide indexes, pagination, cache, and
realtime behavior from evidence.

Add the database feed at the comment in `src/social_api/app.py`. Capture query
statements through the supplied SQLAlchemy event seam and run `EXPLAIN` on the
real feed query before adding indexes or Redis.

After your `/feed` route exists, run
`uv run --locked python scripts/load_reference.py --requests 20`. This is a
single-client correctness/load seam, not a production benchmark; record the
environment and extend concurrency only after its results are stable.

Pause with `docker compose stop`. If startup fails, inspect `docker compose ps`
and `docker compose logs postgres`. To erase only this course database, export
the exact URL from `.env`, run
`uv run python scripts/reset.py --confirm-destroy-course-data`, and then
`uv run --locked alembic upgrade head`.
