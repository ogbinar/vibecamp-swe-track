# Acceptance gate

Required maturity: **Level B** for the persistent POS slice.

## Core

- **A1:** ER rationale and executable SQL cover relationships; Psycopg 3 connects SQLAlchemy to PostgreSQL; PostgreSQL integration tests—not SQLite substitutes—prove unique, FK, nullability, and value constraints plus API/application error translation for C1.
- **A2:** Indexes map to named access paths with before/after plan or timing evidence; query count is bounded and a seeded N+1/duplicated-access regression fails an automated guard.
- **A3:** `alembic upgrade head` works on empty and prior-revision fixtures; interrupted/invalid backfill C3 is recovered and rerun without data loss; Compose persistence/reset behavior is proven.
- **A4:** Request/use-case session scope is explicit; induced flush error rolls back and leaves later work usable; synchronous session behavior is the documented baseline, and any async proposal includes representative before/after evidence plus pool/failure/complexity analysis; M2 API, PostgreSQL integration, migration, Ruff, mypy, and validator commands pass cleanly.
- **A5:** A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces one product/inventory field through source, relational store, derived values, access, retention/deletion, and backup implications, with evidence or a precise later-milestone deferral.

Evidence includes schema revision, SQL/commands, expected/actual rows, and interpretation.

## Stretch

Compare FastCRUD or a pagination adapter against explicit behavior. Retain it only if Core stays legible and fully tested.
