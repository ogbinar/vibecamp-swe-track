# Tools earned here

- **FastAPI routing + generated OpenAPI:** express and inspect the contract; generated docs do not replace consumer examples.
- **FastAPI CLI/Uvicorn runtime:** serve the ASGI application with one documented development command and one no-reload production-shaped command; an application framework is not its own process manager or deployment platform.
- **Pydantic request/response models:** reject ambiguity at the edge; avoid reusing one model for create/update/read when semantics differ.
- **HTTPX + pytest:** API acceptance and rule-level tests; use doubles only for true boundaries.
- **Decimal:** represent money without binary floating-point corruption.

Keep the repository in memory so persistence cannot distract from HTTP reasoning. Implement stable ordering, limits, and pagination behavior before considering `fastapi-pagination`; the adapter must preserve rather than define the contract. Avoid SQLAlchemy, auth, a pagination library, and generic service/base classes. An earned typed client is Stretch only after semantic compatibility checks exist.
