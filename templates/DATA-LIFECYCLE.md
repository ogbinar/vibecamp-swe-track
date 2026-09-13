# Data-lifecycle review

Use only when a milestone creates or changes durable, sensitive, derived, cached, queued, exported, or backed-up data. Trace representative fields; do not write generic privacy prose.

| Field/data class | Source + purpose | Classification | Authoritative store | Derived/cache/queue/provider copies | Access boundary | Retention + deletion/export | Backup/recovery effect | Evidence or explicit deferral |
|---|---|---|---|---|---|---|---|---|

## Review questions

- Which copy is authoritative, and what makes other copies converge or expire?
- Does deletion mean hard delete, tombstone, anonymization, or retained legal/audit record?
- Can logs, failed jobs, provider payloads, caches, exports, and backups outlive the primary row?
- Which actor may read/change/export/delete each class, and how is that tested?
- What recovery action could resurrect deleted or stale data, and how is it reconciled?

Link schema/tests/runbooks. Redact values; lifecycle evidence is about behavior, not collecting sample personal data.
