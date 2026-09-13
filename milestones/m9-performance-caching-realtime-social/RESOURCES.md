# Resource guide

Use current PostgreSQL primary docs for `EXPLAIN`, statistics, indexes, and monitoring; Redis primary docs for expiration/transactions/client failure; protocol or official framework docs for SSE and WebSockets; and primary load-tool docs for measurement limitations.

Prefer sources that expose trade-offs and failure semantics. Reject latency claims without workload/environment and cache guidance that omits invalidation/privacy/outage. Record pinned versions and reproduce examples on realistic seeded data.
