# Problems and mental models

An HTTP 202 or committed order creates an obligation. In-process tasks can vanish; atomically storing business state plus outbox intent closes the commit/publish gap. A queue records durable work; a worker claims it with a lease, performs it, and acknowledges outcome.

FastAPI `BackgroundTasks` runs in the API process and is therefore a best-effort convenience, not durable acceptance. A framework such as Taskiq supplies worker/broker abstractions but does not manufacture exactly-once behavior: durability depends on persisted intent, broker acknowledgement/failure semantics, retry state, idempotent effects, and operational recovery.

Crashes make at-least-once execution normal: the worker may repeat after the side effect but before acknowledgement. Idempotent consumers use stable semantic identity and recorded result so repetition converges; “exactly once” is not claimed across a database, broker, and external provider. Eventual consistency means accepted and completed states differ temporarily and must be visible to users/operators.

Bounded retries, backoff, poison quarantine, manual replay, retention, graceful shutdown, and backpressure are product behavior. Queue depth, oldest-ready age, processing duration, retry count, and terminal failure metrics show whether the obligation is being met.
