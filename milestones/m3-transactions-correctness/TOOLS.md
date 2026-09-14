# Tools earned here

Use the existing FastAPI/PostgreSQL/SQLAlchemy/Alembic stack plus pytest failure injection, controlled clock/ID seams, and small SQL inspection scripts. The database transaction and its isolation behavior are the tool; hide neither behind a generic decorator nor a repository that commits independently.

Keep the transaction local: it owns inventory, sale, receipt, and payment-intent
records in PostgreSQL. It cannot roll back a remote provider effect; do not add
a provider here. Carry that uncertainty to M6.

No message broker, cache, distributed lock, or separate inventory/payment service. Avoid mocks for atomicity—use real integration tests. Earn more sophisticated concurrency control only when M8 measures its contention and semantics.
