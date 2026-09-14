# Resources for M7

Consult these after proving that accepted work can be lost or repeated. Reviewed 2026-09-14.

- [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) — What does in-process post-response work provide, and what does it not make durable? Applicable tool: current FastAPI.
- [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) — How can FOR UPDATE SKIP LOCKED coordinate competing workers? Applicable tool: current PostgreSQL.
- [Taskiq guide](https://taskiq-python.github.io/guide/) — When does an external broker/worker earn its operational cost? Applicable tool: current Taskiq.

Build and test the database-backed durable-intent path before adding Taskiq.
