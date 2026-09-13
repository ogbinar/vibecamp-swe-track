# Tools earned here

- **Docker/Compose + GitHub Actions CI/CD:** build and promote one immutable artifact; use a simple non-production target.
- **Platform secret/config controls:** separate values by environment; scan/redact outputs and support rotation.
- **Structured logs, metrics, traces:** OpenTelemetry with one simple backend, or Logfire/Sentry when justified by diagnostic need, data policy, retention, cost, and removal criteria.
- **PostgreSQL backup/restore and migration tools:** measured recovery and compatible rollout.
- **Synthetic tenant/security/load harnesses:** repeat isolation and operational drills safely.

Prefer platform-managed TLS/secrets. Kubernetes, service mesh, microservices, multiple databases, and elaborate deployment strategies remain excluded. Earn canary/blue-green only from measured rollout risk.

Revisit relevant [complexity rejection records](../../templates/COMPLEXITY-REJECTION.md) before adopting observability or deployment machinery; a production label is not evidence that the trigger fired.
