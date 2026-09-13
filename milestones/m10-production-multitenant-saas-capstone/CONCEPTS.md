# Problems and mental models

Tenant isolation is an invariant across direct IDs, lists/search, writes, reports, jobs, exports, caches, logs, and staff tools. Establish tenant context from authenticated membership, thread it through boundaries, scope every query/write, and add database defense where practical. Audit logs are append-oriented product records of who/tenant/action/target/time/correlation—not mutable diagnostic logs.

Observability connects structured logs, metrics, and traces to answer a concrete user-impact question. Request/correlation IDs bridge HTTP, database, and workers; redact secrets/tenant-sensitive data. Health says process alive; readiness says dependencies/migrations allow traffic. SLOs and alerts need actionable thresholds and runbooks.

CI validates; CD promotes the same immutable artifact. GitHub Actions is not CD merely because a workflow exists: promotion is earned only when a real target, environment-scoped secrets, migration ordering, readiness, and rollback/roll-forward are proven. Docker Compose can define a bounded single-host runtime but does not itself supply TLS, secret custody, backup, monitoring, or safe rollout. Migration deployment requires expand/contract compatibility, ordering, health gates, and rollback/roll-forward thinking. Secrets belong in platform controls. Backup existence is not recovery: restore into isolation, verify data/application integrity, and measure RPO/RTO.

Release and incident discipline includes reviewed evidence, versioning, notes, rollout/rollback, communication, blameless postmortem, and owned follow-ups. Sellable means onboarding, support, limits, data export/deletion, security posture, cost assumptions, and honest constraints—not a billing screen.
