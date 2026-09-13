# M10 fixed capstone contract

Customer: Northstar Retail, with two stores represented as tenants `north` and
`south`. Each has cashiers and a manager. One platform support actor may enter a
time-bounded, reason-recorded support session approved by that tenant. The buyer
wants first sale, daily export, deletion/retention answers, recovery evidence,
known limits, and a support route.

Finite tenant inventory:

| Path/resource | Tenant source | Required policy |
|---|---|---|
| product/inventory/cart/sale/receipt reads and writes | authenticated membership | same tenant only |
| list/search/report/export | authenticated membership | server-added tenant filter |
| manager operations | membership plus manager role | same tenant only |
| support access | approved support session | one tenant, expiry, reason, audit |
| audit read | tenant manager or platform auditor | scoped and paginated |
| cache/job identifiers if later earned | stored tenant context | reject mismatch |

Tenant IDs from request bodies never establish authority. Audit events contain
actor, tenant, action, target, time, correlation ID, and support reason. Normal
application roles cannot update/delete them. Retain seven years for the exercise;
record legal/product exceptions before deletion. Diagnostic logs are separate,
redacted, and retained 30 days.

Core deployment is the two-environment local rehearsal. The stronger endorsement
uses the CI-built GHCR digest on an authorized target. Daily export is tenant
scoped and checksummed. Tenant deletion removes active rows and exports after a
30-day synthetic hold while retaining documented audit exceptions. Daily
encrypted backup targets RPO 24 hours and RTO 2 hours; prove actual values by
isolated restore and reconcile any gap.

Incident: a missing tenant filter exposes one synthetic south receipt to a north
manager. Detect, contain, identify affected synthetic records, repair, rotate any
synthetic credential if needed, notify the named customer role, restore service,
and produce a blameless postmortem with owned follow-ups.
