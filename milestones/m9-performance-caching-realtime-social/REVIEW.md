# Review

Answer one question at a time in `evidence/M9/index.md`:

1. Why does the dataset and request mix represent the fixed feed?
2. Which query-plan observation drove the database change?
3. What statement count detects N+1?
4. What write/storage cost does the index add?
5. How does the cursor prevent duplicates and omissions during insertion?
6. What remains authoritative while Redis is available or down?
7. How are invalidation, wrong-user keys, stampede, and stale authorization tested?
8. Why does the fixed requirement choose SSE instead of WebSockets?
9. What happens after reconnect, restart, gap, or a slow consumer?
10. Did the optimization change visible feed semantics?
11. If async access is proposed, what measured synchronous bottleneck earns it?

Use the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md) to test whether deletion/privacy changes reach cache and live copies. Lens prompt (same A1–A4 gate): a career-shifter explains the performance trade-off in user-impact language; a data specialist connects query-plan skill to cache correctness, API pagination, and live-operation limits.
