# M0 failure challenges

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
3. Use the pytest or mypy link in `REFERENCE.md`; keep the repair your own.

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
3. Use the Pydantic settings link in `REFERENCE.md`.

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
3. Use the uv project link in `REFERENCE.md`.

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
