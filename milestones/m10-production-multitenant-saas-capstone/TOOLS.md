# Tools earned here

- **Docker + GitHub Actions:** CI builds and verifies one immutable artifact; CD promotes that exact digest only after a real target and the deployment gates are present.
- **Docker Compose:** reproduce local/integration environments and, if deliberately chosen, a documented single-host runtime; identify which platform/reverse-proxy controls provide TLS, restart, secrets, backup, monitoring, and rollback.
- **Platform secret/config controls:** separate values by environment; scan/redact outputs and support rotation.
- **Structured logs, metrics, traces:** start with redacted structured logs and correlation IDs. Add OpenTelemetry plus one owned backend for portable instrumentation, or choose Logfire/Sentry when one managed backend better fits the diagnostic need; do not require all three. Record propagation, sampling, retention, cost, and removal criteria.
- **PostgreSQL backup/restore and migration tools:** measured recovery and compatible rollout.
- **Synthetic tenant/security/load harnesses:** repeat isolation and operational drills safely.

Optional endorsements are evaluated one at a time after Core:

- **S3-compatible storage:** only for files that must outlive instances; bound
  tenant-safe keys, presigned expiry, authorization, type/size, checksum,
  retention/delete, partial failure, and orphan reconciliation.
- **OAuth/OIDC:** authorization code plus PKCE and OIDC validation only after an
  external identity need; own state/nonce, redirect allowlist, issuer/audience/
  signature/time/key rotation, linking, logout, and revocation assumptions.
- **Sentry or Logfire:** choose one for one named question; own redaction,
  sampling, retention, access, cost, and deletion, then retain or remove.
- **SQLAdmin:** only after tenant authorization and append-only audit are green;
  every action remains scoped, authorized, and audited.

Each defaults to do not add yet without need, owner, cost/data boundary, removal
trigger, access, and explicit authority. A real deployment is a separate optional
endorsement under the existing target prerequisites.

Prefer platform-managed TLS/secrets and state the boundary outside Compose. Kubernetes, service mesh, microservices, multiple databases, and elaborate deployment strategies remain excluded. Earn canary/blue-green only from measured rollout risk.

Revisit relevant [complexity rejection records](../../templates/COMPLEXITY-REJECTION.md) before adopting observability or deployment machinery; a production label is not evidence that the trigger fired.
