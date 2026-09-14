# Tools earned here

- **PostgreSQL outbox/job tables:** atomic intent and inspectable baseline queue semantics.
- **Polling worker + database locking/leases:** expose claim, timeout, retry, and crash behavior directly.
- **Alembic:** deploy job state and indexes safely.
- **Metrics/structured logs:** queue health and per-job history/correlation.
- **Provider fakes:** deterministic pre/post-side-effect crashes.

Taskiq is optional only after Core. Select and document the production broker, acknowledgement/redelivery and result policy, shutdown behavior, retention, monitoring, and local recovery; compare how it preserves atomic intent, at-least-once behavior, replay, and operations. Redis is not required and may not replace PostgreSQL as business truth. Avoid FastAPI `BackgroundTasks` for every accepted durable obligation.

Revisit the M4 [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md) if Taskiq or Redis is proposed. Adopt only when its measurable trigger is now true; otherwise update the evidence and keep the simpler queue.

An email provider is optional after Core. Retain it only for a named delivery
question with an owner, test recipient, credential/data boundary, cost cap, and
removal trigger. API acceptance is not mailbox delivery.
