# Backup restore runbook

Backup identifier/checksum: ___  Source time: ___  Isolated target: ___

1. Verify authorization, encryption access, and target isolation.
2. Restore without overwriting the source environment.
3. Run database integrity, application, tenant-boundary, and audit checks.
4. Record actual recovery point objective (RPO) and recovery time objective
   (RTO), missing data, reconciliation, and cleanup owner.
