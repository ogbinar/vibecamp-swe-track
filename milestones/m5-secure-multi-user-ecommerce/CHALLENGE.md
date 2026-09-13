# Challenge brief

- **C1 — Broken identity:** Write a short client/trust-boundary comparison and select either an opaque secure-cookie session or JWT for the product. Seed plaintext/fast-hashed passwords and user enumeration; then inject mechanism-specific failures—session fixation/missing CSRF/invalid logout for cookies, or permissive algorithm/expired/wrong-audience claims and leaked signing secret for JWT. Repair `pwdlib[argon2]`, the selected session mechanism, and configuration. If cookies are selected, also complete a bounded isolated PyJWT validation lab covering the signed-claim attacks so required JWT competence is proven without shipping a second product session path.
- **C2 — Role escalation:** Seed an endpoint that trusts a client-supplied role and an admin route missing authorization. Centralize deny-by-default RBAC; test every role/action pair.
- **C3 — IDOR/object leak:** Change order/address IDs, list filters, and nested routes to cross user boundaries. Repair object-level authorization for reads and writes without revealing existence.
- **C4 — Invalid lifecycle:** Race/repeat cancel/pay/ship commands and bypass a handler. Enforce the order state machine and authorization together.

Operate by reviewing sanitized security logs and rotating a synthetic secret. Ship threat-model deltas and regression evidence, never real credentials.
