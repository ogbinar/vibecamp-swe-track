# Resources for M10

Use these to answer a capstone operational question, not to expand the stack. Reviewed 2026-09-13.

- [PostgreSQL row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) — When could database policy reinforce tenant isolation? Applicable tool: current PostgreSQL.
- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) — What is backed up, restored, and actually tested? Applicable tool: current PostgreSQL.
- [Alembic cookbook](https://alembic.sqlalchemy.org/en/latest/cookbook.html) — How can migration deployment address real operational cases? Applicable tool: Alembic 1.19.
- [GitHub deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — Where do approvals, secrets, and deployment history belong? Applicable platform: GitHub Actions.
- [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/) — How do traces and metrics answer declared operational questions? Applicable tool: current OpenTelemetry Python.

Managed tools such as Logfire or Sentry are optional adapters after telemetry questions are explicit.
