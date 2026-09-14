# Review

Answer one question at a time in `evidence/M2/index.md`:

1. Which invariant belongs in application code, the database, or both?
2. Who opens, rolls back, and closes the session?
3. What duplication did normalization remove, and what query cost did it add?
4. Which query does each index serve, and what does it cost on writes?
5. What measured statement count proves the N+1 problem?
6. Why must migration tests include existing rows?
7. Does the failed-migration runbook restore a green state without hidden steps?
8. Is the backfill safe to restart? Show the observation.
9. What measurement—not `async def` syntax—would earn `AsyncSession`?
10. Does the reset command refuse a non-course database?
11. Which observed pressure earns each service or repository, and which simple path stays direct?

Trace one representative field with the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A5 gate): a career-shifter connects a prior-domain recordkeeping rule to a database invariant; a data specialist explains how strong SQL work still depends on API/session ownership and operational recovery.
