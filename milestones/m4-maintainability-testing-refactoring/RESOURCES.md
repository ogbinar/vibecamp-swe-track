# Resources for M4

Consult these when a change is hard to localize or a test gives false confidence. Reviewed 2026-09-13.

- [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/) — How can an endpoint receive a boundary without constructing it? Applicable tool: current FastAPI.
- [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html) — How can tests share setup without sharing mutable state? Applicable tool: pytest 8+.
- [Python typing specification](https://typing.python.org/en/latest/spec/) — What promise does a type annotation make to tools and readers? Applicable standard: current Python typing spec.

Introduce a boundary only when change evidence shows a real coupling problem.
