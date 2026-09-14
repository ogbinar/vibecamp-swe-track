# M7 concepts through lost and repeated work

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
