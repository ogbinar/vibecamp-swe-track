# M7 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M7 concepts through lost and repeated work

## “The API accepted work, then died”

**Example:** an in-process callback never runs. **Term — durable intent:** a
committed record that work is owed. **Rule:** store business state and outbox
intent atomically before acknowledging acceptance.

## “The worker sent the email twice”

**Example:** it dies after the effect but before acknowledgement. **Term —
at-least-once execution:** the job may run again. **Rule:** use stable semantic
identity so repetition produces one business effect.

## “The order committed but its job did not”

**Example:** the process dies between database commit and queue publication.
**Term — transactional outbox:** durable work intent stored with the business
change. **Rule:** persist both atomically before acknowledging the obligation.

## “BackgroundTasks disappeared on restart”

**Example:** process-local work dies with the API. **Term — best-effort work:**
work whose loss is acceptable. **Rule:** use FastAPI `BackgroundTasks` only for
that case; a worker framework does not itself create durability or exactly-once behavior.

## “The worker repeated an external effect”

**Example:** it crashes after sending but before acknowledging. **Term —
idempotent consumer:** repeated delivery converges to one business effect.
**Rule:** use stable semantic identity and stored results; expose accepted versus
completed states as eventual consistency.

For optional email, provider acceptance means only that the provider accepted
the request. It does not prove mailbox receipt, display, or reading. State the
deduplication window and remaining duplicate risk; never claim exactly-once
external delivery.

## “One poison job stopped healthy work”

**Example:** the same invalid item consumes every retry slot. **Term — quarantine:**
a terminal holding area for failed work. **Rule:** bound retries, isolate poison,
audit replay, shut down gracefully, and monitor depth, oldest age, duration, and failures.

### Tools earned here

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

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M7

Consult these after proving that accepted work can be lost or repeated. Reviewed 2026-09-14.

- [FastAPI background tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/) — What does in-process post-response work provide, and what does it not make durable? Applicable tool: current FastAPI.
- [PostgreSQL SELECT](https://www.postgresql.org/docs/current/sql-select.html) — How can FOR UPDATE SKIP LOCKED coordinate competing workers? Applicable tool: current PostgreSQL.
- [Taskiq guide](https://taskiq-python.github.io/guide/) — When does an external broker/worker earn its operational cost? Applicable tool: current Taskiq.

Build and test the database-backed durable-intent path before adding Taskiq.
