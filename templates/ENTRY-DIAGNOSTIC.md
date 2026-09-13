# Entry diagnostic and targeted remediation

Run this after obtaining the M0 starter/walking skeleton and before its main challenges. It is a routing aid, not an exam: passing reduces repetition, while failing selects a short practice loop. No result waives an M0 Core criterion.

## Protocol

1. Work alone from repository instructions; cap the first attempt at 45 minutes.
2. Copy the table into project-local `evidence/M0/entry-diagnostic.md`. Replace angle-bracket commands with the commands documented by the starter.
3. Before each command, predict the useful output or failure. Record command, exit code, observation, and one-sentence explanation.
4. For each `REMEDIATE`, complete only its targeted loop, then rerun that signal once. If it still fails, open a focused issue; do not expand M0 into a prerequisite course.

## Signals and routing

| ID | Task and command | `READY` evidence | If not ready, targeted remediation |
|---|---|---|---|
| D1 Git/shell | From an unexpected directory, locate the repository, run `git status --short`, and identify ignored versus tracked configuration without changing history. | Correct root/branch/status interpretation; no secret is staged. | Practice `pwd`, path navigation, `git status`, and ignore rules on a disposable file; then remove the disposable file and rerun D1. |
| D2 Python/typing | Run `python3 -c "from decimal import Decimal; print(Decimal('0.10') + Decimal('0.20'))"`; inspect one starter type annotation and predict one invalid call/input. | Output is `0.30`; explanation distinguishes runtime value from type hint. | Read the annotated function and Python typing/Decimal references; make one tiny scratch example outside production code, then rerun D2. |
| D3 HTTP | Start with `<documented run command>` and run `curl -i http://127.0.0.1:<port>/health`. Identify status line, content type, and body. | Names all three and explains whether the response proves liveness or readiness. | Review the M0 health contract and HTTP response anatomy; annotate one captured response, then rerun D3. |
| D4 Tests/debugging | Run `<documented test command>`. In a disposable change, alter the expected health field, rerun the narrow test, explain the failure, restore the file, and rerun. | Test fails for the predicted assertion, then passes after restoration; working tree is clean except intended learner work. | Read the failing assertion top-to-bottom, run only that test with verbose output, write expected versus actual, restore, and rerun D4. |
| D5 environment/configuration | Run the documented startup with one required variable absent, then with its safe example value. | Missing input fails non-zero without value leakage; safe configuration starts. | Trace setting name from `.env.example` to validation/startup; document value source and failure, then rerun D5. |

## Routing result

Record `READY` or `REMEDIATE → READY/OPEN ISSUE` for D1–D5, the bounded remediation used, and the next M0 challenge. Do not record a score, rank learners, or infer job readiness from this diagnostic.
