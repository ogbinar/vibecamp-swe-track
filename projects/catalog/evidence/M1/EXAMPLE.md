# Synthetic M1 evidence example

> Reference only: these example observations are not learner evidence.

Claim: a repeated retirement request has the same intended effect as the first.
The opt-in contract test initially returned HTTP 404 because the route did not
exist. The hypothesis was “retirement behavior has not been implemented,” not
“FastAPI is broken.” After implementation, the named test passed twice against
one fresh application instance. The full M0 suite also remained green.

Limitation: this proves the in-memory HTTP contract only. It does not prove
persistence, multi-process consistency, authentication, or production recovery.
