# Unhealthy release rejection runbook

Candidate digest: ___  Previous digest: ___  Approver: ___

Record the exact readiness or user-signal failure, stop promotion, preserve
logs/metrics/traces, restore the previous code/config digest, and verify it.
Never improvise a data downgrade. Name whether the database requires a
roll-forward migration and who owns the customer update.
