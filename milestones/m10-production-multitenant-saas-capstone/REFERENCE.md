# M10 reference

This file preserves the concepts, tool decisions, and primary sources that support the learner route. Open only the section named by the active block.

## Use now

### M10 concepts through operating failures

## “North saw South’s receipt”

**Example:** one list query omitted tenant scope. **Term — tenant isolation:**
every data path keeps customer organizations separate. **Rule:** derive tenant
from membership and attack IDs, lists, writes, exports, support, and audit paths.

## “A backup existed but would not restore”

**Example:** an untested dump is unusable during an incident. **Term — recovery
time objective (RTO):** target time to restore acceptable service. **Rule:**
restore into isolation, verify product and tenant invariants, and measure actual
RPO/RTO.

## “Support tooling bypassed tenant scope”

**Example:** an admin export reads every organization. **Term — tenant context:**
the trusted customer boundary derived from authenticated membership. **Rule:**
carry it through IDs, lists, writes, jobs, exports, caches, logs, and support tools;
audit actor, tenant, action, target, time, and correlation.

## “Health was green while the database was unusable”

**Example:** the process answers but migrations are missing. **Term — readiness:**
whether dependencies and state permit traffic. **Rule:** keep liveness separate;
use logs, metrics, and traces to answer one user-impact question and link alerts to runbooks.

## “Production rebuilt a different image”

**Example:** deployment installs from source after CI passes. **Term — immutable
artifact:** one identified image promoted unchanged. **Rule:** continuous
integration (CI) validates; continuous delivery/deployment (CD) promotes the same
digest after migration, readiness, and rollback/roll-forward gates.

## “Compose started, so the team called it production-ready”

**Example:** no TLS, secret custody, monitoring, or tested restore exists. **Term —
bounded deployment:** a deliberately limited target with named controls and
limitations. **Rule:** test each required control; a backup counts only after an
isolated restore and integrity verification.

## “The incident ended but nobody learned from it”

**Example:** recovery has no timeline or owned follow-up. **Term — blameless
postmortem:** an evidence-based review of impact, detection, conditions, response,
and prevention. **Rule:** pair release notes and recovery evidence with onboarding,
support, export/deletion, costs, security posture, and honest limitations.

### Tools earned here

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

## Evaluate after evidence

Evaluate optional tools only after the stated simpler baseline fails. Record the observed need, operating cost, owner, and removal condition.

## Do not add yet

Do not add a tool that solves a later milestone, duplicates current behavior, or creates a second application path.

## Sources

### Resources for M10

Use these to answer a capstone operational question, not to expand the stack. Reviewed 2026-09-14.

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) — What is backed up, restored, and actually tested? Applicable tool: current PostgreSQL.
- [GitHub deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — Where do approvals, secrets, and deployment history belong? Applicable platform: GitHub Actions.
- [Amazon S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) — Optional: what bearer scope, expiry, and checksum controls bound direct object access?
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html) — Optional: why authorization code with PKCE, and why not the resource-owner password grant? Applicable standard: RFC 9700.
- [Logfire FastAPI](https://pydantic.dev/docs/logfire/integrations/web-frameworks/fastapi/) — Optional example: does one backend answer the named diagnostic question under the declared data/cost boundary? Compare Sentry or SQLAdmin only after its separate trigger fires.

Managed tools such as Logfire or Sentry are optional adapters after telemetry questions are explicit.
