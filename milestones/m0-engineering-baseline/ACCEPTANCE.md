# M0 acceptance gate

Required maturity: **Level A — Works**, plus the reproducibility foundation
used by later milestones. Core items are mandatory; Stretch is optional.

## Core

### **A0 — Entry and remediation**

- [ ] D1–D5 contain your prediction, command, exit code or observation, and explanation.
- [ ] Each `REMEDIATE` item links its bounded practice and successful re-check or a focused open issue.
- [ ] The diagnostic did not waive any Core item.

### **A1 — Clean, runnable baseline**

- [ ] A clean checkout succeeds with the documented uv, Ruff, mypy, pytest, and run commands.
- [ ] `/health` and `/products/sample` return the documented HTTP status, content type, and JSON shape.
- [ ] The production-shaped `fastapi run` command does not enable development reload.
- [ ] C1 behavior and type faults fail the intended check, are diagnosed, and return to green.

### **A2 — Configuration safety**

- [ ] Missing and malformed required configuration exit non-zero with an actionable error.
- [ ] `.env.example` lists safe names/examples while `.env` remains ignored.
- [ ] Source, logs, tests, and evidence contain no secret values.

### **A3 — Matching automation and release trail**

- [ ] GitHub Actions runs the same locked Ruff, mypy, pytest, and curriculum checks used locally.
- [ ] C3 proves dependency/runtime drift is detected and recoverable.
- [ ] The M0 issue, pull request, evidence index, `PROGRESS.md`, and annotated tag link to the reviewed work.

Record commands, environment, expected result, actual result, and interpretation.
A screenshot alone is not evidence.

## Stretch

Test a second supported Python version, or add a task runner only after showing
real command drift. Stretch never blocks or replaces Core.
