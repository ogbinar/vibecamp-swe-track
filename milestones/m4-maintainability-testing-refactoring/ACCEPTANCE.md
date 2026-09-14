# Acceptance gate

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
