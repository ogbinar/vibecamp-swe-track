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
boundary and prove the suite notices. Use [CHALLENGE.md](CHALLENGE.md#m4-challenge-brief) for the
exact evidence and [REFERENCE.md](REFERENCE.md#tools-earned-here) for rejection criteria.

No rewrite, microservice split, generic base class, or pass-through layer is
allowed. Record one attractive complexity you rejected.

## Start here

- **Gate:** [A1–A6 / Level B](ACCEPTANCE.md#core).
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
When needed: [C1 scenario and hints](CHALLENGE.md#c1--stakeholder-driven-technical-debt-change) and [concept explanation](REFERENCE.md#one-small-request-touched-seven-files). [Tool boundaries](REFERENCE.md#tools-earned-here) apply to this product.

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
When needed: [C1 scenario and hints](CHALLENGE.md#c1--stakeholder-driven-technical-debt-change) and [concept explanation](REFERENCE.md#one-small-request-touched-seven-files).

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
When needed: [C3 scenario and hints](CHALLENGE.md#c3--false-confidence-tests) and [concept explanation](REFERENCE.md#database-code-is-duplicated-across-endpoints). Localize [C2 duplication](CHALLENGE.md#c2--duplicated-database-behavior) before the C3 mutation.

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

Use the current project dependencies first. Open [Use now](REFERENCE.md#use-now) for the active pattern, [Evaluate after evidence](REFERENCE.md#evaluate-after-evidence) only after the simpler baseline misses its target, and [Do not add yet](REFERENCE.md#do-not-add-yet) before adding another runtime or service.

## Prove it

Answer [review prompts](ACCEPTANCE.md#review) after the Core proof.

Prove [A1–A6](ACCEPTANCE.md#core) with before/after change scatter,
unit/integration/API tests, a complexity-rejection record, and the interim
portfolio case study.

## Done / next

The requested change is localized, the test layers catch their intended
failures, and all Core checks pass. Tag `m4-maintainable-pos`.

### Recovery

Use [targeted references](REFERENCE.md#resources-for-m4) only for the question left by the active hint ladder.

If tests become hard to interpret, return to the last green commit, run the
narrowest behavior check, and refactor in smaller steps.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M5](../m5-secure-multi-user-ecommerce/README.md).

[Previous milestone: M3](../m3-transactions-correctness/README.md) · [Course home](../../README.md) · [Next milestone: M5](../m5-secure-multi-user-ecommerce/README.md)
