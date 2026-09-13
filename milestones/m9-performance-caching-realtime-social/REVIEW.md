# Review

Explain why workload is representative; which plan observation drove the fix; N+1 detection; index write trade-off; cursor correctness; cache-aside consistency/invalidation/outage; and SSE versus WebSocket choice/replay limits.

Self-review tiny/unskewed data, benchmark drift, omitted errors, warmed-only claims, cross-user cache keys, Redis becoming a truth store, stale authorization, stampedes, unbounded live buffers, and semantic changes disguised as optimization. If async database access is proposed, identify the measured synchronous bottleneck and compare equal workload, pool, errors, and operability—not syntax.

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to test whether deletion/privacy changes reach cache and live copies. Lens prompt (same A1–A4 gate): a career-shifter explains the performance trade-off in user-impact language; a data specialist connects query-plan skill to cache correctness, API pagination, and live-operation limits.
