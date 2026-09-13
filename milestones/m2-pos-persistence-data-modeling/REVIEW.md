# Review

Explain which invariants live in application, database, or both; the session/rollback lifecycle; normalization trade-offs; each index’s target query and write cost; how N+1 was observed; and why migration tests need existing rows.

Self-review raw SQL and generated migrations, constraint names/errors, lazy loads, connection cleanup, secrets, and destructive reset commands. Rehearse recovering C3 from only the runbook and identify whether the backfill is restartable.

Trace one representative field with the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Lens prompt (same A1–A5 gate): a career-shifter connects a prior-domain recordkeeping rule to a database invariant; a data specialist explains how strong SQL work still depends on API/session ownership and operational recovery.
