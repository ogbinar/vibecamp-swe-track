# M0 — Engineering Baseline

[Course home](../../README.md) / M0

**Milestone 1 of 11 · M0**

## Why this matters

An application that works only on its author's machine is not reproducible.
Your first job is to make one small application start, test, fail, and recover
the same way for another person and in GitHub Actions.

You are given a **walking skeleton**: the smallest end-to-end application that
handles a real request and has a real test. You will not design a database or
large architecture here. You will expose hidden assumptions and make the setup
repeatable.

## Starting checkpoint

- **At a glance:** Reproducible · Catalog.
- **You will leave with:** Green baseline transcript; Failure diagnosis and reset record; CI-backed gate PR and annotated tag.
- **Gate:** [A1–A3 plus A0 diagnostic / Level A](ACCEPTANCE.md#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../USABILITY.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/catalog/README.md#run-the-green-baseline), then return to the saved block; first visit: [Block 1](#1-run-the-supplied-baseline-required).

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Terms used here

- **Walking skeleton:** the smallest working end-to-end application.
- **Reproducible:** another machine can rebuild and verify the same state.
- **CI (continuous integration):** checks GitHub runs for a proposed change.
- **Evidence:** a reproducible result supporting an engineering claim.
- **Cold review:** replay from clean instructions without the author's memory.

## Product brief

By the end of M0, `projects/catalog/` will have:

- A working health endpoint and one typed product response
- Locked dependencies and validated configuration
- Ruff, mypy, pytest, and API checks
- Safe, repeatable failure exercises
- GitHub continuous integration (CI)
- An issue, pull request, evidence index, and annotated `m0-engineering-baseline` tag

Terms such as endpoint, lockfile, linting, static type checking, evidence, and
cold review are defined in the [learner glossary](../../GLOSSARY.md).

The supplied walking skeleton serves health and one typed product response. Keep database and architecture work for later milestones.

## Work blocks

### 1. Run the supplied baseline `[REQUIRED]`

Start from the starting checkpoint above. Work in `projects/catalog/`;
focus on `src/catalog_api/` and `tests/test_api.py` and the output named below. Record `evidence/M0/index.md`.
Stop when all baseline checks and both HTTP responses pass.
Resume at [Block 1](#1-run-the-supplied-baseline-required) using that saved result; continue to Block 2.
When needed: [what the checks do](TOOLS.md#m0-tools-and-why-they-are-here); [tool references](RESOURCES.md#m0-resources). Do not activate a fault yet.

From the repository root:

```bash
cd projects/catalog
cp .env.example .env
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

Expected: every command exits with code `0`; pytest reports four passing tests.
If not, use the [starter troubleshooting guide](../../projects/catalog/README.md#if-setup-fails).

Start the application:

```bash
uv run --locked fastapi dev src/catalog_api/main.py --port 8000
```

In another terminal, still inside `projects/catalog/`:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/products/sample
```

Expected: both responses start with HTTP `200` and contain JSON. Stop the server
with `Ctrl+C`.

### 2. Understand the starting path `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/catalog/`;
focus on `src/catalog_api/main.py` and the output named below. Record `evidence/M0/index.md`.
Stop when the request-path explanation is recorded.
Resume at [Block 2](#2-understand-the-starting-path-required) using that saved result; continue to Block 3.
When needed: [trace the HTTP path](CONCEPTS.md#the-app-started-but-can-it-answer).

Read [the HTTP path](CONCEPTS.md#the-app-started-but-can-it-answer) and inspect only these files first:

- `pyproject.toml` declares the project and checks.
- `uv.lock` records exact resolved dependency versions.
- `src/catalog_api/main.py` creates the process entry point.
- `src/catalog_api/app.py` defines the two endpoints.
- `src/catalog_api/models.py` defines response shapes.
- `src/catalog_api/settings.py` validates configuration.
- `tests/test_api.py` checks behavior through HTTP.

Draw the path `curl → FastAPI endpoint → Pydantic response → HTTP response` in
your evidence notes. Explain each arrow in one sentence.

### 3. Run the entry diagnostic `[REQUIRED]`

Start from Block 2 green with its result recorded. Work in `projects/catalog/`;
focus on `src/catalog_api/` and `tests/test_api.py` and the output named below. Record `evidence/M0/index.md`.
Stop when D1–D5 results and remediation are recorded.
Resume at [Block 3](#3-run-the-entry-diagnostic-required) using that saved result; continue to Block 4.
When needed: [diagnostic signals and recovery](../../templates/ENTRY-DIAGNOSTIC.md#signals-and-routing).

Follow [the diagnostic protocol](../../templates/ENTRY-DIAGNOSTIC.md#protocol). It checks Git and
shell use, Python types, HTTP responses, test interpretation, and configuration.
It selects short remediation; it never waives M0 Core work.

Create your evidence file on the first visit only. If it already contains notes,
keep them and fill missing template sections instead of copying over it:

```bash
mkdir -p evidence/M0
cp ../../templates/EVIDENCE-INDEX.md evidence/M0/index.md
```

Compare its level of detail with the clearly marked
[synthetic example](../../projects/catalog/evidence/M0/EXAMPLE.md). Do not copy
the example's claims as your own.

### 4. Diagnose the supplied failures `[REQUIRED]`

Start from Block 3 green with its result recorded. Work in `projects/catalog/`;
focus on `src/catalog_api/` and `tests/test_api.py` and the output named below. Record `evidence/M0/index.md`.
Stop when each C1–C3 failure is recorded and reset to green.
Resume at [Block 4](#4-diagnose-the-supplied-failures-required) using that saved result; continue to Block 5.
When needed: [C1 first failure](CHALLENGE.md#c1--hidden-behavior-and-type-assumptions), then [C2](CHALLENGE.md#c2--hidden-configuration-default) and [C3](CHALLENGE.md#c3--reproducibility-drift); [return to green](CHALLENGE.md#return-to-green).

Use [CHALLENGE.md](CHALLENGE.md#m0-failure-challenges) for the exact C1–C3 commands. For each failure:

1. Activate it.
2. Run the named check without reading the changed file.
3. Record the symptom and a hypothesis.
4. Inspect the smallest relevant area.
5. Repair the behavior and rerun the check.
6. Run `python3 scripts/challenge.py reset` to clear challenge state.
7. Run the complete green baseline before continuing.

### 5. Use the professional workflow `[REQUIRED]`

Start from Block 4 green with its result recorded. Work in `projects/catalog/`;
focus on `src/catalog_api/` and `tests/test_api.py` and the output named below. Record `evidence/M0/index.md`.
Stop when the Core gate, review, and release trail are evidenced.
Resume at [Block 5](#5-use-the-professional-workflow-required) using that saved result; continue to [Evidence](#evidence).
When needed: [why preserve change history](CONCEPTS.md#i-cannot-remember-what-i-changed-last-time) and [release evidence](ACCEPTANCE.md#a3--matching-automation-and-release-trail).

Only after the first green run:

1. Follow the [learner-owned repository setup](../../CONTRIBUTING.md), then open
   one M0 milestone issue from the GitHub issue template.
2. Create a branch: `git switch -c m0/engineering-baseline`.
3. Commit focused changes and push the branch.
4. Open a pull request using the repository template.
5. Confirm GitHub Actions runs the same Ruff, mypy, pytest, and curriculum checks.
6. Link `evidence/M0/index.md` and answer [REVIEW.md](REVIEW.md#m0-review).
7. Complete the [formal acceptance gate](ACCEPTANCE.md#core).
8. Ask a peer—or later use a clean solo context—to repeat one Core behavior and
   one failure using only repository instructions.
9. Merge the pull request, update `PROGRESS.md`, and create an annotated tag:

```bash
git tag -a m0-engineering-baseline -m "Pass M0 Engineering Baseline"
git push origin m0-engineering-baseline
```

## Failures and hints

Use the current scenario’s observation, boundary, and reference hints in order;
return to green before starting another fault. [C1 health/type](CHALLENGE.md#c1--hidden-behavior-and-type-assumptions), [C2 configuration](CHALLENGE.md#c2--hidden-configuration-default), and [C3 drift](CHALLENGE.md#c3--reproducibility-drift).

## Evidence

Record commands, predictions, observed failures, recovery, and limitations in
`projects/catalog/evidence/M0/index.md`. Answer [review prompts](REVIEW.md#m0-review) and prove the [Core gate](ACCEPTANCE.md#core).

## Done when

- The baseline works from a clean checkout using the documented commands.
- C1–C3 fail for the expected reason, are diagnosed, and return to green.
- Missing or malformed configuration fails safely.
- Local and GitHub checks agree.
- Your evidence links actual results and identifies limitations.
- A cold reviewer can repeat the representative path without your private notes.

## Recovery

Use the [catalog troubleshooting guide](../../projects/catalog/README.md#if-setup-fails),
reset any active fault, and rerun the complete baseline before advancing.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

## Next

Continue to [M1 — Production-minded API Foundation](../m1-production-api-foundation/README.md).

[Previous: Course start](../../README.md#start-now) · [Course home](../../README.md) · [Next milestone: M1](../m1-production-api-foundation/README.md)
