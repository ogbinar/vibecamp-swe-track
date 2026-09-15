# M4 — Change the POS without breaking it

[Course home](../../README.md) / M4

**Milestone 5 of 11 · M4**

## Business problem

A small receipt-field change now touches routes, database code, and calculations in
many places. Change the existing POS safely and reduce that scatter without a rewrite.

## Product objective

- **Product can:** receipts can carry an optional cashier display name without scattering the change.
- **You will prove:** characterization, dependency-boundary, refactor, and portfolio evidence.

Use the [fixed stakeholder change](../../projects/pos/specs/M4-CHANGE-BRIEF.md).
Add the optional cashier display name from the fixed brief. Complete C1 before moving code: preserve
current behavior, implement the awkward change, and measure scatter. In C2, add
only the smallest boundary that reduces it. In C3, deliberately weaken a test or
boundary and prove the suite notices. Use the [challenge brief](#challenge-brief) for the
exact evidence and [reference](#tools-earned-here) for rejection criteria.

No rewrite, microservice split, generic base class, or pass-through layer is
allowed. Record one attractive complexity you rejected.

## Start here

- **Gate:** [A1–A6 / Level B](#core).
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-characterize-the-awkward-baseline-required).

Start from `m3-transactions-correctness`. Run all POS tests and record the files
currently touched by the optional cashier-name requirement.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Characterize the awkward baseline `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m4/test_characterization.py` and the output named below. Record `evidence/M4/baseline.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 1](#1-characterize-the-awkward-baseline-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](#c1--stakeholder-driven-technical-debt-change) and [concept explanation](#one-small-request-touched-seven-files). [Tool boundaries](#tools-earned-here) apply to this product.

**Supplied:** the [cashier-name change brief](../../projects/pos/specs/M4-CHANGE-BRIEF.md).
**You build:** characterization tests and a before-change scatter count in
`projects/pos/`. Run the smallest test, then the full suite. Record
`evidence/M4/baseline.md`. Stop when existing behavior is green and protected.

Run from the stated project directory:

```bash
uv run --locked pytest tests/m4/test_characterization.py -q
```

### 2. Deliver the fixed change `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m4/test_cashier_name.py` and the output named below. Record `evidence/M4/change.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 2](#2-deliver-the-fixed-change-required) using that saved result; continue to Block 3.
When needed: [C1 scenario and hints](#c1--stakeholder-driven-technical-debt-change) and [concept explanation](#one-small-request-touched-seven-files).

Add optional cashier display name end to end, including old-row behavior. Run
API and PostgreSQL tests; observe the new field and unchanged totals. Record
`evidence/M4/change.md`. If unrelated behavior changes, return to the last green
commit and split the work. Stop when the contract examples pass.

Run from the stated project directory:

```bash
POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m4/test_cashier_name.py -q
```

### 3. Refactor and enforce a boundary `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m4/test_architecture.py` and the output named below. Record `evidence/M4/refactor.md`.
Stop when this block’s listed command passes and its evidence is saved.
Resume at [Block 3](#3-refactor-and-enforce-a-boundary-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [C3 scenario and hints](#c3--false-confidence-tests) and [concept explanation](#database-code-is-duplicated-across-endpoints). Localize [C2 duplication](#c2--duplicated-database-behavior) before the C3 mutation.

Refactor only the duplication or coupling exposed by Block 2. Add a check that
fails when an API module imports the engine directly. Record scatter, dependency
rule, rejected abstraction, and regression run in `evidence/M4/refactor.md`.
Stop when behavior is unchanged and a controlled boundary mutation is detected.

Run from the stated project directory:

```bash
uv run --locked pytest tests/m4/test_architecture.py -q
```

### Diagnose deliberate failures

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Understand

- **Cohesion:** related behavior is owned together.
- **Coupling:** one change forces changes in other parts.
- **Dependency injection:** code receives a collaborator instead of constructing it secretly.
- **Service boundary:** ownership of a business operation spanning several actions.
- **Characterization test:** a test preserving current behavior before refactoring.

## Use a tool if earned

Use the current project dependencies first. Open [Use now](#use-now) for the active pattern, [Evaluate after evidence](#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](#review) after the Core proof.

Prove [A1–A6](#core) with before/after change scatter,
unit/integration/API tests, a complexity-rejection record, and the interim
portfolio case study.

## Done / next

The requested change is localized, the test layers catch their intended
failures, and all Core checks pass. Tag `m4-maintainable-pos`.

### Recovery

Use [targeted references](#resources-for-m4) only for the question left by the active hint ladder.

If tests become hard to interpret, return to the last green commit, run the
narrowest behavior check, and refactor in smaller steps.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M5](../m5-secure-multi-user-ecommerce/README.md).

[Previous milestone: M3](../m3-transactions-correctness/README.md) · [Course home](../../README.md) · [Next milestone: M5](../m5-secure-multi-user-ecommerce/README.md)


---

## Challenge brief

Run from `projects/pos/`. Preserve behavior before restructuring code.

## **C1 — Stakeholder-driven technical-debt change**

**PROVIDED** — the fixed cashier-name change brief is supplied.

### Steps

1. Record decision owner, compatibility need, accepted behavior, and rejected scope.
2. Create `tests/m4/test_characterization.py`; count files touched by the awkward change.
3. Run README Blocks 1–2 and keep behavior change separate from refactoring.

### Hints

1. List observable behavior before judging structure.
2. Inspect each route, model, query, and serializer touched by cashier name.
3. Use the pytest characterization link in the Reference section below.

### Reset

Stash only the current learner edit, then run
`uv run --locked pytest tests/m4/test_characterization.py -q`.

## **C2 — Duplicated database behavior**

**YOU BUILD** — localize only the duplication the change exposes.

### Steps

1. Record repeated session, transaction, and query behavior.
2. Add the smallest service/repository or injected dependency that reduces scatter.
3. Run `uv run --locked pytest tests/m4/test_cashier_name.py -q` and compare counts.

### Hints

1. Ask which behavior changes together instead of applying a layer template.
2. Inspect transaction ownership and repeated data access.
3. Use the dependency-injection link in the Reference section below; reject pass-through layers.

### Reset

Remove the proposed boundary while keeping characterization tests, then rerun
`uv run --locked pytest tests/m4/test_cashier_name.py -q`.

## **C3 — False-confidence tests**

**YOU BUILD** — create a reversible test or dependency-boundary mutation.

### Steps

1. Show one mock-heavy test staying green while a mapping or route is broken.
2. Replace it with the owning integration/API test; create `tests/m4/test_architecture.py`.
3. Add one forbidden import, observe failure, restore it, and rerun Block 3.

### Hints

1. Name the real boundary the test never crossed.
2. Inspect serialization, mappings, dependency direction, and fixture realism.
3. Use the testing-boundaries link in the Reference section below.

### Reset

Remove the forbidden import and run `uv run --locked pytest tests/m4/test_architecture.py -q`.

Complete one [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md)
with a measurable revisit trigger.


---

## Acceptance gate

Required maturity: **Level B**, emphasizing changeability and test fitness.

## Core

- **A1:**
  - [ ] M3 behavior remains green
  - [ ] C1 preserves stakeholder/decision-owner/accepted-and-rejected-scope evidence
  - [ ] module map states ownership/dependency direction
  - [ ] the forbidden dependency fails automation
  - [ ] the cashier-name change reduces demonstrated change scatter without speculative layers; no second Core variant is required.
- **A2:**
  - [ ] C2 proves only earned dependency-injection/service/repository boundaries localize demonstrated orchestration or persistence change
  - [ ] a simple path remains direct, no retained layer merely forwards calls, and the use case owns transaction/invariant intent while repositories do not commit.
- **A3:**
  - [ ] Table-driven unit tests cover policies
  - [ ] real database integration and HTTP API tests cover wiring/contracts
  - [ ] C3 demonstrates and replaces a false-positive mock test.
- **A4:**
  - [ ] Refactor and behavior changes are reviewable, migrations stay compatible, one deployable/one database remains, and clean lint/test/migration/validator commands pass.
- **A5:**
  - [ ] One nontrivial candidate is rejected or removed using the complexity record.
  - [ ] The record names observed pressure, baseline comparison, lifecycle/operations cost, and decision boundary.
  - [ ] The record has a measurable revisit trigger.
- **A6:**
  - [ ] A draft [portfolio case study](../../templates/PORTFOLIO-CASE-STUDY.md) links the ambiguous requirement and C1/C3 failure evidence.
  - [ ] It links before/after change proof, personal contribution, and the simplicity decision.
  - [ ] It states current limitations without invented impact.

## Execution map

Each checklist bullet is a local step in order. From `projects/pos/`, use README
Block 1 for A1/A3, Block 2 for behavior in A1, and Block 3 for A2/A4. For A5 run
`test -s evidence/M4/complexity-rejection.md`; for A6 run
`test -s evidence/M4/portfolio.md`. Record results under matching A headings;
recover by rerunning the characterization test before refactoring again.

Evidence compares responsibilities/files touched and defect detection, not line counts or subjective “clean code.”

## Stretch

Apply mutation testing to one pure policy, or extract a library only after two real consumers prove stable behavior.

## Review

### Review

Answer one question at a time in `evidence/M4/index.md`:

1. Which coupling caused the highest change scatter?
2. Why does the new boundary group behavior that changes together?
3. What does the service own?
4. What does the repository own?
5. How does dependency injection make one test easier?
6. Why did the mock-based test pass while the product was wrong?
7. Did any repository commit, route import an engine, or refactor change behavior?
8. Which abstraction did you reject, and what future evidence would earn it?

Cold-read the draft portfolio case study: can a reviewer reach the requirement, preserved failure, regression proof, and complexity rejection in ten minutes? Lens prompt (same A1–A6 gate): a career-shifter translates domain/change-management judgment into the boundary decision; a data specialist explains why repository/SQL expertise does not replace service, API, and integration-test reasoning.


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M4 concepts through difficult changes

## “One small request touched seven files”

**Example:** a receipt field changes routes, SQL, and calculations separately.
**Term — coupling:** how much unrelated code a change forces you to know or
touch. **Rule:** measure scatter before adding a boundary.

## “Database code is duplicated across endpoints”

**Example:** session setup and the same query repeat in several routes. **Term —
dependency injection:** giving code its collaborator explicitly. **Rule:** add
only the service or repository boundary that localizes the demonstrated change.

## “Related behavior lives in unrelated places”

**Example:** the cashier display name touches routes, serialization, and SQL fragments.
**Term — cohesion:** keeping behavior that changes together close together.
**Rule:** add a boundary only when it measurably reduces change scatter or isolates
a real external/data seam.

## “A four-layer template added navigation but no value”

**Example:** route, service, and repository methods merely forward the same
arguments. **Term — composition root:** the place concrete collaborators are
assembled and injected. **Rule:** FastAPI dependencies are enough; earn services
through orchestration/invariants and repositories through repeated or complex data access.

## “The mocked test passed while the API was broken”

**Example:** a mock never crosses serialization or database mappings. **Term —
characterization test:** a test that preserves existing behavior before refactoring.
**Rule:** use unit, integration, and API tests for their distinct risks; separate
behavior changes from structure-preserving refactoring.

### Tools earned here

- **FastAPI dependency functions + composition root:** explicit lightweight DI; direct route-to-SQLAlchemy remains valid for simple cases, and needless provider layers are removed.
- **pytest fixtures/markers:** separate fast rule tests, real-database integration tests, and API acceptance tests.
- **Ruff import rules or a tiny dependency check:** enforce one demonstrated high-risk module direction; avoid a framework-sized architecture tool.
- **Git diff/history:** measure changed responsibilities and preserve behavior/refactor separation.

Avoid generic `BaseRepository`, `BaseService`, `utils`, complex DI, microservices, and shared libraries. Require before/after change-scatter evidence for each new service or repository; delete pass-through layers. The use case owns commit/rollback and repositories never auto-commit. An [architecture decision record (ADR)](../../templates/ADR.md) is optional only for a consequential boundary; routine refactoring belongs in the PR rationale.

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M4

Consult these when a change is hard to localize or a test gives false confidence. Reviewed 2026-09-13.

- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) — How can an endpoint receive a boundary without constructing it? Applicable tool: current FastAPI.
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — How can tests share setup without sharing mutable state? Applicable tool: pytest 8+.
- [Python typing specification](https://typing.python.org/en/latest/spec/) — What promise does a type annotation make to tools and readers? Applicable standard: current Python typing spec.

Introduce a boundary only when change evidence shows a real coupling problem.
