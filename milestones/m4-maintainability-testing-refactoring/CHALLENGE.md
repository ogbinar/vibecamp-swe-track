# M4 challenge brief

Run from `projects/pos/`. Preserve behavior before restructuring code.

## **C1 — Stakeholder-driven technical-debt change**

**PROVIDED** — the fixed cashier-name change brief is supplied.

### Steps

1. Record decision owner, compatibility need, accepted behavior, and rejected scope.
2. Create `tests/m4/test_characterization.py`; count files touched by the awkward change.
3. Run README Blocks 1–2 and keep behavior change separate from refactoring.

### Hints

1. List observable behavior before judging structure.
2. Inspect each route, model, query, and serializer touched by cashier name.
3. Use the pytest characterization link in `REFERENCE.md`.

### Reset

Stash only the current learner edit, then run
`uv run --locked pytest tests/m4/test_characterization.py -q`.

## **C2 — Duplicated database behavior**

**YOU BUILD** — localize only the duplication the change exposes.

### Steps

1. Record repeated session, transaction, and query behavior.
2. Add the smallest service/repository or injected dependency that reduces scatter.
3. Run `uv run --locked pytest tests/m4/test_cashier_name.py -q` and compare counts.

### Hints

1. Ask which behavior changes together instead of applying a layer template.
2. Inspect transaction ownership and repeated data access.
3. Use the dependency-injection link in `REFERENCE.md`; reject pass-through layers.

### Reset

Remove the proposed boundary while keeping characterization tests, then rerun
`uv run --locked pytest tests/m4/test_cashier_name.py -q`.

## **C3 — False-confidence tests**

**YOU BUILD** — create a reversible test or dependency-boundary mutation.

### Steps

1. Show one mock-heavy test staying green while a mapping or route is broken.
2. Replace it with the owning integration/API test; create `tests/m4/test_architecture.py`.
3. Add one forbidden import, observe failure, restore it, and rerun Block 3.

### Hints

1. Name the real boundary the test never crossed.
2. Inspect serialization, mappings, dependency direction, and fixture realism.
3. Use the testing-boundaries link in `REFERENCE.md`.

### Reset

Remove the forbidden import and run `uv run --locked pytest tests/m4/test_architecture.py -q`.

Complete one [complexity rejection record](../../templates/COMPLEXITY-REJECTION.md)
with a measurable revisit trigger.
