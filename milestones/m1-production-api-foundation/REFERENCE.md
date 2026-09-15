# M1 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M1 concepts through client problems

## “The client cannot predict the response”

**Example:** two identical create requests return different shapes. **Term — HTTP
contract:** the public agreement covering method, path, status, headers, and
body. **Rule:** publish examples first and test the complete observable response.

## “A repeat request created another effect”

**Example:** a network retry retires the same product twice. **Term — idempotent
operation:** repeating it has the same intended final effect as doing it once.
An HTTP safe method is different: it is intended only to read. **Rule:** declare
repeat behavior per operation and prove it at the API boundary.

## “The list changes between pages”

**Example:** a page has no stable last item. **Term — pagination:** returning a
bounded, ordered part of a collection. **Rule:** define total order, limit,
cursor meaning, and empty/final response before implementation.

## “Generated documentation hid a breaking change”

**Example:** a field rename still returns HTTP 200 but breaks a client. **Term —
compatibility check:** an automated comparison that detects an unintended public
contract change. **Rule:** use Pydantic for transport shape, named product logic
for invariants, and API/OpenAPI tests for observable drift. “Production-minded”
here means a predictable boundary, not persistence, security, or deployment.

### Tools earned here

- **FastAPI routing + generated OpenAPI:** express and inspect the contract; generated docs do not replace consumer examples.
- **FastAPI CLI/Uvicorn runtime:** serve the ASGI application with one documented development command and one no-reload production-shaped command; an application framework is not its own process manager or deployment platform.
- **Pydantic request/response models:** reject ambiguity at the edge; avoid reusing one model for create/update/read when semantics differ.
- **HTTPX + pytest:** API acceptance and rule-level tests; use doubles only for true boundaries.
- **Decimal:** represent money without binary floating-point corruption.

Keep the repository in memory so persistence cannot distract from HTTP reasoning. Implement stable ordering, limits, and pagination behavior before considering `fastapi-pagination`; the adapter must preserve rather than define the contract. Avoid SQLAlchemy, auth, a pagination library, and generic service/base classes. An earned typed client is Stretch only after semantic compatibility checks exist.

## Evaluate after evidence

Evaluate only the optional tools named in the tool guidance above, after the stated simpler baseline has failed. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates the current behavior, or creates a second application path.

## Sources

### Resources for M1

Open a reference only after the matching question appears. Reviewed 2026-09-13.

- [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110) — Which method, status, or header expresses this outcome? Applicable standard: RFC 9110.
- [FastAPI response status codes](https://fastapi.tiangolo.com/tutorial/response-status-code/) — How does the declared contract reach OpenAPI and the response? Applicable tool: current FastAPI docs.
- [FastAPI response models](https://fastapi.tiangolo.com/tutorial/response-model/) — Which declared output shape is filtered, documented, and validated? Applicable tool: current FastAPI docs.
- [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) — Where should input validation and output shape live? Applicable tool: Pydantic 2.
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html) — What makes an API change structurally compatible? Applicable standard: current OpenAPI specification.

Prefer the RFC for protocol meaning and framework documentation for implementation details.
