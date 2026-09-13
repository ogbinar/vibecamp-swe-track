# Resources for M3

Use these after reproducing partial writes or conflicting checkouts. Reviewed 2026-09-13.

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — What can concurrent transactions observe? Applicable tool: current PostgreSQL.
- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — Which lock protects the invariant, and what can it block? Applicable tool: current PostgreSQL.
- [SQLAlchemy transactions](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html) — Where should commit and rollback boundaries live? Applicable tool: SQLAlchemy 2.0.

Read database behavior first; an ORM cannot strengthen an invariant by itself.
