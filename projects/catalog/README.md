# M0 catalog starter

This is the smallest working application used by
[M0 — Engineering Baseline](../../milestones/m0-engineering-baseline/README.md).
It is intentionally incomplete: you will break, diagnose, improve, and ship it.

## Run the green baseline

From this directory:

```bash
cp .env.example .env
uv sync --locked
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked mypy
uv run --locked pytest
```

Every check should exit with code `0`; pytest should report six passing tests.

Start the development server:

```bash
uv run --locked fastapi dev src/catalog_api/main.py --port 8000
```

In another terminal:

```bash
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/products/sample
curl -i http://127.0.0.1:8000/
```

Expect HTTP `200`; the first two responses are JSON and `/` is an Air-rendered
HTML catalog containing the same sample product. Stop the server
with `Ctrl+C`. The production-shaped, no-reload command used later in M0 is:

```bash
uv run --locked fastapi run src/catalog_api/main.py --port 8000
```

## Safe challenge control

Only activate a challenge when the M0 lesson asks. The default branch is green.

```bash
python3 scripts/challenge.py activate health
python3 scripts/challenge.py status
python3 scripts/challenge.py reset
```

Available names are `health`, `type`, `config`, and `automation`. Only one can
be active. Activation changes one bounded file and writes an ignored state file.
Reset is repeatable and refuses to overwrite an unrecognized edit.
Use `python3`, not `uv run`, for challenge control: the `automation` scenario
deliberately makes the project incompatible with its selected Python version.

## Begin M1 after passing M0

Read the [M1 product brief](specs/M1-PRODUCT-BRIEF.md), then expose the opt-in
contract tests:

```bash
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected at the start of M1: failures beginning with HTTP `404`, because the
product routes are intentionally absent. Implement the public behavior without
editing the contract tests. Keep `uv run --locked pytest` green throughout; it
protects M0 behavior.

After the contract passes, activate the compatibility fault:

```bash
python3 scripts/challenge.py activate compatibility
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
python3 scripts/challenge.py reset
```

Expected: the OpenAPI field check fails, then returns to green after reset.

## If setup fails

- `uv: command not found`: install uv using its official instructions, then
  reopen the terminal.
- Python mismatch: run `uv python install 3.13`, then repeat `uv sync --locked`.
- Lock mismatch: do not update the lockfile during setup; run `git status` and
  reset an active `automation` challenge.
- Missing `CATALOG_SERVICE_NAME`: copy `.env.example` to `.env` from this folder.
- Port 8000 is occupied: stop the old process or use `--port 8001` consistently
  in both the server and `curl` commands.
- Import failure: confirm `pwd` ends in `projects/catalog` and use the exact
  commands above.
- A check fails: run that command without `-q`, read the first error, and compare
  it with `git status`. Do not delete the environment as a first response.
- M1 state leaks between tests: create the FastAPI application and in-memory
  store inside a fixture rather than as shared module state.
- M1 returns an unexpected `500`: run the narrow failing test with `-vv`, read
  the first application traceback, and compare it with the published error shape.
- Invalid JSON behaves differently: send the exact request from the product
  brief before changing the contract.
- Compatibility challenge is stale: run `python3 scripts/challenge.py status`,
  then reset before switching branches or updating dependencies.
