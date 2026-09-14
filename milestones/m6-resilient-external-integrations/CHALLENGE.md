# M6 challenge brief

Run from `projects/ecommerce/`. Keep provider data and credentials synthetic.

## **C1 — Unreliable provider**

**PROVIDED** — extend the deterministic provider fake with published modes.

### Steps

1. Create `tests/m6/test_provider.py` for payment/refund, latency, 429/503, malformed response, and before/after-effect timeout.
2. Classify each outcome and use `lookup` after uncertainty before adding timeout, backoff, jitter, or retry.
3. Run README Block 1 and preserve unknown outcomes for reconciliation.

### Hints

1. Ask whether failure is definite or the outcome is unknown.
2. Inspect timeout phase, operation identity, retry budget, and provider fact.
3. Use the HTTPX timeout link in `RESOURCES.md`.

### Reset

Rerun `uv run --locked pytest tests/test_failure_harnesses.py -q`; the fake is
in-memory and returns to its deterministic initial state.

## **C2 — Hostile webhook**

**YOU BUILD** — create synthetic signed fixtures from the matrix.

### Steps

1. Create `tests/m6/test_retry_webhook.py` for duplicate, replay, reorder, tamper, age, and wrong bytes/account.
2. Verify the raw body before parsing or applying an effect.
3. Deduplicate and apply order-aware transitions; run README Block 2.

### Hints

1. Compare the exact signed bytes, timestamp, event ID, and account.
2. Inspect verification order, durable event identity, and transition policy.
3. Use the webhook-security link in `RESOURCES.md`.

### Reset

Reload the synthetic fixture set and run
`uv run --locked pytest tests/m6/test_retry_webhook.py -q`.

## **C3 — Integration incident**

**YOU BUILD** — reconcile a fixed unknown operation against fake provider state.

### Steps

1. Create `tests/m6/test_reconciliation.py` and `scripts/reconcile_payment.py`.
2. Reconstruct attempts by correlation ID and choose one legal local transition.
3. Run README Block 3 twice and write a concise incident note.

### Hints

1. Start with provider fact, prior local state, and semantic operation ID.
2. Inspect idempotency record, correlation fields, and transition ownership.
3. Use the idempotency reference in `RESOURCES.md`.

### Reset

Restore the fixed `synthetic-unknown-1` fake state and rerun
`uv run --locked pytest tests/m6/test_reconciliation.py -q`.

Ship documented degraded behavior and residual provider risk.
