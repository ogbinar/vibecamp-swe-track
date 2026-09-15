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
