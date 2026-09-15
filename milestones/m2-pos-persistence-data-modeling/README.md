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
[reference](#m2-concepts-through-data-problems), then complete C1–C3 in
[challenge brief](#challenge-brief): write query examples first, implement schema and
SQLAlchemy mappings, justify indexes from those queries, and recover a failed
migration. Keep the empty baseline migration; add your own revision after it.

Do not add authentication, Redis, workers, generic base repositories, or async
database access. The learner owns tables, constraints, indexes, and boundaries.

## Start here

- **Gate:** [A1–A5 / Level B](#core).
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
When needed: [C1 scenario and hints](#c1--model-from-behavior) and [concept explanation](#the-tables-do-not-support-the-required-reads). [Tool boundaries](#tools-earned-here) apply to this product.

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
When needed: [C2 scenario and hints](#c2--slow-and-duplicated-data-access) and [concept explanation](#the-product-vanished-after-restart).

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
When needed: [C3 scenario and hints](#c3--failed-migration-incident) and [concept explanation](#the-empty-migration-passed-but-existing-data-failed).

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

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A5](#core) with PostgreSQL-backed tests, SQL examples,
migration transcripts, and query plans. Use [reference](#tools-earned-here) only when the
problem reaches that tool. Use [reference](#resources-for-m2) and the three-level
hints in the challenge if blocked.

## Done / next

A clean database upgrades, existing data migrates, constraints fail specifically,
and [A1–A5](#core) pass. Tag `m2-pos-persistence`.

### Recovery

Use [targeted references](#resources-for-m2) only for the question left by the active hint ladder.

Use the exact stop/reset and Alembic diagnosis commands in the
[POS README](../../projects/pos/README.md). Never delete an unexplained volume.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M3](../m3-transactions-correctness/README.md).

[Previous milestone: M1](../m1-production-api-foundation/README.md) · [Course home](../../README.md) · [Next milestone: M3](../m3-transactions-correctness/README.md)


---

## Challenge brief

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
3. Use the PostgreSQL constraint and SQLAlchemy mapping links in the Reference section below.

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
3. Use the SQLAlchemy session and PostgreSQL `EXPLAIN` links in the Reference section below.

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
3. Use the Alembic links in the Reference section below; do not delete the volume to hide failure.

### Reset

Run `uv run --locked alembic current`, preserve the transcript, and use the
bounded reset only when the exercise explicitly starts over.

Refactor only after C2 evidence. Ship schema, migration, and query-plan evidence.


---

## Acceptance gate

Required maturity: **Level B** for the persistent POS slice.

## Core

- **A1:**
  - [ ] ER rationale and executable SQL cover relationships
  - [ ] Psycopg 3 connects SQLAlchemy to PostgreSQL
  - [ ] PostgreSQL integration tests—not SQLite substitutes—prove unique, FK, nullability, and value constraints plus API/application error translation for C1.
- **A2:**
  - [ ] Indexes map to named access paths with before/after plan or timing evidence
  - [ ] query count is bounded and a seeded N+1/duplicated-access regression fails an automated guard.
- **A3:**
  - [ ] `alembic upgrade head` works on empty and prior-revision fixtures
  - [ ] interrupted/invalid backfill C3 is recovered and rerun without data loss
  - [ ] Compose persistence/reset behavior is proven.
- **A4:**
  - [ ] Request/use-case session scope is explicit
  - [ ] a simple route may call SQLAlchemy directly; any service/repository names the observed orchestration, invariant, duplication, or substitution that earned it, and repositories never commit
  - [ ] induced flush error rolls back and leaves later work usable
  - [ ] synchronous session behavior is the documented baseline, and any async proposal includes representative before/after evidence plus pool/failure/complexity analysis
  - [ ] M2 API, PostgreSQL integration, migration, Ruff, mypy, and validator commands pass cleanly.
- **A5:**
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces one product/inventory field from source through relational and derived storage.
  - [ ] The review identifies access, retention/deletion, and backup implications.
  - [ ] Every claim links evidence or a precise later-milestone deferral.

## Execution map

Each checklist bullet is a local step in order. From `projects/pos/`, use README
Block 1 for A1, Block 3 for A2–A3, Block 2 plus the full POS check block for A4,
and `test -s evidence/M2/data-lifecycle.md` for A5. Expected: every step is
observable and green or has a precise N/A deferral. Record under the matching A
heading; recover with `uv run --locked alembic current` and the bounded reset.

Evidence includes schema revision, SQL/commands, expected/actual rows, and interpretation.

## Stretch

Compare FastCRUD or a pagination adapter against explicit behavior. Retain it only if Core stays legible and fully tested.

## Review

### Review

Answer one question at a time in `evidence/M2/index.md`:

1. Which invariant belongs in application code, the database, or both?
2. Who opens, rolls back, and closes the session?
3. What duplication did normalization remove, and what query cost did it add?
4. Which query does each index serve, and what does it cost on writes?
5. What measured statement count proves the N+1 problem?
6. Why must migration tests include existing rows?
7. Does the failed-migration runbook restore a green state without hidden steps?
8. Is the backfill safe to restart? Show the observation.
9. What measurement—not `async def` syntax—would earn `AsyncSession`?
10. Does the reset command refuse a non-course database?
11. Which observed pressure earns each service or repository, and which simple path stays direct?

Trace one representative field with the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A5 gate): a career-shifter connects a prior-domain recordkeeping rule to a database invariant; a data specialist explains how strong SQL work still depends on API/session ownership and operational recovery.


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M2 concepts through data problems

## “The product vanished after restart”

**Example:** a catalog held only in a Python dictionary disappears. **Term —
persistence:** keeping facts beyond one process lifetime. **Rule:** model product
identity, relationships, and required reads before choosing tables.

## “One write bypassed the API check”

**Example:** direct SQL inserts negative quantity. **Term — constraint:** a
database rule that protects every writer. **Rule:** keep friendly validation in
the application and critical truth in the database too.

## “The tables do not support the required reads”

**Example:** a cart needs several fragile joins because identities and relationships
were never written down. **Term — relational model:** tables, keys, and
relationships representing product facts. **Rule:** begin with identity,
cardinality, lifecycle, access paths, and invariants; treat ORM mappings as one
client of the SQL design.

## “The index made writes slower but did not help the query”

**Example:** an index does not match the cart filter or ordering. **Term — query
plan:** the database’s chosen path for executing SQL. **Rule:** connect every
index to a named read and compare the plan while accounting for write/storage cost.

## “The empty migration passed but existing data failed”

**Example:** a required column cannot be added to legacy rows in one unsafe step.
**Term — migration:** a versioned schema/data change. **Rule:** test empty and
existing-data paths, interruption, restart, compatibility, and rollback or
roll-forward. Diagnose N+1 by query count and shape, not latency alone.

## “A repository only forwarded one call”

**Example:** a route and repository have identical signatures and no repeated
query or substitution need. **Term — earned boundary:** a layer introduced by
observed orchestration, invariants, duplication, or substitution. **Rule:** keep
simple route-to-SQLAlchemy code direct; the use case owns commit/rollback, and a
repository never commits independently.

### Tools earned here

- **PostgreSQL + Psycopg 3 + SQL:** use the explicit production database driver, enforce relational truth, and inspect behavior directly.
- **SQLAlchemy 2 typed mappings:** reduce mapping repetition while retaining visible sessions and queries.
- **Alembic:** version and test schema/data transitions; autogenerated output must be reviewed.
- **Docker Compose:** reproduce the database dependency, not simulate a deployment platform.
- **pytest integration fixtures:** isolate real database behavior and migration paths.

Use synchronous SQLAlchemy sessions/Psycopg first. FastAPI's async transport is not evidence for async database access; `AsyncSession` needs a representative before/after workload, pool/failure analysis, and complexity record showing that a simpler correction did not meet the target.

FastCRUD is optional only for repetitive commodity CRUD after handwritten fundamentals and a comparison showing it preserves constraints, transaction ownership, query shape, and API semantics. Remove it from invariant-heavy workflows or whenever hooks obscure those properties. Redis and extra databases remain out.

## Evaluate after evidence

Evaluate only optional tools after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M2

Open these when a model, query, or migration creates the question. Reviewed 2026-09-13.

- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — Which facts can the database reject for every writer? Applicable tool: PostgreSQL 17+.
- [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html) — Which access path justifies an index? Applicable tool: current PostgreSQL.
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) — How do tables, relationships, sessions, and SQL fit together? Applicable tool: SQLAlchemy 2.0.
- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) — How is schema history created, inspected, upgraded, and downgraded? Applicable tool: Alembic 1.19.

Do not substitute an ORM recipe for understanding the emitted SQL.
