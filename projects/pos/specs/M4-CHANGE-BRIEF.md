# M4 fixed stakeholder change

Operations needs each receipt to show an optional cashier display name without
changing historical totals. Add the field from HTTP request through service,
persistence, receipt response, and tests. Existing sales remain readable and
show `cashier_name: null`.

The supplied starting awkwardness is deliberate: first record every file that
must change and why. `change scatter` is the count of distinct modules changed
for one behavior. Refactor only after characterization tests preserve current
behavior. Add a dependency-boundary check that fails if API modules import the
database engine directly; API may call a service, and repositories may use a
session.

Done means the stakeholder example passes, old data remains readable, the
before/after scatter count is recorded, and the refactor is behavior-neutral.
