# M5 — Secure Multi-user Ecommerce

**Capability:** establish identity and enforce permissions over multi-user resources. **Deliverable:** create `projects/ecommerce/` with registration/login, customer/staff/admin roles, carts/orders/addresses, and an explicit order state machine.

Prerequisite: M4 boundary/test competence. Sequence: threat-model user stories → build identity → enforce coarse and object permissions → seed security mistakes → repair/test matrix → inspect secrets/audit-safe logs → ship `m5-secure-ecommerce`.

Outputs: password/JWT policy, RBAC and object-authorization matrices, state-transition rules, attack-focused API tests, and a concise threat model. External payment calls wait until M6.
