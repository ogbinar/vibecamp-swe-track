# M10 — Production / Multi-tenant SaaS Capstone

**Capability:** own secure delivery, operation, recovery, and release of a product others can trust. **Deliverable:** evolve the existing POS into a non-production-tested multi-tenant SaaS candidate with onboarding, tenant-safe sales/inventory, audit history, observability, deploy/upgrade/rollback, and backup/restore.

Prerequisite: all prior gates. Sequence: define tenant/support/SLO requirements → retrofit tenant context → instrument → build immutable artifact/CI-CD path → deploy migrations safely → attack isolation → restore backup → run incident/release review → ship `m10-production-saas`.

Outputs: tenant and audit model, customer/operator docs, telemetry, runbooks, restore report, deployment record, postmortem, and disciplined release. Remaining real-money limitations must be explicit.
