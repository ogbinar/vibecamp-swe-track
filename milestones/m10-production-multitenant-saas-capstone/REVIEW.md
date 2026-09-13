# Review

Answer one question at a time in `evidence/M10/index.md`:

1. How is tenant context established from membership?
2. Which boundary enforces that tenant context?
3. How is an audit record different from a diagnostic log?
4. Where does continuous integration (CI) end and continuous deployment (CD) begin?
5. What exact digest was built, approved, and deployed?
6. Which TLS, secret, monitoring, backup, and rollback controls exist outside Compose?
7. Which expand/contract step is backward compatible?
8. When is rollback unsafe and roll-forward required?
9. How is a synthetic secret rotated without logging it?
10. Which user question does each log, metric, and trace answer?
11. What RPO and RTO were measured during isolated restore?
12. What does a buyer or operator need before trusting this product?
13. What is the biggest remaining blocker to real-money use?

Trace a deleted tenant through primary rows, audit exceptions, exports, logs, jobs/caches, and restored backups using the [data-lifecycle template](../../templates/DATA-LIFECYCLE.md). Cold-review the final portfolio reader path. Lens prompt (same A1–A7 gate): a career-shifter translates domain/support judgment into incident and release decisions; a data specialist demonstrates ownership beyond storage—tenant-safe APIs, deployment, observability, recovery, and customer communication.
