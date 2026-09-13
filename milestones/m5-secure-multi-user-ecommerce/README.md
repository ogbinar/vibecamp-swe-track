# M5 — Secure Multi-user Ecommerce

[Course home](../../README.md) / M5

**Milestone 6 of 11 · M5**

## Why

Once several people use the product, knowing who sent a request is not enough.
Every action must also be allowed for that person and that specific object.

## Starting checkpoint

- **At a glance:** Secure · Ecommerce.
- **You will leave with:** Session and role/object matrix; Order-state attack regressions and threat record.
- **Gate:** [A1–A6 / B + contextual C](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/ecommerce/README.md#ecommerce-launch-kit-for-m5), then return to the saved block; first visit: [Block 1](#1-establish-identity-safely-required).

Start in `projects/ecommerce/`. Run its documented checks. Expected: anonymous
health works and identity routes are absent. Do not copy credentials or POS
business logic into this new product.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Authentication:** establishing who is making the request.
- **Authorization:** deciding whether that identity may perform the action.
- **RBAC:** role-based access control grants broad permissions by role.
- **Object authorization:** checking access to this particular cart, address, or order.
- **JWT:** JSON Web Token, a signed claim container—not a universal session default.

## Product brief

Read the [product and threat brief](../../projects/ecommerce/REQUIREMENTS.md) and
[security contract](../../projects/ecommerce/specs/M5-SECURITY-CONTRACT.md).
Build registration/login, customer/staff/admin roles, carts, addresses, orders,
and an order state machine. Start with the attack descriptions in
`projects/ecommerce/fixtures/`. Compare secure cookie sessions with JWT for the
actual client. Complete C1–C4 in [CHALLENGE.md](CHALLENGE.md#m5-challenge-brief), including password
hashing, enumeration, cross-user object access, and invalid state transitions.

External payments wait until M6. Never log passwords, tokens, reset secrets, or
personal data.

## Work blocks

### 1. Establish identity safely `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/ecommerce/`;
focus on `tests/m5/test_identity.py` and the output named below. Record `evidence/M5/identity.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 1](#1-establish-identity-safely-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--broken-identity) and [concept explanation](CONCEPTS.md#the-password-database-leaked). [Tool boundaries](TOOLS.md#tools-earned-here) apply to this product.

**Supplied:** PostgreSQL shell and the [security contract](../../projects/ecommerce/specs/M5-SECURITY-CONTRACT.md).
**You build:** user model, Argon2 password hashing, generic registration/login/
recovery responses, and opaque cookie sessions in `projects/ecommerce/`. Run
focused API tests; observe cookie rotation and no identity enumeration. Record
`evidence/M5/identity.md`. Stop after login/logout/recovery are green.

### 2. Enforce role and object policy `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m5/test_authorization_matrix.py` and the output named below. Record `evidence/M5/authorization.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-enforce-role-and-object-policy-required) using that saved result; continue to Block 3.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--role-escalation) and [concept explanation](CONCEPTS.md#alice-guessed-bobs-order-id). Also use [C3 object-scope attacks](CHALLENGE.md#c3--object-leak).

Implement the role and ownership matrices for Alice, Bob, staff, and admin.
Run each negative test alone before the full suite; observe denial without
object disclosure or mutation. Record `evidence/M5/authorization.md`. If a test
passes unexpectedly, disable the test-only mutation and inspect scope first.

### 3. Protect the order lifecycle `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/ecommerce/`;
focus on `tests/m5/test_order_state.py` and the output named below. Record `evidence/M5/state-and-threats.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-protect-the-order-lifecycle-required) using that saved result; continue to [Evidence](#evidence).
When needed: [C4 scenario and hints](CHALLENGE.md#c4--invalid-lifecycle) and [concept explanation](CONCEPTS.md#a-permitted-user-forced-an-impossible-order-state).

Implement the published state table and attack invalid transitions. Run the
state tests and secret scan; observe unchanged rows after denial. Record
`evidence/M5/state-and-threats.md`. Stop when all C1–C4 attacks have a focused
regression test. JWT implementation remains Stretch.

### Literal command map

Run from `projects/ecommerce/`; create each named learner test before expecting green.

Before: the learner test is absent or its synthetic attack succeeds. After: the
row’s stop condition is green with unchanged protected state.

| Block | Learner target | Copyable command | Expected stop condition |
|---|---|---|---|
| 1 | `tests/m5/test_identity.py` | `ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_identity.py -q` | Login, logout, recovery, cookie rotation, and generic responses pass. |
| 2 | `tests/m5/test_authorization_matrix.py` | `ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_authorization_matrix.py -q` | Every role/object denial preserves state and reveals no object existence. |
| 3 | `tests/m5/test_order_state.py` | `ECOMMERCE_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5433/vibecamp_ecommerce uv run --locked pytest tests/m5/test_order_state.py -q` | Allowed transitions pass and every denial preserves rows. |

An absent target is the create-it signal. Recover with the ecommerce bounded
reset and one synthetic identity; record the next action before pausing.

Pause: record the active synthetic actor, failing policy case, and next test.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A6](ACCEPTANCE.md#core) with an authorization matrix, attack-focused API
tests, threat model, secret scan, and redacted logs.

## Done when

Every identity, role, object, and lifecycle attack has a focused regression test
and all Core checks pass. Tag `m5-secure-ecommerce`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m5) only for the question left by the active hint ladder.

Run one attack test, inspect the policy decision and object scope, then use the
hint ladder and [RESOURCES.md](RESOURCES.md#resources-for-m5). Rotate only synthetic secrets.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M6](../m6-resilient-external-integrations/README.md).

[Previous milestone: M4](../m4-maintainability-testing-refactoring/README.md) · [Course home](../../README.md) · [Next milestone: M6](../m6-resilient-external-integrations/README.md)
