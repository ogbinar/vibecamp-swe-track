# M9 — Performance, Caching & Realtime using Social

**Capability:** improve critical paths from representative measurements without changing product semantics. **Deliverable:** create `projects/social/` with profiles, follows, posts, likes, cursor-paginated feed, and live notifications, then diagnose skewed realistic load.

Prerequisite: M8 measurement/correctness discipline. Sequence: declare workload/SLO → build database-first slice → capture baseline → repair N+1/query plans → earn or reject cache → compare realtime transports → break outage/reconnect paths → ship `m9-performance-social`.

Outputs: seeded workload generator, plans/query counts/percentiles, pagination guarantees, cache decision/evidence, realtime loss/reconnect policy, and regression budget.
