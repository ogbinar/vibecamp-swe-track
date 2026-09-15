# M1 — Make the catalog predictable for clients

[Course home](../../README.md) / M1

**Milestone 2 of 11 · M1**

## Business problem

The M0 catalog can answer two requests, but it cannot yet behave predictably for
a real client. In M1 you turn unclear product requests into an explicit HTTP
contract: which requests are valid, what each response means, and what happens
when a client retries or makes a mistake.

An **HTTP contract** is the public agreement formed by methods, paths, status
codes, headers, and response bodies. **Idempotent** means repeating the same
request has the same intended effect as sending it once. Review either term in
the [glossary](../../GLOSSARY.md) when it first becomes relevant.

## Product objective

- **Product can:** validate a browser product draft and expose a predictable JSON contract for clients.
- **You will prove:** the request matrix, invalid-form/API behavior, and compatibility-change evidence.

## Start here

- **Gate:** [A1–A4 / A + selected B](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/catalog/README.md#run-the-green-baseline), then return to the saved block; first visit: [Block 1](#1-describe-client-behavior-before-routes-required).

Start from your reviewed `m0-engineering-baseline` tag. Confirm the eight tests
still pass before changing code. Evolve `projects/catalog/`; do not create a
second catalog or copy a finished solution.

You will add in-memory create, retrieve, list, update, and retire behavior with
stable validation, errors, and pagination. The result is production-minded at
the API boundary, not production-ready: data still disappears on restart, and
security, deployment, and recovery are intentionally absent.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Describe client behavior before routes `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/catalog/`;
focus on `evidence/M1/` and the output named below. Record `evidence/M1/index.md`.
Stop when the request matrix is recorded.
Resume at [Block 1](#1-describe-client-behavior-before-routes-required) using that saved result; continue to Block 2.
When needed: [client response explanation](REFERENCE.md#the-client-cannot-predict-the-response). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

Read the [supplied product brief](../../projects/catalog/specs/M1-PRODUCT-BRIEF.md)
and [REFERENCE.md](REFERENCE.md#m1-concepts-through-client-problems). Copy its request matrix into your evidence and
record any remaining ambiguity in the milestone issue. The brief fixes public
behavior while leaving internal design to you. Then run `test -s evidence/M1/request-matrix.md`.

Expected: another person can predict the method, path, status, headers, and JSON
shape without reading your Python. If two examples conflict, resolve the
requirement before implementation.

### 2. Build the smallest contract `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/catalog/`;
focus on `evidence/M1/` and the output named below. Record `evidence/M1/index.md`.
Stop when the public contract passes.
Resume at [Block 2](#2-build-the-smallest-contract-required) using that saved result; continue to Block 3.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--the-client-contract-is-missing) and [concept explanation](REFERENCE.md#a-repeat-request-created-another-effect).

Use the [tool boundaries](REFERENCE.md#tools-earned-here). Keep state in memory so HTTP behavior is
the only new problem. Use separate Pydantic models when create, update, and read
operations accept different fields. Use `Decimal` for money.

Expected: valid examples work, invalid input produces a deliberate client error,
and unknown mistakes do not leak a traceback in the response.

From `projects/catalog/`, expose the missing behavior:

```bash
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected initially: HTTP 404 failures. That is the starting signal, not a broken
setup. Implement one behavior at a time and rerun the narrow test. If M0 tests
fail, repair the regression before continuing.

### 3. Diagnose contract failures `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/catalog/`;
focus on `tests/test_api.py` and the output named below. Record `evidence/M1/index.md`.
Stop when C1–C2 regressions pass after reset.
Resume at [Block 3](#3-diagnose-contract-failures-required) using that saved result; continue to Block 4.
When needed: [C2 scenario and hints](CHALLENGE.md#c2--invalid-input-must-not-corrupt-valid-state) and [concept explanation](REFERENCE.md#generated-documentation-hid-a-breaking-change).

Complete C1 and C2 in [CHALLENGE.md](CHALLENGE.md#m1-challenges-and-hints). Test rules in isolation only
when that makes the failure clearer; use HTTPX API tests for routing,
serialization, status codes, and error bodies. Use the supplied semantic OpenAPI
check, which detects a renamed or removed public field. Extend it only when you
add a new required public field.

Expected: each deliberate defect fails a specific test before repair and the
full M0/M1 suite returns to green afterward. Run
`PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py tests/test_api.py -q`.

### 4. Handle a changed requirement `[REQUIRED]`

Start from Block 3 green with its result recorded. Work in `projects/catalog/`;
focus on `scripts/challenge.py` and the output named below. Record `evidence/M1/index.md`.
Stop when C3 compatibility and changed-requirement evidence is recorded.
Resume at [Block 4](#4-handle-a-changed-requirement-required) using that saved result; continue to Block 5.
When needed: [C3 scenario and hints](CHALLENGE.md#c3--a-public-field-changes-unexpectedly) and [concept explanation](REFERENCE.md#generated-documentation-hid-a-breaking-change).

Complete C3 using the [requirement change record](../../templates/REQUIREMENTS.md#requirement-change-record). First preserve current behavior in
a test. Then add archival reason without silently breaking existing clients.
Record who decides an ambiguity, the smallest accepted scope, and rejected work.

After all contract tests pass, use the compatibility fault in C3. Record a
hypothesis before inspecting the changed test. Use the exact activation and reset
commands in [C3](CHALLENGE.md#c3--a-public-field-changes-unexpectedly).

### 5. Review and ship `[REQUIRED]`

Start from Block 4 green with its result recorded. Work in `projects/catalog/`;
focus on `evidence/M1/` and the output named below. Record `evidence/M1/index.md`.
Stop when the Core gate and honest operation record pass.
Resume at [Block 5](#5-review-and-ship-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [operation gate](ACCEPTANCE.md#a4--honest-operation) and [review prompts](ACCEPTANCE.md#review).

Serve the app using the documented no-reload command and inspect sanitized
request logs. Answer [review prompts](ACCEPTANCE.md#review), then prove [A1–A4](ACCEPTANCE.md#core)
in `evidence/M1/index.md`. Use the same issue → branch → pull request → Actions
→ evidence workflow learned in M0. Run `uv run --locked ruff check .`, `uv run --locked ruff format --check .`,
`uv run --locked mypy`, and `uv run --locked pytest`. Tag the reviewed result
`m1-api-foundation` only after the learner-owned gate passes.

## Understand

- **HTTP contract:** the public agreement formed by methods, paths, status
  codes, headers, and response bodies.
- **Idempotent:** repeating a request has the same intended effect as once.
- **Pagination:** returning a bounded, ordered part of a collection.
- **OpenAPI:** a machine-readable description of the HTTP interface.
- **Product invariant:** a rule such as “price is positive” that must remain
  true regardless of which endpoint changes state.

Use the [fixed catalog client contract](../../projects/catalog/specs/M1-PRODUCT-BRIEF.md#required-behavior). It owns requests, errors, repeat behavior, and pagination; internal design remains yours.

## Use a tool if earned

Use Air forms for browser validation and FastAPI/Pydantic for the retained JSON
contract. Implement ordering and cursors explicitly before evaluating a
pagination package; see [tool timing](REFERENCE.md#evaluate-after-evidence).

## Prove it

Use the current scenario’s observation, boundary, and reference hints in order;
return to green before starting another fault. [C1 missing contract](CHALLENGE.md#c1--the-client-contract-is-missing), [C2 invalid input](CHALLENGE.md#c2--invalid-input-must-not-corrupt-valid-state), and [C3 compatibility](CHALLENGE.md#c3--a-public-field-changes-unexpectedly).

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Record commands, predictions, observed failures, recovery, and limitations in
`projects/catalog/evidence/M1/index.md`. Answer [review prompts](ACCEPTANCE.md#review) and prove the [Core gate](ACCEPTANCE.md#core).

## Done / next

- Consumer examples and the implemented HTTP behavior agree.
- Validation, retry behavior, pagination, and errors have focused tests.
- A public breaking change is detected rather than silently accepted.
- The limitation statement makes no persistence, security, or operations claim.
- A cold reviewer can execute one success, one error, and one retry from the docs.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m1) only for the question left by the active hint ladder.

Use the [catalog troubleshooting guide](../../projects/catalog/README.md#if-setup-fails).
Run the single failing test with `-vv`, compare expected and actual HTTP data,
and inspect the route/model boundary before changing architecture. Reset an
active challenge before switching branches.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M2 — POS Persistence / Data Modeling](../m2-pos-persistence-data-modeling/README.md).

[Previous milestone: M0](../m0-engineering-baseline/README.md) · [Course home](../../README.md) · [Next milestone: M2](../m2-pos-persistence-data-modeling/README.md)
