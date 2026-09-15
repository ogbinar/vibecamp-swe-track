# Synthetic M0 evidence example

> **Reference only:** this is fabricated demonstration data, not learner work
> and not proof that your environment passed. Replace it with your own results.

## Claim and environment

Claim: the supplied catalog responds through HTTP and rejects absent required
configuration. Example environment: Linux, Python 3.13, uv 0.9.21.

## Green behavior

Command: `uv run --locked pytest`

Expected: exit code 0 and eight passing tests. Example actual result: exit code
0; `8 passed`. Interpretation: the checked HTML, API, form, and configuration examples pass;
this does not prove production readiness or behavior that has no test.

## Failure, diagnosis, and regression proof

Command: `python3 scripts/challenge.py activate health`, followed by
`uv run --locked pytest tests/test_api.py::test_health_reports_liveness`.

Expected: the health assertion fails. Example actual result: response field
`status` was `warning`, not `ok`. Initial hypothesis: the endpoint constructs
the wrong response value. Diagnosis: the bounded fault changed the literal in
`src/catalog_api/app.py`; routing and serialization still worked.

Recovery: `python3 scripts/challenge.py reset`, then rerun the narrow test and
the full test suite. Example actual result: both exited 0. This is regression
proof for the demonstrated fault, not proof against every health-check defect.

## Limitations

- No database, authentication, deployment, load, or dependency-readiness check exists in M0.
- Timings and output above are examples and must not be copied as personal evidence.
- A cold reviewer still needs to repeat one behavior and one failure.
