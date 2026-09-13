# Tools earned here

- **PostgreSQL outbox/job tables:** atomic intent and inspectable baseline queue semantics.
- **Polling worker + database locking/leases:** expose claim, timeout, retry, and crash behavior directly.
- **Alembic:** deploy job state and indexes safely.
- **Metrics/structured logs:** queue health and per-job history/correlation.
- **Provider fakes:** deterministic pre/post-side-effect crashes.

Taskiq is optional only after Core; compare how it preserves atomic intent, at-least-once behavior, replay, and local operations. Redis is not required. Avoid in-process FastAPI background tasks for accepted durable obligations.

Revisit the M4 [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md) if Taskiq or Redis is proposed. Adopt only when its measurable trigger is now true; otherwise update the evidence and keep the simpler queue.
