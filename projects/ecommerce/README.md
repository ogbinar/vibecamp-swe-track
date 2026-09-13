# Ecommerce launch kit for M5

This is a green anonymous shell, not an authentication solution. Read the M5
threat brief and isolated scenarios before adding users or credentials.
The product boundary is in [REQUIREMENTS.md](REQUIREMENTS.md); callable attack
descriptions remain disabled in `fixtures/SECURITY-SCENARIOS.md`. The Core client
is a first-party browser, so M5 uses an opaque server-side session referenced by
a secure cookie. JSON Web Token (JWT) implementation is Stretch.

```bash
cp .env.example .env
uv sync --locked
docker compose up -d --wait
uv run --locked alembic upgrade head
uv run --locked alembic current
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest
```

Expected: the baseline migration is current and all tests pass; `/health` works,
`/ready` proves PostgreSQL answers, and `/login` is intentionally absent.
Start with `uv run --locked fastapi dev src/ecommerce_api/main.py --port 8002`.
Stop with `Ctrl+C`.

When M5 tells you to begin the identity contract, run
`uv run --locked pytest contracts/test_m5_security_contract.py -q`. It initially
fails with missing routes. Implement one published behavior at a time; never add
an `X-Test-Actor` bypass to runtime code—replace that synthetic header with your
real authenticated test fixture.

M6 also supplies `FakeProvider`, with success, decline, timeout-before, and
timeout-after modes. M7 supplies `outbox_lab.py` with deterministic process-death
windows. These reproduce uncertainty; they do not implement retries, durable
work, idempotent consumers, or reconciliation for you.

If configuration fails, copy `.env.example` from this directory. If an identity
route exists before you build it, inspect the diff and remove accidental shared
business code. Security scenarios live in `fixtures/` and are documentation,
never enabled vulnerable endpoints. The doubles keep state only in memory, so
rerun pytest for a clean case.

Pause with `docker compose stop`; resume with `docker compose up -d --wait`.
To erase only the course database, export the exact URL from `.env`, run
`uv run python scripts/reset.py --confirm-destroy-course-data`, then run
`uv run --locked alembic upgrade head`. The reset refuses any database name
other than `vibecamp_ecommerce`. Inspect `docker compose ps` and
`docker compose logs postgres` before resetting a failed start.
