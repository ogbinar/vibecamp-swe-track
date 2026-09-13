# M1 concepts through client problems

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
