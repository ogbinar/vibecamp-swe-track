# Problems and mental models

A timeout means the outcome is unknown, not necessarily failed. Every outbound call needs connect/read/overall bounds, a retry classification, exponential backoff with jitter, a total budget, and an idempotency strategy. Retrying non-idempotent effects blindly duplicates money or shipments.

Webhooks are untrusted, duplicated, delayed, reordered messages. Verify signature against raw bytes, timestamp/replay window, event identity, and account context; acknowledge only durable handling and make processing idempotent. Model pending/succeeded/failed/unknown states and reconcile uncertainty rather than lying to users.

Structured logs with request/correlation IDs connect inbound request, outbound attempt, webhook, and state change. Emit safe fields and useful failure classification. Incident thinking asks impact, timeline, detection, contributing conditions, recovery, and prevention—not blame.
