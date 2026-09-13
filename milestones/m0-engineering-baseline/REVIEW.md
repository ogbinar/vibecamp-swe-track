# M0 review

Answer these in `projects/catalog/evidence/M0/index.md` using your own words:

1. Which tracked files recreate the environment? What remained local?
2. What does `uv.lock` guarantee, and what does it not guarantee?
3. Why does the smoke test send an HTTP request instead of calling the endpoint function directly?
4. How did you prove each test or check could detect its claimed defect?
5. What happened when configuration was missing or malformed?
6. What is the difference between Ruff, mypy, and pytest?
7. Why is `/health` liveness rather than full dependency readiness?

Review the diff for generated files, secrets, undocumented commands, unnecessary
folders, platform assumptions, and disagreement between local and CI commands.
Repeat one failure without your notes and state your hypothesis before inspecting
the cause.

For a **cold review**, use a peer or return later in a clean checkout without
implementation notes. The reviewer repeats one Core API path and one failure,
records confusion and fixes, and gives `PASS` or `NEEDS WORK`.

Optional background lens, with the same A0–A3 gate:

- A career shifter may connect a prior troubleshooting habit to the C1 hypothesis.
- A data specialist may contrast a data-value check with an HTTP/configuration contract.
