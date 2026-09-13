# Resources for M8

Use these after the supplied barrier reproduces the final-seat race. Reviewed 2026-09-13.

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) — Why can two individually valid requests conflict? Applicable tool: current PostgreSQL.
- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — Which row, table, or advisory lock matches the protected resource? Applicable tool: current PostgreSQL.
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — Can the database reject the invalid final state regardless of writer? Applicable tool: current PostgreSQL.

Choose from measured interleavings; do not reach for a distributed lock by default.
