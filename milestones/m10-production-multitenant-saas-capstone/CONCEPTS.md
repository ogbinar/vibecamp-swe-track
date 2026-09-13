# M10 concepts through operating failures

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
