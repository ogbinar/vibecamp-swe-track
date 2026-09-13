# M4 — Maintainability, Testing & Refactoring

**Capability:** change a tested system safely and improve boundaries under real pressure. **Deliverable:** add returns and configurable promotions to the existing POS while refactoring duplicated/scattered behavior into a coherent modular monolith.

Prerequisite: M3 correctness evidence. Sequence: characterize behavior → make a deliberately awkward change → measure scatter/coupling → design smallest boundary → refactor with tests green → seed boundary/test defects → operate the unchanged deployable → ship `m4-maintainable`.

Outputs: module ownership map, explicit service/repository/composition boundaries, balanced unit/integration/API suite, and before/after change evidence. No rewrite and no service split.
