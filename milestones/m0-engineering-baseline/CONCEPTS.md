# M0 concepts through problems

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
