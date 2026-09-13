# Challenge brief

Use the full learning cycle for each scenario and capture hypotheses plus recovery.

Before C1, run D1–D5 in the [entry diagnostic](../../templates/ENTRY-DIAGNOSTIC.md). For each `REMEDIATE`, do only the named short exercise and one re-check; unresolved gaps become focused issues. Diagnostic success changes practice routing, not acceptance criteria.

- **C1 — Hidden workspace state:** Build the catalog slice, then remove the environment/caches and run from an unexpected directory. Seed a path/import fault and a health-response regression. Debug until clean setup, API test, project structure, and health check are deterministic.
- **C2 — Configuration leak:** Make one setting required, then omit and malform it. Ensure startup fails concisely, `.env.example` reveals names only, and test/log output contains no seeded secret.
- **C3 — Automation drift:** Alter a local command or dependency without updating CI/lock state. Diagnose the local/Actions disagreement, restore one canonical command path, and document release impact.

Refactor only duplicated setup knowledge. Operate by starting/stopping cleanly and inspecting exit codes. Ship through an issue, reviewed PR, evidence index, and annotated tag—without publishing as part of the challenge.
