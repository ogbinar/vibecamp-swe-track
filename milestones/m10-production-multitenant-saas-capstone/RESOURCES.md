# Resources for M10

Use these to answer a capstone operational question, not to expand the stack. Reviewed 2026-09-14.

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) — What is backed up, restored, and actually tested? Applicable tool: current PostgreSQL.
- [GitHub deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) — Where do approvals, secrets, and deployment history belong? Applicable platform: GitHub Actions.
- [Amazon S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) — Optional: what bearer scope, expiry, and checksum controls bound direct object access?
- [OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700.html) — Optional: why authorization code with PKCE, and why not the resource-owner password grant? Applicable standard: RFC 9700.
- [Logfire FastAPI](https://pydantic.dev/docs/logfire/integrations/web-frameworks/fastapi/) — Optional example: does one backend answer the named diagnostic question under the declared data/cost boundary? Compare Sentry or SQLAdmin only after its separate trigger fires.

Managed tools such as Logfire or Sentry are optional adapters after telemetry questions are explicit.
