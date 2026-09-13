# M7 durable-work contract

Job states are pending, leased, succeeded, retryable, and dead-lettered. Outbox
records are pending, published, or cancelled. Store business change and outbox
intent in one database transaction. Delivery is at least once, so consumers
must record a stable message ID before applying a repeatable effect.

Create extension points for an outbox repository, worker handler, injected
clock, injected identifier source, and kill hook. Do not implement durable
semantics in the starter. Required commands must demonstrate one worker,
competing workers, process death after effect/before acknowledgement, lease
expiry, duplicate delivery, and authorized replay.

Replay requires actor, reason, bounded message IDs, preview, confirmation, and
an audit record. Expected result after every scenario: one business effect,
observable attempt history, and no permanently stuck lease.
