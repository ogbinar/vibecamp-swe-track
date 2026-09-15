# M0 reference

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

Use [the glossary](../../GLOSSARY.md) for quick recall.

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
