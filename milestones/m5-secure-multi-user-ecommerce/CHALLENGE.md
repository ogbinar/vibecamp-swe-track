# Challenge brief

- **C1 — Broken identity:** Seed plaintext/fast-hashed passwords, user enumeration, permissive JWT validation, expired/wrong-audience tokens, and a leaked signing secret. Repair hashing/JWT/configuration and prove safe failure.
- **C2 — Role escalation:** Seed an endpoint that trusts a client-supplied role and an admin route missing authorization. Centralize deny-by-default RBAC; test every role/action pair.
- **C3 — IDOR/object leak:** Change order/address IDs, list filters, and nested routes to cross user boundaries. Repair object-level authorization for reads and writes without revealing existence.
- **C4 — Invalid lifecycle:** Race/repeat cancel/pay/ship commands and bypass a handler. Enforce the order state machine and authorization together.

Operate by reviewing sanitized security logs and rotating a synthetic secret. Ship threat-model deltas and regression evidence, never real credentials.
