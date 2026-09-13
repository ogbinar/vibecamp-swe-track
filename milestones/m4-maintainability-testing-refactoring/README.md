# M4 — Maintainability, Testing, and Refactoring

[Course home](../../README.md) / M4

**Milestone 5 of 11 · M4**

## Why

A small promotion change now touches routes, database code, and calculations in
many places. Change the existing POS safely and reduce that scatter without a rewrite.

## Starting checkpoint

- **At a glance:** Maintainable · POS.
- **You will leave with:** Cashier-name change and boundary check; Refactor evidence and portfolio draft.
- **Gate:** [A1–A6 / Level B](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/pos/README.md#pos-launch-kit-for-m2), then return to the saved block; first visit: [Block 1](#1-characterize-the-awkward-baseline-required).

Start from `m3-transactions-correctness`. Run all POS tests and record the files
currently touched by one awkward promotion and return requirement.

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Cohesion:** related behavior is owned together.
- **Coupling:** one change forces changes in other parts.
- **Dependency injection:** code receives a collaborator instead of constructing it secretly.
- **Service boundary:** ownership of a business operation spanning several actions.
- **Characterization test:** a test preserving current behavior before refactoring.

## Product brief

Use the [fixed stakeholder change](../../projects/pos/specs/M4-CHANGE-BRIEF.md).
Add configurable promotions and returns. Complete C1 before moving code: preserve
current behavior, implement the awkward change, and measure scatter. In C2, add
only the smallest boundary that reduces it. In C3, deliberately weaken a test or
boundary and prove the suite notices. Use [CHALLENGE.md](CHALLENGE.md#m4-challenge-brief) for the
exact evidence and [TOOLS.md](TOOLS.md#tools-earned-here) for rejection criteria.

No rewrite, microservice split, generic base class, or pass-through layer is
allowed. Record one attractive complexity you rejected.

## Work blocks

### 1. Characterize the awkward baseline `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/pos/`;
focus on `tests/m4/test_characterization.py` and the output named below. Record `evidence/M4/baseline.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 1](#1-characterize-the-awkward-baseline-required) using that saved result; continue to Block 2.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--stakeholder-driven-technical-debt-change) and [concept explanation](CONCEPTS.md#one-small-request-touched-seven-files). [Tool boundaries](TOOLS.md#tools-earned-here) apply to this product.

**Supplied:** the [cashier-name change brief](../../projects/pos/specs/M4-CHANGE-BRIEF.md).
**You build:** characterization tests and a before-change scatter count in
`projects/pos/`. Run the smallest test, then the full suite. Record
`evidence/M4/baseline.md`. Stop when existing behavior is green and protected.

### 2. Deliver the fixed change `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m4/test_cashier_name.py` and the output named below. Record `evidence/M4/change.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 2](#2-deliver-the-fixed-change-required) using that saved result; continue to Block 3.
When needed: [C1 scenario and hints](CHALLENGE.md#c1--stakeholder-driven-technical-debt-change) and [concept explanation](CONCEPTS.md#one-small-request-touched-seven-files).

Add optional cashier display name end to end, including old-row behavior. Run
API and PostgreSQL tests; observe the new field and unchanged totals. Record
`evidence/M4/change.md`. If unrelated behavior changes, return to the last green
commit and split the work. Stop when the contract examples pass.

### 3. Refactor and enforce a boundary `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/pos/`;
focus on `tests/m4/test_architecture.py` and the output named below. Record `evidence/M4/refactor.md`.
Stop when this block’s [command-map row](#literal-command-map) passes and its evidence is saved.
Resume at [Block 3](#3-refactor-and-enforce-a-boundary-required) using that saved result; continue to [Evidence](#evidence).
When needed: [C3 scenario and hints](CHALLENGE.md#c3--false-confidence-tests) and [concept explanation](CONCEPTS.md#database-code-is-duplicated-across-endpoints). Localize [C2 duplication](CHALLENGE.md#c2--duplicated-database-behavior) before the C3 mutation.

Refactor only the duplication or coupling exposed by Block 2. Add a check that
fails when an API module imports the engine directly. Record scatter, dependency
rule, rejected abstraction, and regression run in `evidence/M4/refactor.md`.
Stop when behavior is unchanged and a controlled boundary mutation is detected.

### Literal command map

Run from `projects/pos/`; create each named learner test before expecting green.

Before: characterization is missing or the controlled mutation escapes. After:
the row’s stop condition is green and before/after scatter is recorded.

| Block | Learner target | Copyable command | Expected stop condition |
|---|---|---|---|
| 1 | `tests/m4/test_characterization.py` | `uv run --locked pytest tests/m4/test_characterization.py -q` | Existing behavior is characterized and the initial scatter count is recorded. |
| 2 | `tests/m4/test_cashier_name.py` | `POS_TEST_DATABASE_URL=postgresql+psycopg://vibecamp:vibecamp@127.0.0.1:5432/vibecamp_pos uv run --locked pytest tests/m4/test_cashier_name.py -q` | New and legacy examples pass without changing receipt totals. |
| 3 | `tests/m4/test_architecture.py` | `uv run --locked pytest tests/m4/test_architecture.py -q` | The allowed graph passes and a controlled forbidden import is detected. |

Recover with `git diff --stat` and the last green focused test; revert only your
current learner edit, never the course repository. Record the next row before pausing.

Pause: preserve the last green characterization result and next change.

## Failures and hints

Activate or construct only the current C scenario. Record the symptom and one
hypothesis before inspecting the implementation. Use the matching scenario link
in your active block, then its three hint levels in order. Reset to the last
green checkpoint before starting another scenario.

## Evidence

Answer [review prompts](REVIEW.md#review) after the Core proof.

Prove [A1–A6](ACCEPTANCE.md#core) with before/after change scatter,
unit/integration/API tests, a complexity-rejection record, and the interim
portfolio case study.

## Done when

The requested variants are localized, the test layers catch their intended
failures, and all Core checks pass. Tag `m4-maintainable-pos`.

## Recovery

Use [targeted references](RESOURCES.md#resources-for-m4) only for the question left by the active hint ladder.

If tests become hard to interpret, return to the last green commit, run the
narrowest behavior check, and refactor in smaller steps.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M5](../m5-secure-multi-user-ecommerce/README.md).

[Previous milestone: M3](../m3-transactions-correctness/README.md) · [Course home](../../README.md) · [Next milestone: M5](../m5-secure-multi-user-ecommerce/README.md)
