# Acceptance gate

Required maturity: **Level B**, emphasizing changeability and test fitness.

## Core

- **A1:** M3 behavior remains green; C1 preserves stakeholder/decision-owner/accepted-and-rejected-scope evidence; module map states ownership/dependency direction; the forbidden dependency fails automation; two requirement variants reduce demonstrated change scatter without speculative layers.
- **A2:** C2 proves dependency injection plus service/repository boundaries localize orchestration/persistence while transaction and invariant ownership remain explicit.
- **A3:** Table-driven unit tests cover policies; real database integration and HTTP API tests cover wiring/contracts; C3 demonstrates and replaces a false-positive mock test.
- **A4:** Refactor and behavior changes are reviewable, migrations stay compatible, one deployable/one database remains, and clean lint/test/migration/validator commands pass.
- **A5:** One nontrivial candidate is rejected or removed using the complexity record with observed pressure, baseline comparison, lifecycle/operations cost, decision boundary, and measurable revisit trigger.
- **A6:** A draft [portfolio case study](../../templates/PORTFOLIO-CASE-STUDY.md) links the ambiguous requirement, C1/C3 failure evidence, before/after change proof, personal contribution, simplicity decision, and current limitations without invented impact.

Evidence compares responsibilities/files touched and defect detection, not line counts or subjective “clean code.”

## Stretch

Apply mutation testing to one pure policy, or extract a library only after two real consumers prove stable behavior.
