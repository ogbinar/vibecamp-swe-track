# Resources for M2

Open these when a model, query, or migration creates the question. Reviewed 2026-09-13.

- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — Which facts can the database reject for every writer? Applicable tool: PostgreSQL 17+.
- [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html) — Which access path justifies an index? Applicable tool: current PostgreSQL.
- [SQLAlchemy Unified Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) — How do tables, relationships, sessions, and SQL fit together? Applicable tool: SQLAlchemy 2.0.
- [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html) — How is schema history created, inspected, upgraded, and downgraded? Applicable tool: Alembic 1.19.

Do not substitute an ORM recipe for understanding the emitted SQL.
