# M2 challenge brief

Run from `projects/pos/`. Preserve the last green command before each scenario.

## **C1 — Model from behavior**

**YOU BUILD** — use the fixed M2 contract to create the schema and failure tests.

### Steps

1. Write representative reads before selecting tables or ORM mappings.
2. Create `tests/m2/test_schema.py` for duplicate SKU, orphan lines, negative quantities, and direct-SQL bypass.
3. Run README Block 1 and decide which rules belong in the application, database, or both.

### Hints

1. Ask which invalid row can enter without using the API.
2. Inspect identities, cardinality, foreign keys, checks, and `Base.metadata`.
3. Use the PostgreSQL constraint and SQLAlchemy mapping links in `RESOURCES.md`.

### Reset

Run `uv run --locked alembic current`. If the course database is disposable,
use the bounded reset in `projects/pos/README.md`, then rerun Block 1.

## **C2 — Slow and duplicated data access**

**YOU BUILD** — add query capture around the fixed cart-loading example.

### Steps

1. Create `tests/m2/test_persistence_api.py` and `tests/m2/test_migration_query.py`.
2. Record duplicated SQL, initial query count, and plan before changing code.
3. Keep the simple route direct; add only the repository boundary or index justified by measured duplication/query evidence, then rerun Blocks 2–3.

### Hints

1. Count statements before guessing that an index or repository will help.
2. Inspect query ownership, session lifetime, relationship loading, and the plan.
3. Use the SQLAlchemy session and PostgreSQL `EXPLAIN` links in `RESOURCES.md`.

### Reset

Remove only the current experiment, then run
`uv run --locked pytest tests/test_api.py -q` before measuring again.

## **C3 — Failed migration incident**

**PROVIDED** — use synthetic legacy SQL; you create and interrupt the learner migration.

### Steps

1. Upgrade empty and prior-revision databases; load `fixtures/m2-legacy-products.sql` only into the course database.
2. Interrupt the backfill once and record revision and row state.
3. Make it restartable, rerun Block 3, and document volume retention and reset.

### Hints

1. Compare the Alembic revision and rows already changed.
2. Inspect transaction boundaries, batches, compatibility, and uniqueness assumptions.
3. Use the Alembic links in `RESOURCES.md`; do not delete the volume to hide failure.

### Reset

Run `uv run --locked alembic current`, preserve the transcript, and use the
bounded reset only when the exercise explicitly starts over.

Refactor only after C2 evidence. Ship schema, migration, and query-plan evidence.
