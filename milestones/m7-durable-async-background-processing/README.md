# M7 — Durable Async / Background Processing

**Capability:** ensure accepted work survives process death and replay. **Deliverable:** extend ecommerce with atomic fulfillment intent, a PostgreSQL-backed outbox/job queue, and independently runnable worker from the same modular monolith.

Prerequisite: M6 idempotency/integration semantics. Sequence: demonstrate lost in-process work → persist intent with business state → claim/process/ack jobs → kill at each boundary → make consumers idempotent → quarantine/replay poison work → operate backlog → ship `m7-durable-async`.

Outputs: schema/migration, worker, leases/retries/quarantine, observable eventual consistency, recovery runbook, and crash/replay evidence. Exactly-once is not promised.
