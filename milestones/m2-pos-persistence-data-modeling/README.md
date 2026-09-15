# M2 — Make stock survive a restart

[Course home](../../README.md) / M2

**Milestone 3 of 11 · M2**

## Business problem

The catalog forgets everything when it restarts. Build a point-of-sale (POS)
system whose data survives and whose database rejects impossible records.

## Product objective

- **Product can:** stock and carts survive restart in PostgreSQL.
- **You will prove:** schema, migration, restart, constraint, and query-shape evidence.

Read the [bounded POS requirements](../../projects/pos/REQUIREMENTS.md) and the
[M2 persistence contract](../../projects/pos/specs/M2-PERSISTENCE-CONTRACT.md), then
model products, inventory locations, stock receipts, carts, and line items. Read
[REFERENCE.md](REFERENCE.md#m2-concepts-through-data-problems), then complete C1–C3 in
[CHALLENGE.md](CHALLENGE.md#m2-challenge-brief): write query examples first, implement schema and
SQLAlchemy mappings, justify indexes from those queries, and recover a failed
migration. Keep the empty baseline migration; add your own revision after it.

Do not add authentication, Redis, workers, generic base repositories, or async
database access. The learner owns tables, constraints, indexes, and boundaries.

## Start here

- **Gate:** [A1–A5 / Level B](ACCEPTANCE.md#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-model-the-fixed-queries-required).

Start in `projects/pos/`. From that directory, run the ordered commands in its
README. Expected: the API and real PostgreSQL smoke tests pass. If not, use its
database and Alembic recovery steps before designing tables.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Model the fixed queries `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m2/test_schema.py` and the output named below. Record `evidence/M2/schema.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 1](#1-model-the-fixed-queries-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--model-from-behavior) and [concept explanation](REFERENCE.md#the-tables-do-not-support-the-required-reads). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

Outcome: store products, locations, stock, and carts without impossible rows.
**Supplied:** the [persistence contract](../../projects/pos/specs/M2-PERSISTENCE-CONTRACT.md),
empty migration, and PostgreSQL shell. **You build:** models, metadata, a domain
migration, and constraint tests in `projects/pos/`. Run
`uv run --locked alembic upgrade head`; observe a clean upgrade and specific
constraint failures. Record `evidence/M2/schema.md`. Diagnose with
`uv run --locked alembic current`; stop when a fresh database upgrades cleanly.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m2/test_schema.py -q
```

### 2. Earn a data-access boundary `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m2/test_persistence_api.py` and the output named below. Record `evidence/M2/persistence.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 2](#2-earn-a-data-access-boundary-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--slow-and-duplicated-data-access) and [concept explanation](REFERENCE.md#the-product-vanished-after-restart).

Create request-scoped session injection and API/integration tests. A simple
route may call SQLAlchemy directly. Add a repository only for demonstrated
repeated/complex data access, and a service only for orchestration or invariants;
the use case owns commit/rollback and repositories never commit. Run
the POS README test block; observe data after an API restart. Record
`evidence/M2/persistence.md`. Stop when it passes twice across a restart.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m2/test_persistence_api.py -q
```

### 3. Migrate and inspect `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m2/test_migration_query.py` and the output named below. Record `evidence/M2/migration-and-query.md`.
Stop when this block's listed command passes and its evidence is saved.
Resume at [Block 3](#3-migrate-and-inspect-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--failed-migration-incident) and [concept explanation](REFERENCE.md#the-empty-migration-passed-but-existing-data-failed).

Load `fixtures/m2-legacy-products.sql` into a disposable database, backfill it,
interrupt once, and recover. Capture cart-loading query count and one `EXPLAIN`
plan. Record `evidence/M2/migration-and-query.md`. Use only the documented reset;
stop when both legacy rows survive and the index decision cites the plan.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m2/test_migration_query.py -q
```

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Relational model:** tables and relationships representing product facts.
- **Constraint:** a database rule that rejects invalid data.
- **Index:** an extra structure that speeds a named query at write/storage cost.
- **Migration:** a versioned change that moves a database schema forward or back.
- **Repository:** code owning repeated data access; it must not hide transactions.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A5](ACCEPTANCE.md#core) with PostgreSQL-backed tests, SQL examples,
migration transcripts, and query plans. Use [REFERENCE.md](REFERENCE.md#tools-earned-here) only when the
problem reaches that tool. Use [REFERENCE.md](REFERENCE.md#resources-for-m2) and the three-level
hints in the challenge if blocked.

## Done / next

A clean database upgrades, existing data migrates, constraints fail specifically,
and [A1–A5](ACCEPTANCE.md#core) pass. Tag `m2-pos-persistence`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m2) only for the question left by the active hint ladder.

Use the exact stop/reset and Alembic diagnosis commands in the
[POS README](../../projects/pos/README.md). Never delete an unexplained volume.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M3](../m3-transactions-correctness/README.md).

[Previous milestone: M1](../m1-production-api-foundation/README.md) · [Course home](../../README.md) · [Next milestone: M3](../m3-transactions-correctness/README.md)
