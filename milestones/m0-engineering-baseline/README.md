# M0 — Engineering Baseline

**Capability:** make work reproducible before feature complexity arrives. **Deliverable:** create `projects/catalog/` with the thinnest FastAPI walking skeleton: health response, one typed sample product, locked dependencies, configuration contract, tests, and CI.

Prerequisites are a supported Python installation, Git, and willingness to delete/rebuild local state. Begin with the bounded [entry diagnostic](../../templates/ENTRY-DIAGNOSTIC.md): it routes gaps to targeted remediation but never waives Core work. Sequence: diagnose/remediate → specify the clean-checkout promise → build one vertical slice → automate it → break environment/configuration assumptions → repair and document → tag `m0-engineering-baseline`.

Outputs are a diagnostic routing record, runnable baseline, `.env.example`, documented install/run/lint/test commands, API smoke tests, passing Actions, and an M0 evidence index. This is reproducibility, not production readiness.
