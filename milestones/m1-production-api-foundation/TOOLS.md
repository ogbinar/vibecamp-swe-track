# Tools earned here

- **FastAPI routing + generated OpenAPI:** express and inspect the contract; generated docs do not replace consumer examples.
- **Pydantic request/response models:** reject ambiguity at the edge; avoid reusing one model for create/update/read when semantics differ.
- **HTTPX + pytest:** API acceptance and rule-level tests; use doubles only for true boundaries.
- **Decimal:** represent money without binary floating-point corruption.

Keep the repository in memory so persistence cannot distract from HTTP reasoning. Avoid SQLAlchemy, auth, a pagination library, and generic service/base classes. An earned typed client is Stretch only after semantic compatibility checks exist.
