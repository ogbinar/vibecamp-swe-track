# Ecommerce launch kit for M5

This is a green anonymous shell, not an authentication solution. Read the M5
threat brief and isolated scenarios before adding users or credentials.
The product boundary is in [REQUIREMENTS.md](REQUIREMENTS.md); callable attack
descriptions remain disabled in
[SECURITY-SCENARIOS.md](fixtures/SECURITY-SCENARIOS.md). The Core client is a
first-party browser, so M5 uses an opaque server-side session referenced by a
secure cookie. JSON Web Token (JWT) implementation is Stretch.

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
`/ready` proves PostgreSQL answers, `/` is a neutral Air shell, and identity,
order, payment-status, job, and FastAPI `/login` routes are intentionally absent.
Start with `uv run --locked fastapi dev src/ecommerce_api/main.py --port 8002`.
Stop with `Ctrl+C`.

When M5 tells you to begin the identity contract, run
`uv run --locked pytest contracts/test_m5_security_contract.py -q`. It initially
fails with missing routes. Implement one published behavior at a time; never add
an `X-Test-Actor` bypass to runtime code—replace that synthetic header with your
real authenticated test fixture.

## M6 preflight after completing M5

Use this checkpoint only after the M5 Core gate is green. It validates the
identity, authorization, and order-state work you now own; the anonymous-shell
expectations above apply only when starting M5.

From `projects/ecommerce/`:

```bash
test -s tests/m5/test_identity.py
test -s tests/m5/test_authorization_matrix.py
test -s tests/m5/test_order_state.py
ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5 -q
uv run --locked pytest tests/test_failure_harnesses.py -q
```

Expected: the learner-built M5 tests pass and the supplied provider-failure
harness remains green. If an M5 target is missing or red, return to that M5
block and its saved evidence; do not remove completed identity routes or reset
the database merely to recreate the anonymous starter. If only the supplied
failure harness is red, leave M5 intact and diagnose the fake/fixture boundary.

M6 supplies `FakeProvider`, with success, decline, timeout-before, and
timeout-after modes. You build the payment-status fragment after the measured
need appears. M7 supplies `outbox_lab.py` with deterministic process-death
windows. These reproduce uncertainty; they do not implement retries, durable
work, idempotent consumers, or reconciliation for you.

If configuration fails, copy `.env.example` from this directory. When starting
M5 only, if an identity or order route exists before you build it, inspect the
diff and remove accidental shared business code. Never apply that anonymous-shell repair
after completing M5 or while working in M6. Security scenarios live in
`fixtures/` and are documentation, never enabled vulnerable endpoints. The
doubles keep state only in memory, so rerun pytest for a clean case.

Pause with `docker compose stop`; resume with `docker compose up -d --wait`.
To erase only the course database, export the exact URL from `.env`, run
`uv run python scripts/reset.py --confirm-destroy-course-data`, then run
`uv run --locked alembic upgrade head`. The reset refuses any database name
other than `vibecamp_ecommerce`. Inspect `docker compose ps` and
`docker compose logs postgres` before resetting a failed start.
