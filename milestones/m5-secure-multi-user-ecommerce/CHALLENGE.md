# M5 challenge brief

Run from `projects/ecommerce/` and use only synthetic identities and secrets.

## **C1 — Broken identity**

**YOU BUILD** — implement the fixed browser's Core opaque cookie session after comparing it with JWT.

### Steps

1. Create `tests/m5/test_identity.py`; compare cookie sessions with JWT, then implement only the Core cookie path.
2. Test hashing, enumeration, fixation, CSRF policy, logout, and cookie rotation.
3. Run README Block 1; keep any isolated PyJWT implementation as conditional Stretch for a newly earned non-browser client.

### Hints

1. Separate “who is this?” from “may they do this?”
2. Inspect password verification, session rotation, cookie attributes, and configuration.
3. Use the FastAPI security and OWASP links in `RESOURCES.md`.

### Reset

Disable the test-only mutation, rotate only the synthetic secret, and run
`uv run --locked pytest tests/m5/test_identity.py -q`.

## **C2 — Role escalation**

**YOU BUILD** — activate escalation only inside an isolated test.

### Steps

1. Add Alice, Bob, staff, and admin cases to `tests/m5/test_authorization_matrix.py`.
2. Prove client-supplied role and a missing admin check fail before repair.
3. Centralize default-deny role policy and run README Block 2.

### Hints

1. Ask which trusted server fact should determine role.
2. Inspect authentication context, role-policy input, and default denial.
3. Use the OWASP authorization link in `RESOURCES.md`.

### Reset

Disable the role mutation and run
`uv run --locked pytest tests/m5/test_authorization_matrix.py -q`.

## **C3 — Object leak**

**PROVIDED** — Alice/Bob attack descriptions are supplied; you implement tests.

### Steps

1. Change IDs, list filters, and nested routes across synthetic users.
2. Record response and database state before repair.
3. Scope reads and writes, then rerun README Block 2.

### Hints

1. Ask which exact object and user scope every query needs.
2. Inspect predicates, nested identifiers, filters, and disclosure differences.
3. Use the object-authorization link in `RESOURCES.md`.

### Reset

Restore Alice/Bob fixtures with the bounded reset and run
`uv run --locked pytest tests/m5/test_authorization_matrix.py -q`.

## **C4 — Invalid lifecycle**

**PROVIDED** — the transition table fixes allowed and denied outcomes.

### Steps

1. Create `tests/m5/test_order_state.py` from every transition.
2. Repeat and race cancel/pay/fulfill and bypass one handler in a test.
3. Enforce state and authorization together; run README Block 3.

### Hints

1. Compare current state, command, actor, and expected unchanged rows.
2. Inspect state policy and database transaction together.
3. Use the state-machine link in `RESOURCES.md`.

### Reset

Reload synthetic orders with the bounded reset and run
`uv run --locked pytest tests/m5/test_order_state.py -q`.

Ship threat-model deltas and regression evidence, never real credentials.
