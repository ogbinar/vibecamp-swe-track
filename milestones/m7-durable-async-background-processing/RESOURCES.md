# Resource guide

Use PostgreSQL primary docs for row locking/`SKIP LOCKED`/transactions/indexes, SQLAlchemy transaction docs, and official guidance for process shutdown and the metrics library chosen. If evaluating Taskiq/Redis, use current primary durability/acknowledgement documentation.

Reject “exactly once” claims without a failure model and queue examples that omit poison work, leases, replay, or retention. Reproduce crash boundaries; prose guarantees alone are insufficient.
