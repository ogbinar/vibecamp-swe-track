# M10 challenge brief

Use synthetic tenant data. Learner tests run from `projects/pos/`; release drills
run from the repository root.

## **C1 — Invisible production failure**

**YOU BUILD** — answer the fixed checkout-impact question.

### Steps

1. Create `tests/m10/test_observability.py` and seed one checkout failure.
2. Correlate one request through database work with redacted logs, a metric, and a trace.
3. Route the detected symptom to a runbook and run README Block 2.

### Hints

1. Start with the user-impact question and one correlation ID.
2. Inspect request context, database span, error classification, and alert threshold.
3. Use the OpenTelemetry link in `REFERENCE.md`.

### Reset

Disable the synthetic failure and run `uv run --locked pytest tests/m10/test_observability.py -q`.

## **C2 — Cross-tenant security incident**

**YOU BUILD** — use only synthetic tenant attack requests.

### Steps

1. Create `tests/m10/test_tenant_isolation.py` for IDs, lists, writes, exports, jobs, caches, logs, and admin paths.
2. Record disclosure/mutation and missing audit facts before repair.
3. Derive tenant from membership, scope every path, and run README Block 1.

### Hints

1. Ask where tenant context originates and where it is lost.
2. Inspect every query/write/export/cache key and support elevation boundary.
3. Use the tenant-security link in `REFERENCE.md`.

### Reset

Restore only synthetic North/South fixtures and run
`uv run --locked pytest tests/m10/test_tenant_isolation.py -q`.

## **C3 — Failed release and migration**

**YOU BUILD** — use local rehearsal first; a real target needs authorization.

### Steps

1. Build the revision-labelled image and run `sh projects/pos/scripts/rehearse_m10.sh` with its immutable image ID.
2. Confirm migration completes before readiness and the unhealthy override is rejected.
3. Record artifact, migration, restore, rollback/roll-forward decision, and limitations.

### Hints

1. Distinguish image creation, migration, readiness, promotion, and rollback.
2. Inspect Compose dependency conditions, `/ready`, image ID, and migration revision.
3. Use the Docker, Alembic, and Actions links in `REFERENCE.md`.

### Reset

The rehearsal trap removes only its three fixed synthetic Compose projects and
volumes. Rerun `sh projects/pos/scripts/rehearse_m10.sh`; never delete an unexplained volume.

## **C4 — Data-loss and incident drill**

**YOU BUILD** — restore a synthetic backup into an isolated target and follow runbooks.

### Steps

1. Verify `dist/m10-rehearsal.sql.sha256` and inspect the isolated restored revision.
2. Verify tenant totals and audit continuity, then measure recovery point/time.
3. Complete incident, customer, operator, and portfolio evidence using README Block 4.

### Hints

1. A backup file is not recovery evidence; begin with restore and integrity checks.
2. Inspect checksum, schema revision, tenant totals, audit continuity, and elapsed time.
3. Use the PostgreSQL backup/restore link in `REFERENCE.md` and follow the runbook.

### Reset

Preserve sanitized evidence, then rerun the fixed rehearsal; its isolated volumes
are recreated. Verify it first with `sha256sum -c dist/m10-rehearsal.sql.sha256`.
Do not claim the optional real-target endorsement from this drill.

Refactor the existing POS—do not rewrite it. Ship explicit limitations.
