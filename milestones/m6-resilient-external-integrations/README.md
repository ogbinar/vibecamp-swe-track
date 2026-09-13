# M6 — Resilient External Integrations

**Capability:** bound and reconcile uncertain outcomes across network boundaries. **Deliverable:** extend ecommerce with payment and shipping adapters plus signed inbound webhooks, keeping external effects behind tested ports.

Prerequisite: M5 identity/state rules. Sequence: specify failure semantics → build controllable adapters → impose timeouts/retry budget → add idempotency/reconciliation → attack webhooks → diagnose an incident with correlated logs → ship `m6-resilient-integrations`.

Outputs: integration contracts, state transitions, retry/idempotency policy, webhook verification, fakes, reconciliation path, operational signals, and incident/postmortem evidence.
