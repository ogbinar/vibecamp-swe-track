# Challenge brief

- **C1 — Unreliable provider:** Fake latency, timeout after side effect, 429/5xx, malformed response, and retry storms. Classify retryability, add bounded timeout/backoff/jitter, preserve unknown outcomes, and reconcile without duplicate charge/shipment.
- **C2 — Hostile webhook:** Replay, duplicate, reorder, tamper, age, and sign the wrong bytes. Verify before parsing side effects, deduplicate event handling, and make state transitions order-aware.
- **C3 — Integration incident:** Seed missing correlation IDs, leaked payload data, duplicate client requests, and provider outage. Reconstruct impact, repair idempotency/log structure, operate a recovery/reconciliation procedure, and write a concise postmortem.

Refactor only the tested external boundary. Ship documented degraded behavior and residual dependency risk.
