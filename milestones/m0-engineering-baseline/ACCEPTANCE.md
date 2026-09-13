# Acceptance gate

Required maturity: **Level A**, plus reproducibility foundations used by later levels.

## Core

- **A0:** The entry record contains D1–D5 commands/artifacts, predictions, exit codes/observations, `READY` or bounded remediation plus re-check, and any focused issue; it explicitly grants no Core exemption.
- **A1:** From a clean checkout, the pinned Python/uv install, Ruff lint/format, mypy, pytest, and declared `fastapi run`/Uvicorn commands succeed; no production command uses reload; HTTP tests assert health and a typed sample response; the seeded C1 type/behavior defects fail the intended checks.
- **A2:** Missing/invalid configuration exits non-zero with an actionable message; `.env.example` lists every setting; repository, logs, and evidence contain no seeded secret.
- **A3:** Actions runs the same locked dependency, Ruff, mypy, pytest, and curriculum-validator path as local development; it is labeled CI rather than CD; issue, PR, evidence index, `PROGRESS`, and annotated tag are mutually linked.

Record exact commands, environment, expected/actual output, and interpretation. Also show `git status --ignored` excludes environments, caches, secrets, and local data.

## Stretch

Test a second supported Python version, or add a task runner only after demonstrating real command drift. Stretch never blocks or replaces Core.
