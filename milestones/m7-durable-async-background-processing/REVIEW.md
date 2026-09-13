# Review

Explain why accepted FastAPI `BackgroundTasks` work can vanish; how outbox closes the gap; at-least-once versus exactly-once; why Taskiq cannot erase the commit/broker/external-effect boundaries; idempotent consumer identity; lease expiry; eventual-consistency UX; and which metric catches stuck work first.

Self-review atomic insertion, double claims, clock source, retry storms, infinite poison loops, unsafe replay authorization, hidden jobs on shutdown, and retention growth. Predict each kill-point outcome before executing C1/C2.

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to decide how completed, failed, and quarantined payloads expire without destroying audit/recovery needs. If optional queue infrastructure is proposed, show whether the M4 revisit trigger actually fired.
