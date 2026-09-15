# M5 — Protect customer accounts and orders

[Course home](../../README.md) / M5

**Milestone 6 of 11 · M5**

## Business problem

Once several people use the product, knowing who sent a request is not enough.
Every action must also be allowed for that person and that specific object.

## Product objective

- **Product can:** a first-party browser can sign in and access only its authorized orders through a secure cookie session.
- **You will prove:** identity, role, ownership, state, and negative security tests.

Read the [product and threat brief](../../projects/ecommerce/REQUIREMENTS.md) and
[security contract](../../projects/ecommerce/specs/M5-SECURITY-CONTRACT.md).
Build registration/login, customer/staff/admin roles, carts, addresses, orders,
and an order state machine. Start with the attack descriptions in
`projects/ecommerce/fixtures/`. Compare secure cookie sessions with JWT for the
actual client. Complete C1–C4 in the [challenge brief](#challenge-brief), including password
hashing, enumeration, cross-user object access, and invalid state transitions.

External payments wait until M6. Never log passwords, tokens, reset secrets, or
personal data.

## Start here

- **Gate:** [A1–A6 / B + contextual C](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/ecommerce/README.md#ecommerce-launch-kit-for-m5), then return to the saved block; first visit: [Block 1](#1-establish-identity-safely-required).

Start in `projects/ecommerce/`. Run its documented checks. Expected: anonymous
health works and identity routes are absent. Do not copy credentials or POS
business logic into this new product.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Establish identity safely `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/ecommerce/`;
focus on the supplied `contracts/test_m5_security_contract.py`, then create
`tests/m5/test_identity.py`. Use the [C1 scenario and hints](#c1--broken-identity),
[password example](#the-password-database-leaked), and
[tool boundaries](#tools-earned-here) only when the concrete failure
raises that question. Run the supplied contract first; its missing-route
failures are the intended red behavior, while a missing learner test is only a
setup signal. Record the learner check in `evidence/M5/identity.md`. If it fails,
follow C1 recovery and rerun the narrow check without resetting unrelated state.
Stop when this block's listed command passes and its
evidence is saved. Resume at [Block 1](#1-establish-identity-safely-required)
using that saved result; continue to Block 2.

**Supplied:** PostgreSQL shell and the [security contract](../../projects/ecommerce/specs/M5-SECURITY-CONTRACT.md).
**You build:** user model, Argon2 password hashing, generic registration/login/
recovery responses, and opaque cookie sessions in `projects/ecommerce/`. Run
`uv run --locked pytest contracts/test_m5_security_contract.py -q` once to
observe the supplied red contract, then run focused learner API tests; observe
cookie rotation and no identity enumeration. Record
`evidence/M5/identity.md`. Stop after login/logout/recovery are green.

Run from the stated project directory:

```bash
ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_identity.py -q
```

### 2. Enforce role and object policy `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m5/test_authorization_matrix.py` and the output named below. Record `evidence/M5/authorization.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-enforce-role-and-object-policy-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](#c2--role-escalation) and [concept explanation](#alice-guessed-bobs-order-id). Also use [C3 object-scope attacks](#c3--object-leak).

Implement the role and ownership matrices for Alice, Bob, staff, and admin.
Run each negative test alone before the full suite; observe denial without
object disclosure or mutation. Record `evidence/M5/authorization.md`. If a test
passes unexpectedly, disable the test-only mutation and inspect scope first.

Run from the stated project directory:

```bash
ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_authorization_matrix.py -q
```

### 3. Protect the order lifecycle `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m5/test_order_state.py` and the output named below. Record `evidence/M5/state-and-threats.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-protect-the-order-lifecycle-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C4 scenario and hints](#c4--invalid-lifecycle) and [concept explanation](#a-permitted-user-forced-an-impossible-order-state).

Implement the published state table and attack invalid transitions. Run the
state tests and secret scan; observe unchanged rows after denial. Record
`evidence/M5/state-and-threats.md`. Stop when all C1–C4 attacks have a focused
regression test. JWT implementation remains Stretch.

Run from the stated project directory:

```bash
ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_order_state.py -q
```

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Authentication:** establishing who is making the request.
- **Authorization:** deciding whether that identity may perform the action.
- **RBAC:** role-based access control grants broad permissions by role.
- **Object authorization:** checking access to this particular cart, address, or order.
- **JWT:** JSON Web Token, a signed claim container—not a universal session default.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A6](#core) with an authorization matrix, attack-focused API
tests, threat model, secret scan, and redacted logs.

## Done / next

Every identity, role, object, and lifecycle attack has a focused regression test
and all Core checks pass. Tag `m5-secure-ecommerce`.

### Recovery

Use [targeted references](#resources-for-m5) only for the question left by the active hint ladder.

Run one attack test, inspect the policy decision and object scope, then use the
hint ladder and [reference](#resources-for-m5). Rotate only synthetic secrets.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M6](../m6-resilient-external-integrations/README.md).

[Previous milestone: M4](../m4-maintainability-testing-refactoring/README.md) · [Course home](../../README.md) · [Next milestone: M6](../m6-resilient-external-integrations/README.md)


---

## Challenge brief

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
3. Use the FastAPI security and OWASP links in the Reference section below.

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
3. Use the OWASP authorization link in the Reference section below.

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
3. Use the object-authorization link in the Reference section below.

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
3. Use the state-machine link in the Reference section below.

### Reset

Reload synthetic orders with the bounded reset and run
`uv run --locked pytest tests/m5/test_order_state.py -q`.

Ship threat-model deltas and regression evidence, never real credentials.


---

## Acceptance gate

Required maturity: **Level B plus contextual Level C security controls**.

## Core

- **A1:**
  - [ ] C1 evidence compares opaque secure-cookie sessions with JWT against the declared client/trust boundary and justifies one product choice.
  - [ ] Tests prove `pwdlib[argon2]` hashing/upgrade, bounded login behavior, no user enumeration, and no secrets in source/logs/evidence.
  - [ ] Cookie choice additionally proves `Secure`/`HttpOnly`/`SameSite`, fixation rotation, CSRF defense, expiry, and logout/revocation.
  - [ ] A short JWT comparison explains algorithm allowlist, issuer, audience, time, token type, rotation/revocation, and theft behavior.
  - [ ] JWT implementation tests are Stretch for the declared first-party browser; Core does not implement both session systems.
- **A2:**
  - [ ] A deny-by-default RBAC matrix covers customer/staff/admin and C2 escalation attempts across every privileged route.
- **A3:**
  - [ ] Two-user API tests cover every owned resource/list/nested/write path
  - [ ] all C3 object-level authorization attacks fail without cross-user disclosure or mutation.
- **A4:**
  - [ ] Order state-machine tests cover allowed, forbidden, repeated, and bypass transitions together with required permissions
  - [ ] C4 prior state remains intact.
- **A5:**
  - [ ] Threat model names assets, actors, trust boundaries, abuse cases, mitigations, residual risks
  - [ ] clean unit/integration/API/migration/lint/validator commands pass.
- **A6:**
  - [ ] A [data-lifecycle review](../../templates/DATA-LIFECYCLE.md) traces password-derived data and session identifiers/claims.
  - [ ] It traces addresses and order ownership through stores, logs, retention, and deletion.
  - [ ] Access behavior has tests or explicit justified deferrals.

## Execution map

Each checklist bullet is a local step in order. From `projects/ecommerce/`, use
README Block 1 for A1, Block 2 for A2–A3, and Block 3 for A4. For A5 run
`uv run --locked ruff check . && uv run --locked mypy && uv run --locked pytest`;
for A6 run `test -s evidence/M5/data-lifecycle.md`. Record results under matching
A headings; recover with the bounded ecommerce reset and synthetic fixtures.

## Stretch

Add refresh-token rotation/revocation or rate limiting only with explicit threat/UX requirements and replay/lockout tests.

## Review

### Review

Answer one question at a time in `evidence/M5/index.md`:

1. How is authentication different from authorization?
2. Which decision belongs to a role, and which belongs to object ownership?
3. How is an old password hash upgraded?
4. Why does the first-party browser earn an opaque cookie session for Core?
5. What does that cookie/session design not guarantee?
6. Where is identity established, rotated, expired, and revoked?
7. How do permission and order state combine for one command?
8. Do ID, list, and nested routes deny Alice access to Bob's object without disclosure?
9. Which cookie, Cross-Site Request Forgery (CSRF), log, and secret checks pass?
10. What residual threat remains?

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to find copies that authentication tests alone miss: logs, session records or token claims, order snapshots, and retained audit/security records.


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M5 concepts through access mistakes

## “Alice guessed Bob’s order ID”

**Example:** Alice is logged in but reads an object she does not own. **Term —
object-level authorization:** checking permission for this specific object.
**Rule:** scope reads, lists, writes, and nested identifiers; login alone is not
authorization.

## “The password database leaked”

**Example:** reversible encryption reveals every password. **Term — password
hashing:** one-way, salted password verification. **Rule:** use Argon2 through
`pwdlib`, bound input, and never log credentials.

## “A staff role was trusted from request JSON”

**Example:** a client sends `role=admin`. **Term — role-based access control
(RBAC):** broad permissions assigned from trusted server-side roles. **Rule:**
deny by default and combine role permission with object scope on every path.

## “The browser session worked, but cross-site requests could use it”

**Example:** cookies are sent automatically with a forged request. **Term —
cross-site request forgery (CSRF):** another site triggers an authenticated browser
request. **Rule:** choose authentication from the client/trust boundary and test
cookie attributes, CSRF defense, fixation, expiry, logout, theft, and revocation.

## “A token was decoded but not safely validated”

**Example:** a JSON Web Token (JWT) accepts the wrong audience or algorithm.
**Term — signed claim:** data whose integrity is verifiable but not encrypted.
**Rule:** when JWT is justified, use PyJWT with a fixed algorithm, issuer,
audience, time, type, and rotation/revocation policy; keep payloads nonsensitive.

## “A permitted user forced an impossible order state”

**Example:** an owner pays an already cancelled order. **Term — state machine:**
the allowed states and transitions. **Rule:** enforce authorization and transition
policy together, return nonrevealing errors, protect secrets, and log safely.

### Tools earned here

- **`pwdlib[argon2]`:** adaptive password hashing, verification, and upgrade; never invent cryptography.
- **Server-side opaque session plus secure cookie (Core):** the declared client is a first-party browser. Prove CSRF/session fixation/rotation/logout behavior.
- **PyJWT (Stretch comparison):** consider bearer tokens only if a different client/trust boundary is later earned; require short-lived claims, fixed-algorithm validation, issuer/audience/time/type checks, and explicit refresh/revocation behavior.
- **FastAPI security/dependency boundaries:** authenticate once, authorize per action/object.
- **pytest/HTTPX security matrix:** prove negative paths at the API boundary.
- **`pydantic-settings`/CI secrets:** keep secret values outside source and output.

No OAuth server, external identity platform, payment SDK, WAF, or broad security scanner is required. Core compares the mechanisms but implements only the cookie session. Earn JWT or refresh tokens only from a new client requirement and document revocation/theft behavior.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M5

Read after an attack case fails, not as a security-themed tutorial dump. Reviewed 2026-09-14.

- [FastAPI security tools](https://fastapi.tiangolo.com/reference/security/) — Which framework helper follows, rather than defines, the authentication decision? Applicable tool: current FastAPI.
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — What must be checked beyond “the user is logged in”? Applicable guidance: current OWASP Cheat Sheet Series.
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html) — Which password-storage properties and parameters matter? Applicable guidance: current OWASP Cheat Sheet Series.
- [PyJWT usage](https://pyjwt.readthedocs.io/en/stable/usage.html) — Stretch only: which claims and algorithms must decoding verify explicitly? Applicable tool: PyJWT 2.

Examples are starting points; the milestone threat cases decide the policy.
