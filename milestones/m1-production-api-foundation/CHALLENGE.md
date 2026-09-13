# M1 challenges and hints

Run commands from `projects/catalog/`. Preserve failing output and a hypothesis
before inspecting implementation files.

## **C1 — The client contract is missing**

**PROVIDED** — the product brief and black-box contract are supplied; you build
the application behavior.

### Steps

1. Run the supplied contract and record the first 404 response.
2. Implement create, retrieve, list, replace, and retire one example at a time.
3. Rerun the complete contract and preserve the final green result.

Run:

```bash
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected initially: HTTP 404 failures. Implement create, retrieve, list,
replace, and retire behavior from the product brief one example at a time.

### Hints

1. Compare the first unexpected status with the request path.
2. Inspect `app.py` for route ownership and `models.py` for transport shape.
3. Use the FastAPI response-model and status-code references.

### Reset

Run `python3 scripts/challenge.py reset`, then rerun the supplied contract.

Evidence: request matrix, named tests, expected/actual responses, and the final
green contract run.

## **C2 — Invalid input must not corrupt valid state**

**YOU BUILD** — add focused invalid-input cases without changing the published
contract.

### Steps

1. Add one negative-price and one missing-replacement-field HTTP case.
2. Prove each rejection preserves the prior in-memory state.
3. Add ordered bounded-list cases and rerun the complete contract.

Run the replacement and invalid-input tests with `-vv`. Seed one negative price
or missing replacement field through HTTP; do not mutate the store directly.

Expected: HTTP 422 and the prior product remains unchanged. Then create products
in reverse order and prove listing remains ordered and bounded.

### Hints

1. Distinguish request-shape validation from a product rule.
2. Inspect when validation occurs relative to the in-memory write.
3. Use the Pydantic strictness and FastAPI validation references.

### Reset

Recreate the in-memory app fixture, then run
`PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q`.

## **C3 — A public field changes unexpectedly**

**PROVIDED** — activation changes the application response model while the
consumer contract remains unchanged. Never repair this by weakening the test.

### Steps

1. Activate compatibility and record the OpenAPI failure and affected client.
2. Preserve compatibility or document the authorized change and deprecation.
3. Reset the challenge and rerun the supplied contract.

After the M1 contract is green:

```bash
python3 scripts/challenge.py activate compatibility
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Expected: the OpenAPI compatibility test fails. Record the observed public
change and affected client before reading the changed file. Restore with:

```bash
python3 scripts/challenge.py reset
PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q
```

Use the requirements template for the archival-reason request. Record decision
owner, accepted behavior, rejected scope, and deprecation only if compatibility
cannot be preserved.

### Hints

1. Compare the changed OpenAPI property set with the documented client response.
2. Inspect the response model and compatibility assertion, not every route.
3. Use the OpenAPI specification link in `RESOURCES.md`; do not weaken the guard.

### Reset

Run `python3 scripts/challenge.py reset`, then rerun the supplied contract.
