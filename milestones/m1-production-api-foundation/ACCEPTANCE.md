# M1 acceptance gate

Required maturity: **Level A plus selected Level B boundary engineering**. M1
makes no Level C claim.

## Core

### **A1 — Public HTTP behavior**

- [ ] Create returns HTTP 201, the product representation, and `Location`.
- [ ] Retrieve distinguishes a known product from a missing product.
- [ ] Full replacement rejects missing fields without changing stored state.
- [ ] Repeated retirement has the same intended effect and representation.
- [ ] API evidence names the exact contract tests and sanitized responses.

### **A2 — Validation and pagination**

- [ ] Negative price, invalid money precision, blank identity, and oversized limit fail deliberately.
- [ ] Errors use the published envelope instead of an unhandled 500.
- [ ] Listing is ordered by SKU and bounded to 1–100 results.
- [ ] Empty and final pages return `next: null`.
- [ ] Unit tests isolate only rules that become clearer outside HTTP.

### **A3 — Compatibility and changed requirements**

- [ ] The OpenAPI comparison fails when a required product field changes.
- [ ] C3 preserves the failing observation, hypothesis, reset, and regression proof.
- [ ] The archival-reason brief records decision owner and accepted/rejected scope.
- [ ] Release notes describe any unavoidable compatibility break and deprecation.

### **A4 — Honest operation**

- [ ] M0 and M1 checks pass from a clean copy with locked dependencies.
- [ ] Development and no-reload commands serve the same tested contract.
- [ ] Documentation states that state is volatile and security/deployment/recovery are absent.
- [ ] GitHub Actions runs the locked baseline and collects the opt-in M1 contract.
- [ ] A cold reviewer repeats one success, one error, and one retry from the docs.

Record command, environment, expected result, actual result, interpretation, and
limitation. A screenshot alone is not evidence.

## Execution map

Checklist bullets under each A ID are local steps in written order. Run from
`projects/catalog/`: A1–A3 use
`PYTHONPATH=src uv run --locked pytest contracts/test_m1_contract.py -q`; A4 uses
`uv run --locked ruff check . && uv run --locked ruff format --check . && uv run --locked mypy && uv run --locked pytest`.
Expected: named behavior and regressions are green. Record results under the
matching A heading in `evidence/M1/index.md`; recover with
`python3 scripts/challenge.py reset` and rerun the last green command.

## Stretch

Add ETag conditional replacement or a tiny typed client only after Core. Tests
must preserve the established public contract.

## Review

### Review

Answer one question at a time in `evidence/M1/index.md`:

1. How is an HTTP safe method different from an idempotent operation?
2. Which invalid input is rejected by transport validation?
3. Which invalid input is rejected by a product invariant?
4. What exact order makes pagination stable?
5. Which public breaking change could internal unit tests miss?
6. Why is this API production-minded but not production-ready?
7. For each endpoint, what happens on success, unknown identity, and repeat?
8. Which test could falsely pass, and which controlled defect proves it can fail?
9. Which persistence or authentication idea did you defer, and why?
