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

## Review

### M0 review

Answer these in `projects/catalog/evidence/M0/index.md` using your own words:

1. Which tracked files recreate the environment? What remained local?
2. What does `uv.lock` guarantee, and what does it not guarantee?
3. Why does the smoke test send an HTTP request instead of calling the endpoint function directly?
4. How did you prove each test or check could detect its claimed defect?
5. What happened when configuration was missing or malformed?
6. What is the difference between Ruff, mypy, and pytest?
7. Why is `/health` liveness rather than full dependency readiness?

Review the diff for generated files, secrets, undocumented commands, unnecessary
folders, platform assumptions, and disagreement between local and CI commands.
Repeat one failure without your notes and state your hypothesis before inspecting
the cause.

For a **cold review**, use a peer or return later in a clean checkout without
implementation notes. The reviewer repeats one Core API path and one failure,
records confusion and fixes, and gives `PASS` or `NEEDS WORK`.

Optional background lens, with the same A0–A3 gate:

- A career shifter may connect a prior troubleshooting habit to the C1 hypothesis.
- A data specialist may contrast a data-value check with an HTTP/configuration contract.
