# POS launch kit for M2

This checkpoint proves the Air/FastAPI application can start and PostgreSQL can
be reached. It does not contain the POS schema or business solution.

Read [the bounded requirements brief](REQUIREMENTS.md) after this checkpoint is
green. It fixes behavior and invalid cases while leaving the schema to you.

```bash
cp .env.example .env
uv sync --locked
docker compose up -d --wait
uv run --locked alembic upgrade head
uv run --locked alembic current
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest
```

Expected: health and PostgreSQL smoke tests pass. Start the application with
`uv run --locked fastapi dev src/pos_api/main.py --port 8001`; `/` and
`/app/stock` show the Air checkpoint, `/health` proves the process is alive, and
`/ready` proves the database answers. The page states that durable stock is
still learner work.

Use `docker compose stop` to pause without deleting data. `docker compose down`
removes containers but keeps the named volume. Only when you intend to erase
course data, export `POS_DATABASE_URL`, run
`uv run python scripts/reset.py --confirm-destroy-course-data`, then run
`uv run --locked alembic upgrade head`. Never point the reset command at another
database.

To rehearse migration reversal after you add a reversible learner revision, run
`uv run --locked alembic downgrade -1`, inspect the schema, and then run
`uv run --locked alembic upgrade head`. The supplied baseline is the floor and
does not downgrade further.

If readiness fails, inspect `docker compose ps` and `docker compose logs postgres`.
If port 5432 is occupied, stop the conflicting local database or change both the
Compose mapping and URL. If Alembic disagrees with the database, run
`uv run alembic current` before creating or deleting a revision.
