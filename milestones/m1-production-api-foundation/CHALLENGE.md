# Challenge brief

- **C1 — Ambiguous contract:** Resolve requirements for create/get/list/update/retire. Send malformed JSON, unsupported fields, missing resources, repeated mutations, and boundary pages. Repair status/header/body and pagination semantics; capture a request matrix.
- **C2 — Validation and compatibility:** Seed negative/binary-float prices, duplicate identity, oversized limits, state leakage between tests, and a renamed response field. Locate whether transport, domain, or contract is responsible; add unit/API/OpenAPI regression evidence.
- **C3 — Stakeholder change to an existing API:** Use the [requirements brief](../../templates/REQUIREMENTS.md) for a request to add product archival reason. Record affected roles, decision owner, conflicting compatibility need, accepted interpretation, and rejected scope. Characterize current behavior first, implement the smallest compatible change, and document deprecation if compatibility is impossible.

Operate by correlating sanitized requests with stable errors; ship release notes that state behavior and limitations.
