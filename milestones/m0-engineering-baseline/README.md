# M0 — Make the catalog easy to run

[Course home](../../README.md) / M0

**Milestone 1 of 11 · M0**

## Business problem

An application that works only on its author's machine is not reproducible.
Your first job is to make one small application start, test, fail, and recover
the same way for another person and in GitHub Actions.

You are given a **walking skeleton**: the smallest end-to-end application that
handles a real request and has a real test. You will not design a database or
large architecture here. You will expose hidden assumptions and make the setup
repeatable.

## Product objective

- **Product can:** show one useful catalog page while keeping health and product JSON stable.
- **You will prove:** a green baseline, one diagnosed/reset failure, and matching automation evidence.

## Start here

- **Gate:** [A1–A3 plus A0 diagnostic / Level A](#core).
- **Repository support:** supplied starter locally verified; your learner gate needs your own evidence. [Dated scope and limits](../../docs/maintainers/usability.md#readiness-status-vocabulary)
separate local structure/starter checks from pending hosted and human evidence.
- **Resume:** open [PROGRESS](../../PROGRESS.md#active-milestone-dashboard), run the
[starting checks](../../projects/catalog/README.md#run-the-green-baseline), then return to the saved block; first visit: [Block 1](#1-run-the-supplied-baseline-required).

On resume, preserve your existing `.env` and evidence. Use the validation
commands from the starting checks; first-install copy and destructive reset
steps are not routine resume actions. If a check fails, use Recovery first.

## Build

### 1. Run the supplied baseline `[REQUIRED]`

- **Do:** start from the checkpoint above; work in `projects/catalog/` on the
  supplied `src/catalog_api/` and `tests/test_api.py`, then run the commands below.
- **Understand:** a reproducible baseline is the last-green state that makes a
  later failure diagnostic meaningful. Use [what the checks do](#m0-tools-and-why-they-are-here)
  and [tool references](#m0-resources) only when that question appears.
- **Check:** all baseline checks and all three HTTP responses pass; record the exact
  commands and observations in `evidence/M0/index.md`.
- **If it fails:** do not activate a fault. Use the targeted troubleshooting
  route below, preserve `.env` and evidence, and return to the narrowest red command.
- **Stop/resume:** stop with the green transcript saved. Resume at
  [Block 1](#1-run-the-supplied-baseline-required) from that result, then continue to Block 2.

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

Expected: every command exits with code `0`; pytest reports six passing tests.
If not, use the [starter troubleshooting guide](../../projects/catalog/README.md#if-setup-fails).

Start the application:

```bash
uv run --locked fastapi dev src/catalog_api/main.py --port 8000
```

In another terminal, still inside `projects/catalog/`:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/products/sample
curl -i http://127.0.0.1:8000/
```

Expected: all three responses start with HTTP `200`; the first two contain JSON,
and `/` contains the Air-rendered catalog page. Stop the server with `Ctrl+C`.

### 2. Understand the starting path `[REQUIRED]`

Start from Block 1 green with its result recorded. Work in `projects/catalog/`;
focus on `src/catalog_api/main.py` and the output named below. Record `evidence/M0/index.md`.
Stop when the request-path explanation is recorded.
Resume at [Block 2](#2-understand-the-starting-path-required) using that saved result; continue to Block 3.
When needed: [trace the HTTP path](#the-app-started-but-can-it-answer).

Read [the HTTP path](#the-app-started-but-can-it-answer) and inspect only these files first:

- `pyproject.toml` declares the project and checks.
- `uv.lock` records exact resolved dependency versions.
- `src/catalog_api/main.py` composes one Air/FastAPI process entry point.
- `src/catalog_api/web.py` defines the supplied catalog page route.
- `src/catalog_api/app.py` defines the FastAPI backend endpoints.
- `src/catalog_api/models.py` defines the supplied public response shape.
- `src/catalog_api/settings.py` validates configuration.
- `tests/test_api.py` checks behavior through HTTP.

Draw both paths—`browser → Air page → shared product behavior → HTML` and
`client → FastAPI endpoint → the same product behavior → JSON`—in your evidence
notes. Explain each arrow and why neither handler calls the other over HTTP.

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
When needed: [C1 first failure](#c1--hidden-behavior-and-type-assumptions), then [C2](#c2--hidden-configuration-default) and [C3](#c3--reproducibility-drift); [return to green](#return-to-green).

Use the [challenge brief](#challenge-brief) for the exact C1–C3 commands. For each failure:

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
Resume at [Block 5](#5-use-the-professional-workflow-required) using that saved result; continue to [Prove it](#prove-it).
When needed: [why preserve change history](#i-cannot-remember-what-i-changed-last-time) and [release evidence](#a3--matching-automation-and-release-trail).

Only after the first green run:

1. Follow the [learner-owned repository setup](../../CONTRIBUTING.md), then open
   one M0 milestone issue from the GitHub issue template.
2. Create a branch: `git switch -c m0/engineering-baseline`.
3. Commit focused changes and push the branch.
4. Open a pull request using the repository template.
5. Confirm GitHub Actions runs the same Ruff, mypy, pytest, and curriculum checks.
6. Link `evidence/M0/index.md` and answer [review prompts](#m0-review).
7. Complete the [formal acceptance gate](#core).
8. Ask a peer—or later use a clean solo context—to repeat one Core behavior and
   one failure using only repository instructions.
9. Merge the pull request, update `PROGRESS.md`, and create an annotated tag:

```bash
git tag -a m0-engineering-baseline -m "Pass M0 Engineering Baseline"
git push origin m0-engineering-baseline
```

## Understand

- **Walking skeleton:** the smallest working end-to-end application.
- **Reproducible:** another machine can rebuild and verify the same state.
- **CI (continuous integration):** checks GitHub runs for a proposed change.
- **Evidence:** a reproducible result supporting an engineering claim.
- **Cold review:** replay from clean instructions without the author's memory.

By the end of M0, `projects/catalog/` will have:

- A working health endpoint and one typed product response
- Locked dependencies and validated configuration
- Ruff, mypy, pytest, and API checks
- Safe, repeatable failure exercises
- GitHub continuous integration (CI)
- An issue, pull request, evidence index, and annotated `m0-engineering-baseline` tag

Terms such as endpoint, lockfile, linting, static type checking, evidence, and
cold review are defined in the [learner glossary](../../docs/reference/glossary.md).

The supplied walking skeleton serves health and one typed product response. Keep database and architecture work for later milestones.

## Use a tool if earned

Use uv, Ruff, mypy, pytest, Air, and FastAPI for the concrete checks above.
Evaluate an extra command wrapper only after repeated command drift; see the
[tool decision](#evaluate-after-evidence).

## Prove it

Use the current scenario’s observation, boundary, and reference hints in order;
return to green before starting another fault. [C1 health/type](#c1--hidden-behavior-and-type-assumptions), [C2 configuration](#c2--hidden-configuration-default), and [C3 drift](#c3--reproducibility-drift).

Record commands, predictions, observed failures, recovery, and limitations in
`projects/catalog/evidence/M0/index.md`. Answer [review prompts](#m0-review) and prove the [Core gate](#core).

## Done / next

- The baseline works from a clean checkout using the documented commands.
- C1–C3 fail for the expected reason, are diagnosed, and return to green.
- Missing or malformed configuration fails safely.
- Local and GitHub checks agree.
- Your evidence links actual results and identifies limitations.
- A cold reviewer can repeat the representative path without your private notes.

### Recovery

Use the [catalog troubleshooting guide](../../projects/catalog/README.md#if-setup-fails),
reset any active fault, and rerun the complete baseline before advancing.

After the local hints and recovery, optional [learner help](../../.github/ISSUE_TEMPLATE/help.yml)
asks for the block, failing command, expected/actual result, last green reference,
and redacted evidence. In your repository, choose Issues → New issue → Learner help.
The same Core gate applies; no extra technical content is withheld.

Continue to [M1 — Production-minded API Foundation](../m1-production-api-foundation/README.md).

[Previous: Course start](../../README.md#start-now) · [Course home](../../README.md) · [Next milestone: M1](../m1-production-api-foundation/README.md)


---

## Challenge brief

The starter is green by default. A small script safely changes one known file
to create a deterministic symptom. Do not inspect the script or changed file
until you have run the named check and recorded a hypothesis.

Run all commands from `projects/catalog/`. Only one challenge may be active.

## **C1 — Hidden behavior and type assumptions**

**PROVIDED** — activate the named health or type fault and reset it afterward.

### Steps

1. Activate health, record the failing test and one hypothesis, then repair/reset.
2. Activate type, record the mypy error and one hypothesis, then repair/reset.
3. Run the complete Return to green block before continuing.

### Health behavior

```bash
python3 scripts/challenge.py activate health
uv run --locked pytest
```

Expected: one health test fails. Record expected versus actual behavior, then
locate and repair the smallest cause. After the test passes:

```bash
python3 scripts/challenge.py reset
```

### Type mismatch

```bash
python3 scripts/challenge.py activate type
uv run --locked mypy
```

Expected: mypy reports an incompatible product-price type. Record why ordinary
runtime validation could hide this mistake, repair it, and reset.

### Hints

1. Read the first pytest or mypy failure and name the expected behavior or type.
2. Inspect only the reported application file and its owning test.
3. Use the pytest or mypy link in the Reference section below; keep the repair your own.

### Reset

Run `python3 scripts/challenge.py reset`, then `uv run --locked pytest` and
`uv run --locked mypy`.

## **C2 — Hidden configuration default**

**PROVIDED** — activate the configuration fault and reset it afterward.

### Steps

1. Activate config and record why missing input unexpectedly succeeds.
2. Repair and reset, then try one invalid synthetic `.env` value.
3. Restore `.env` and run the complete Return to green block.

```bash
python3 scripts/challenge.py activate config
uv run --locked pytest
```

Expected: configuration tests show that missing input no longer fails. Repair
the required setting without printing its value, rerun the tests, and reset.
Then temporarily replace `CATALOG_ENVIRONMENT=development` in `.env` with an
invalid value. Starting the server must fail with a useful validation error.
Restore `.env`; it is local and must remain ignored.

### Hints

1. Compare the missing or invalid input with the setting’s declared requirement.
2. Inspect the Pydantic settings model and `.env.example`, not unrelated routes.
3. Use the Pydantic settings link in the Reference section below.

### Reset

Run `python3 scripts/challenge.py reset`, restore the synthetic `.env` value,
then run `uv run --locked pytest`.

## **C3 — Reproducibility drift**

**PROVIDED** — activate the automation fault and reset it afterward.

### Steps

1. Activate automation and record uv’s first version disagreement.
2. Explain which file owns each version claim, then repair and reset.
3. Run `uv sync --locked` and the complete Return to green block.

```bash
python3 scripts/challenge.py activate automation
uv sync --locked
```

Expected: uv rejects a disagreement between the pinned Python version and
project requirement. Explain which file owns each claim and repair the mismatch.
Use system Python to reset because the project environment is deliberately
invalid:

```bash
python3 scripts/challenge.py reset
uv sync --locked
```

### Hints

1. Identify which Python-version claim uv says disagrees.
2. Inspect `.python-version`, `pyproject.toml`, and the lock metadata only.
3. Use the uv project link in the Reference section below.

### Reset

Run `python3 scripts/challenge.py reset`, then `uv sync --locked`.

## Return to green

After every challenge:

```bash
python3 scripts/challenge.py status
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
git status --short --ignored
```

Expected: no challenge is active; all checks pass; `.env`, `.venv`, caches, and
challenge state are ignored. Preserve the sanitized failing output, hypothesis,
diagnosis, and regression proof in `evidence/M0/index.md`. Do not retain the
defect in the working application.


---

## Acceptance gate

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


---

## Reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M0 concepts through problems

## “It works on my machine”

If another person cannot recreate your environment, hidden local state is part
of the system. Record the Python version, direct dependencies, exact resolved
versions, configuration names, startup command, and ignored generated files.

A **lockfile** records exact resolved dependency versions. It makes dependency
installation repeatable; it does not guarantee that every operating system is
identical or that every dependency is secure.

## “The app started, but can it answer?”

A **walking skeleton** is the smallest end-to-end application that exercises a
real path. Here the path begins with an HTTP request, reaches a FastAPI
**endpoint** (a method and URL path), validates a Pydantic response, and returns
HTTP status, headers, and JSON.

The `/health` endpoint proves **liveness**: the process can answer. It does not
prove database or external-service **readiness**; those dependencies do not
exist in M0.

## “The setting existed only in my terminal”

**Configuration** is input supplied outside the code. Validate it when the
application starts, list safe setting names in `.env.example`, and never commit
secret values. A concise startup failure is better than silently using an unsafe
default.

## “The code looks fine, but the change is wrong”

Ruff finds selected source problems and enforces formatting. Mypy performs
**static type checking**: it compares type annotations without running the
normal application. Pytest executes behavior. HTTPX sends requests through the
public API boundary. These checks answer different questions, so one does not
replace the others.

## “I cannot remember what I changed last time”

Git commits preserve changes. An issue states the problem; a pull request (PR)
explains and reviews a proposed solution; continuous integration (CI) repeats
checks; evidence supports the completion claim; an annotated tag names the
reviewed milestone state.

Use [the glossary](../../docs/reference/glossary.md) for quick recall.

### M0 tools and why they are here

- **uv** installs the pinned Python dependencies and runs commands in the
  project environment. `uv.lock` makes the resolved versions repeatable.
- **FastAPI and Uvicorn** define the API and run the ASGI server process.
- **Pydantic and pydantic-settings** define response shapes and validate
  configuration at startup.
- **pytest and HTTPX** execute behavior through the HTTP boundary.
- **Ruff** checks source rules and formatting. **Mypy** separately checks type
  annotations across files.
- **Git and GitHub** preserve change history and review. **GitHub Actions**
  repeats the same checks in continuous integration (CI).

M0 deliberately has no PostgreSQL, Docker, authentication, task runner,
service/repository layer, frontend, or deployment platform. Adding them would
hide the reproducibility problem under unrelated setup. Use one supported
Python version; a version matrix is earned only when compatibility is claimed.

## Evaluate after evidence

Evaluate only the optional tools named in the tool guidance above, after the stated simpler baseline has failed. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates the current behavior, or creates a second application path.

## Sources

### M0 resources

These are references for a specific question, not required reading before you
run the starter.

- [uv installation](https://docs.astral.sh/uv/getting-started/installation/):
  use only if the `uv` command is unavailable.
- [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/):
  use when `pyproject.toml`, `uv.lock`, and `--locked` behavior are unclear.
- [FastAPI first steps](https://fastapi.tiangolo.com/tutorial/first-steps/):
  use to understand the app instance, endpoint, server command, and generated docs.
- [FastAPI async tests](https://fastapi.tiangolo.com/advanced/async-tests/):
  use when tracing HTTPX requests through the in-memory ASGI application.
- [Pydantic settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/):
  use when tracing environment variables and startup validation.
- [Ruff tutorial](https://docs.astral.sh/ruff/tutorial/): use when a lint or
  formatting result is unfamiliar.
- [Mypy getting started](https://mypy.readthedocs.io/en/stable/getting_started.html):
  use when a type-check result differs from runtime behavior.
- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html):
  use when reading a failure or selecting a narrow test.
- [GitHub Actions for Python](https://docs.github.com/en/actions/tutorials/build-and-test-code/python):
  use when comparing local commands with continuous integration.

Prefer these version-current primary sources over copied tutorials. Record the
question answered; do not collect links without using them.
