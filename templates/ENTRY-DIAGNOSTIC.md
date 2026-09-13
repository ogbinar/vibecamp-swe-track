# Entry diagnostic and targeted remediation

Run this after obtaining the M0 starter/walking skeleton and before its main challenges. It is a routing aid, not an exam: passing reduces repetition, while failing selects a short practice loop. No result waives an M0 Core criterion.

## Protocol

1. Work alone from repository instructions; cap the first attempt at 45 minutes.
2. From `projects/catalog/`, create `evidence/M0/entry-diagnostic.md` and copy
   the table below into it.
3. Before each command, predict the useful output or failure. Record command, exit code, observation, and one-sentence explanation.
4. For each `REMEDIATE`, complete only its targeted loop, then rerun that signal once. If it still fails, open a focused issue; do not expand M0 into a prerequisite course.

## Signals and routing

| ID | Task and command | `READY` evidence | If not ready, targeted remediation |
|---|---|---|---|
| D1 Git/shell | From an unexpected directory, locate the repository, run `git status --short`, and identify ignored versus tracked configuration without changing history. | Correct root/branch/status interpretation; no secret is staged. | Practice `pwd`, path navigation, `git status`, and ignore rules on a disposable file; then remove the disposable file and rerun D1. |
| D2 Python/typing | Run `python3 -c "from decimal import Decimal; print(Decimal('0.10') + Decimal('0.20'))"`; inspect one starter type annotation and predict one invalid call/input. | Output is `0.30`; explanation distinguishes runtime value from type hint. | Read the annotated function and Python typing/Decimal references; make one tiny scratch example outside production code, then rerun D2. |
| D3 HTTP | Run `uv run --locked fastapi dev src/catalog_api/main.py --port 8000`, then in a second terminal run `curl -i http://127.0.0.1:8000/health`. Identify status line, content type, and body; stop with `Ctrl+C`. | Names all three and explains whether the response proves liveness or readiness. | Review the M0 health contract and HTTP response anatomy; annotate one captured response, then rerun D3. |
| D4 Tests/debugging | Run `uv run --locked pytest`. Activate the bounded fault with `python3 scripts/challenge.py activate health`, run `uv run --locked pytest tests/test_api.py::test_health_reports_liveness`, explain the failure, then run `python3 scripts/challenge.py reset` and rerun the test. | Test fails for the predicted assertion, then passes after reset; no challenge remains active. | Read the failing assertion top-to-bottom, write expected versus actual, reset, and rerun D4. |
| D5 environment/configuration | Run `env -u CATALOG_SERVICE_NAME PYTHONPATH=src uv run --locked python -c "from catalog_api.settings import Settings; Settings(_env_file=None)"`, then run `CATALOG_SERVICE_NAME='Diagnostic Catalog' PYTHONPATH=src uv run --locked python -c "from catalog_api.settings import Settings; print(Settings(_env_file=None).service_name)"`. | Missing input exits non-zero without value leakage; the second command prints `Diagnostic Catalog`. | Trace `CATALOG_SERVICE_NAME` from `.env.example` to `Settings`, document its source and failure, then rerun D5. |

## Routing result

Record `READY` or `REMEDIATE → READY/OPEN ISSUE` for D1–D5, the bounded remediation used, and the next M0 challenge. Do not record a score, rank learners, or infer job readiness from this diagnostic.
