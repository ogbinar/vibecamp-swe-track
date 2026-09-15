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
actual client. Complete C1–C4 in [CHALLENGE.md](CHALLENGE.md#m5-challenge-brief), including password
hashing, enumeration, cross-user object access, and invalid state transitions.

External payments wait until M6. Never log passwords, tokens, reset secrets, or
personal data.

## Start here

- **Gate:** [A1–A6 / B + contextual C](ACCEPTANCE.md#core).
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
`tests/m5/test_identity.py`. Use the [C1 scenario and hints](CHALLENGE.md#c1--broken-identity),
[password example](REFERENCE.md#the-password-database-leaked), and
[tool boundaries](REFERENCE.md#tools-earned-here) only when the concrete failure
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
When needed: [C2 scenario and hints](CHALLENGE.md#c2--role-escalation) and [concept explanation](REFERENCE.md#alice-guessed-bobs-order-id). Also use [C3 object-scope attacks](CHALLENGE.md#c3--object-leak).

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
When needed: [C4 scenario and hints](CHALLENGE.md#c4--invalid-lifecycle) and [concept explanation](REFERENCE.md#a-permitted-user-forced-an-impossible-order-state).

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

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A6](ACCEPTANCE.md#core) with an authorization matrix, attack-focused API
tests, threat model, secret scan, and redacted logs.

## Done / next

Every identity, role, object, and lifecycle attack has a focused regression test
and all Core checks pass. Tag `m5-secure-ecommerce`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m5) only for the question left by the active hint ladder.

Run one attack test, inspect the policy decision and object scope, then use the
hint ladder and [REFERENCE.md](REFERENCE.md#resources-for-m5). Rotate only synthetic secrets.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M6](../m6-resilient-external-integrations/README.md).

[Previous milestone: M4](../m4-maintainability-testing-refactoring/README.md) · [Course home](../../README.md) · [Next milestone: M6](../m6-resilient-external-integrations/README.md)
