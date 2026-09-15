# M7 challenge brief

Run from `projects/ecommerce/`. Preserve job attempts and use injected time.

## **C1 — Lost accepted work**

**PROVIDED** — the kill window is supplied; bridge durable intent to PostgreSQL.

### Steps

1. Create the `accepted_intent` case in `tests/m7/test_worker.py`.
2. Kill the API after the business commit and observe missing in-process work.
3. Store business state and outbox intent atomically; run README Block 1.

### Hints

1. Compare acknowledged response, committed business row, and durable intent.
2. Inspect the business transaction and commit/publish gap.
3. Use the transactional-outbox link in `REFERENCE.md`.

### Reset

Disable the kill hook and run
`uv run --locked pytest tests/m7/test_worker.py -q -k accepted_intent`.

## **C2 — Duplicate execution**

**PROVIDED** — naive replay is supplied; you build the idempotent consumer.

### Steps

1. Add one-worker, competing-worker, lease-expiry, and after-effect cases.
2. Kill after effect but before acknowledgement and record every attempt.
3. Add stable semantic identity and run README Block 2.

### Hints

1. Separate durable intent, claim, external effect, and acknowledgement.
2. Inspect lease expiry, attempt history, idempotency key, and stored result.
3. Use the at-least-once link in `REFERENCE.md`; do not claim exactly once.

### Reset

Stop workers, advance only the injected synthetic clock, and rerun one selector
with `uv run --locked pytest tests/m7/test_worker.py -q -k lease_expiry`.

## **C3 — Poison and backlog incident**

**YOU BUILD** — create bounded poison input and authorized replay.

### Steps

1. Add the poison case and exhaust the fixed retry budget.
2. Quarantine without blocking healthy work; expose backlog and oldest-job age.
3. Preview and confirm one bounded replay using README Block 3.

### Hints

1. Ask whether one bad item blocks unrelated ready work.
2. Inspect retry count, next-attempt time, terminal state, actor, and audit entry.
3. Use the worker-operations link in `REFERENCE.md`.

### Reset

Use preview first; restore only the synthetic poison job, then run
`uv run --locked pytest tests/m7/test_worker.py -q -k poison`.

Ship API and worker as one codebase with separate processes.
