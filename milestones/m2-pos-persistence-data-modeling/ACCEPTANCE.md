# Acceptance gate

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
