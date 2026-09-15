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
the [glossary](../../docs/reference/glossary.md) when it first becomes relevant.

## Product objective

- **Product can:** validate a browser product draft and expose a predictable JSON contract for clients.
- **You will prove:** the request matrix, invalid-form/API behavior, and compatibility-change evidence.

## Start here

- **Gate:** [A1–A4 / A + selected B](#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../docs/maintainers/usability.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/catalog/README.md#run-the-green-baseline), then return to the saved block; first visit: [Block 1](#1-describe-client-behavior-before-routes-required).

Start from your reviewed `m0-engineering-baseline` tag. Confirm the six tests
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
When needed: [client response explanation](#the-client-cannot-predict-the-response). [Tool boundaries](#tools-earned-here) apply to this product.

Read the [supplied product brief](../../projects/catalog/specs/M1-PRODUCT-BRIEF.md)
and [reference](#m1-concepts-through-client-problems). Copy its request matrix into your evidence and
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
When needed: [C1 scenario and hints](#c1--the-client-contract-is-missing) and [concept explanation](#a-repeat-request-created-another-effect).

Use the [tool boundaries](#tools-earned-here). Keep state in memory so HTTP behavior is
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
When needed: [C2 scenario and hints](#c2--invalid-input-must-not-corrupt-valid-state) and [concept explanation](#generated-documentation-hid-a-breaking-change).

Complete C1 and C2 in the [challenge brief](#challenge-brief). Test rules in isolation only
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
When needed: [C3 scenario and hints](#c3--a-public-field-changes-unexpectedly) and [concept explanation](#generated-documentation-hid-a-breaking-change).

Complete C3 using the [requirement change record](../../templates/REQUIREMENTS.md#requirement-change-record). First preserve current behavior in
a test. Then add archival reason without silently breaking existing clients.
Record who decides an ambiguity, the smallest accepted scope, and rejected work.

After all contract tests pass, use the compatibility fault in C3. Record a
hypothesis before inspecting the changed test. Use the exact activation and reset
commands in [C3](#c3--a-public-field-changes-unexpectedly).

### 5. Review and ship `[REQUIRED]`

Start from Block 4 green with its result recorded. Work in `projects/catalog/`;
focus on `evidence/M1/` and the output named below. Record `evidence/M1/index.md`.
Stop when the Core gate and honest operation record pass.
Resume at [Block 5](#5-review-and-ship-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [operation gate](#a4--honest-operation) and [review prompts](#review).

Serve the app using the documented no-reload command and inspect sanitized
request logs. Answer [review prompts](#review), then prove [A1–A4](#core)
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
pagination package; see [tool timing](#evaluate-after-evidence).

## Prove it

Use the current scenario’s observation, boundary, and reference hints in order;
return to green before starting another fault. [C1 missing contract](#c1--the-client-contract-is-missing), [C2 invalid input](#c2--invalid-input-must-not-corrupt-valid-state), and [C3 compatibility](#c3--a-public-field-changes-unexpectedly).

Answer [review prompts](#review) after the Core proof.

Record commands, predictions, observed failures, recovery, and limitations in
`projects/catalog/evidence/M1/index.md`. Answer [review prompts](#review) and prove the [Core gate](#core).

## Done / next

- Consumer examples and the implemented HTTP behavior agree.
- Validation, retry behavior, pagination, and errors have focused tests.
- A public breaking change is detected rather than silently accepted.
- The limitation statement makes no persistence, security, or operations claim.
- A cold reviewer can execute one success, one error, and one retry from the docs.

### Recovery

Use [targeted references](#resources-for-m1) only for the question left by the active hint ladder.

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


---

## Challenge brief

Run commands from `projects/catalog/`. Preserve failing output and a hypothesis
before inspecting implementation files.

## **C1 — The client contract is missing**

**PROVIDED** — the product brief and black-box contract are supplied; you build
the application behavior.

### Steps

1. Run the supplied contract and record the first 404 response.
2. Implement create, retrieve, list, replace, and retire one example at a time.
3. Rerun the complete contract and preserve the final green result.

Run:

```bash
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected initially: HTTP 404 failures. Implement create, retrieve, list,
replace, and retire behavior from the product brief one example at a time.

### Hints

1. Compare the first unexpected status with the request path.
2. Inspect `app.py` for route ownership and `models.py` for transport shape.
3. Use the FastAPI response-model and status-code references.

### Reset

Run `python3 scripts/challenge.py reset`, then rerun the supplied contract.

Evidence: request matrix, named tests, expected/actual responses, and the final
green contract run.

## **C2 — Invalid input must not corrupt valid state**

**YOU BUILD** — add focused invalid-input cases without changing the published
contract.

### Steps

1. Add one negative-price and one missing-replacement-field HTTP case.
2. Prove each rejection preserves the prior in-memory state.
3. Add ordered bounded-list cases and rerun the complete contract.

Run the replacement and invalid-input tests with `-vv`. Seed one negative price
or missing replacement field through HTTP; do not mutate the store directly.

Expected: HTTP 422 and the prior product remains unchanged. Then create products
in reverse order and prove listing remains ordered and bounded.

### Hints

1. Distinguish request-shape validation from a product rule.
2. Inspect when validation occurs relative to the in-memory write.
3. Use the Pydantic strictness and FastAPI validation references.

### Reset

Recreate the in-memory app fixture, then run
`PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q`.

## **C3 — A public field changes unexpectedly**

**PROVIDED** — activation changes the application response model while the
consumer contract remains unchanged. Never repair this by weakening the test.

### Steps

1. Activate compatibility and record the OpenAPI failure and affected client.
2. Preserve compatibility or document the authorized change and deprecation.
3. Reset the challenge and rerun the supplied contract.

After the M1 contract is green:

```bash
python3 scripts/challenge.py activate compatibility
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected: the OpenAPI compatibility test fails. Record the observed public
change and affected client before reading the changed file. Restore with:

```bash
python3 scripts/challenge.py reset
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Use the requirements template for the archival-reason request. Record decision
owner, accepted behavior, rejected scope, and deprecation only if compatibility
cannot be preserved.

### Hints

1. Compare the changed OpenAPI property set with the documented client response.
2. Inspect the response model and compatibility assertion, not every route.
3. Use the OpenAPI specification link in the Reference section below; do not weaken the guard.

### Reset

Run `python3 scripts/challenge.py reset`, then rerun the supplied contract.


---

## Acceptance gate

Required maturity: **Level A plus selected Level B boundary engineering**. M1
makes no Level C claim.

## Core

### **A1 — Public HTTP behavior**

- [ ] Create returns HTTP 201, the product representation, and `Location`.
- [ ] Retrieve distinguishes a known product from a missing product.
- [ ] Full replacement rejects missing fields without changing stored state.
- [ ] Repeated retirement has the same intended effect and representation.
- [ ] API evidence names the exact contract tests and sanitized responses.

### **A2 — Validation and pagination**

- [ ] Negative price, invalid money precision, blank identity, and oversized limit fail deliberately.
- [ ] Errors use the published envelope instead of an unhandled 500.
- [ ] Listing is ordered by SKU and bounded to 1–100 results.
- [ ] Empty and final pages return `next: null`.
- [ ] Unit tests isolate only rules that become clearer outside HTTP.

### **A3 — Compatibility and changed requirements**

- [ ] The OpenAPI comparison fails when a required product field changes.
- [ ] C3 preserves the failing observation, hypothesis, reset, and regression proof.
- [ ] The archival-reason brief records decision owner and accepted/rejected scope.
- [ ] Release notes describe any unavoidable compatibility break and deprecation.

### **A4 — Honest operation**

- [ ] M0 and M1 checks pass from a clean copy with locked dependencies.
- [ ] Development and no-reload commands serve the same tested contract.
- [ ] Documentation states that state is volatile and security/deployment/recovery are absent.
- [ ] GitHub Actions runs the locked baseline and collects the opt-in M1 contract.
- [ ] A cold reviewer repeats one success, one error, and one retry from the docs.

Record command, environment, expected result, actual result, interpretation, and
limitation. A screenshot alone is not evidence.

## Execution map

Checklist bullets under each A ID are local steps in written order. Run from
`projects/catalog/`: A1–A3 use
`PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q`; A4 uses
`uv run --locked ruff check . && uv run --locked ruff format --check . && uv run --locked mypy && uv run --locked pytest`.
Expected: named behavior and regressions are green. Record results under the
matching A heading in `evidence/M1/index.md`; recover with
`python3 scripts/challenge.py reset` and rerun the last green command.

## Stretch

Add ETag conditional replacement or a tiny typed client only after Core. Tests
must preserve the established public contract.

## Review

### Review

Answer one question at a time in `evidence/M1/index.md`:

1. How is an HTTP safe method different from an idempotent operation?
2. Which invalid input is rejected by transport validation?
3. Which invalid input is rejected by a product invariant?
4. What exact order makes pagination stable?
5. Which public breaking change could internal unit tests miss?
6. Why is this API production-minded but not production-ready?
7. For each endpoint, what happens on success, unknown identity, and repeat?
8. Which test could falsely pass, and which controlled defect proves it can fail?
9. Which persistence or authentication idea did you defer, and why?


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M1 concepts through client problems

## “The client cannot predict the response”

**Example:** two identical create requests return different shapes. **Term — HTTP
contract:** the public agreement covering method, path, status, headers, and
body. **Rule:** publish examples first and test the complete observable response.

## “A repeat request created another effect”

**Example:** a network retry retires the same product twice. **Term — idempotent
operation:** repeating it has the same intended final effect as doing it once.
An HTTP safe method is different: it is intended only to read. **Rule:** declare
repeat behavior per operation and prove it at the API boundary.

## “The list changes between pages”

**Example:** a page has no stable last item. **Term — pagination:** returning a
bounded, ordered part of a collection. **Rule:** define total order, limit,
cursor meaning, and empty/final response before implementation.

## “Generated documentation hid a breaking change”

**Example:** a field rename still returns HTTP 200 but breaks a client. **Term —
compatibility check:** an automated comparison that detects an unintended public
contract change. **Rule:** use Pydantic for transport shape, named product logic
for invariants, and API/OpenAPI tests for observable drift. “Production-minded”
here means a predictable boundary, not persistence, security, or deployment.

### Tools earned here

- **FastAPI routing + generated OpenAPI:** express and inspect the contract; generated docs do not replace consumer examples.
- **FastAPI CLI/Uvicorn runtime:** serve the ASGI application with one documented development command and one no-reload production-shaped command; an application framework is not its own process manager or deployment platform.
- **Pydantic request/response models:** reject ambiguity at the edge; avoid reusing one model for create/update/read when semantics differ.
- **HTTPX + pytest:** API acceptance and rule-level tests; use doubles only for true boundaries.
- **Decimal:** represent money without binary floating-point corruption.

Keep the repository in memory so persistence cannot distract from HTTP reasoning. Implement stable ordering, limits, and pagination behavior before considering `fastapi-pagination`; the adapter must preserve rather than define the contract. Avoid SQLAlchemy, auth, a pagination library, and generic service/base classes. An earned typed client is Stretch only after semantic compatibility checks exist.

## Evaluate after evidence

Evaluate only the optional tools named in the tool guidance above, after the stated simpler baseline has failed. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates the current behavior, or creates a second application path.

## Sources

### Resources for M1

Open a reference only after the matching question appears. Reviewed 2026-09-13.

- [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) — Which method, status, or header expresses this outcome? Applicable standard: RFC 9110.
- [FastAPI response status codes](https://fastapi.tiangolo.com/tutorial/response-status-code/) — How does the declared contract reach OpenAPI and the response? Applicable tool: current FastAPI docs.
- [FastAPI response models](https://fastapi.tiangolo.com/tutorial/response-model/) — Which declared output shape is filtered, documented, and validated? Applicable tool: current FastAPI docs.
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) — Where should input validation and output shape live? Applicable tool: Pydantic 2.
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html) — What makes an API change structurally compatible? Applicable standard: current OpenAPI specification.

Prefer the RFC for protocol meaning and framework documentation for implementation details.
