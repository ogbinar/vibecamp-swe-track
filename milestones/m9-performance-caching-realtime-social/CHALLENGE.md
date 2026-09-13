# Challenge brief

- **C1 — Slow feed incident:** Seed skewed high-fan-out data, N+1 loading, missing/misleading indexes, and offset pagination drift. Baseline, inspect SQL/query plans, optimize, and prove cursor pages have no duplicate/omission during insertion.
- **C2 — Cache correctness:** Implement a narrow Redis cache-aside experiment only after a missed target. Seed stale deleted/private items, missed invalidation, stampede, Redis outage, and cross-user key collision; repair or remove cache based on equal-harness results.
- **C3 — Realtime mismatch:** Compare polling, SSE, and WebSockets for one-way notifications. Exercise disconnect/reconnect, process restart, gaps, malformed events, and slow consumers; retain the smallest transport meeting stated semantics.

Operate via database/cache/connection signals and a repeatable load run. Ship before/after evidence without cherry-picking.
