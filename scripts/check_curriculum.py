"""Validate durable curriculum semantics without coupling to lesson prose."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/maintainers/curriculum.json"
PROJECTS = ("catalog", "pos", "ecommerce", "booking", "social")
EXPECTED_SPECS = {
    "projects/catalog/specs/M1-PRODUCT-BRIEF.md",
    "projects/pos/REQUIREMENTS.md",
    "projects/pos/specs/M2-PERSISTENCE-CONTRACT.md",
    "projects/pos/specs/M3-CHECKOUT-CONTRACT.md",
    "projects/pos/specs/M4-CHANGE-BRIEF.md",
    "projects/pos/specs/M10-CAPSTONE-CONTRACT.md",
    "projects/ecommerce/REQUIREMENTS.md",
    "projects/ecommerce/specs/M5-SECURITY-CONTRACT.md",
    "projects/ecommerce/specs/M6-INTEGRATION-CONTRACT.md",
    "projects/ecommerce/specs/M7-JOB-CONTRACT.md",
    "projects/ecommerce/fixtures/SECURITY-SCENARIOS.md",
    "projects/booking/specs/M8-BOOKING-CONTRACT.md",
    "projects/social/specs/M9-FEED-CONTRACT.md",
}
REQUIRED_TEMPLATE_CAPABILITIES = {
    "ADR.md",
    "COMPLEXITY-REJECTION.md",
    "DATA-LIFECYCLE.md",
    "ENTRY-DIAGNOSTIC.md",
    "EVIDENCE-INDEX.md",
    "INCIDENT.md",
    "PORTFOLIO-CASE-STUDY.md",
    "REQUIREMENTS.md",
    "RUNBOOK-MIGRATION.md",
    "RUNBOOK-RELEASE-REJECTION.md",
    "RUNBOOK-RESTORE.md",
}


def slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[*_`~]", "", text)
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"\s", "-", text)


def anchors(path: Path) -> set[str]:
    found: set[str] = set()
    counts: dict[str, int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        base = slug(match.group(1))
        count = counts.get(base, 0)
        counts[base] = count + 1
        found.add(base if count == 0 else f"{base}-{count}")
    return found


def markdown_links(text: str) -> list[str]:
    return re.findall(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)", text)


def check_links() -> list[str]:
    errors: list[str] = []
    for source in ROOT.rglob("*.md"):
        if any(
            part in {".git", ".venv", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
            for part in source.parts
        ):
            continue
        for raw in markdown_links(source.read_text(encoding="utf-8")):
            if raw.startswith(("http://", "https://", "mailto:")):
                continue
            destination, _, fragment = unquote(raw).partition("#")
            target = (source.parent / destination).resolve() if destination else source.resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: broken link: {raw}")
            elif fragment and target.is_file() and fragment not in anchors(target):
                errors.append(f"{source.relative_to(ROOT)}: broken Markdown anchor: {raw}")
    return errors


def ids(text: str, prefix: str) -> set[str]:
    return set(re.findall(rf"\*\*({prefix}\d+)(?:\s|\u2014|:)", text))


def check_manifest(data: dict[str, object]) -> tuple[list[str], dict[str, Path]]:
    errors: list[str] = []
    milestones = data.get("milestones")
    if data.get("schema_version") != 1 or not isinstance(milestones, list):
        return ["curriculum manifest: unsupported schema"], {}
    by_code: dict[str, Path] = {}
    expected_ids = [f"M{i}" for i in range(11)]
    actual_ids = [entry.get("id") for entry in milestones if isinstance(entry, dict)]
    if actual_ids != expected_ids:
        errors.append("curriculum manifest: milestones must be ordered M0 through M10")
    maturity = [entry.get("maturity") for entry in milestones if isinstance(entry, dict)]
    if maturity != [
        "reproducible",
        "functional",
        "persistent",
        "correct",
        "maintainable",
        "secure",
        "resilient",
        "durable",
        "concurrent",
        "performant",
        "operable/sellable",
    ]:
        errors.append("curriculum manifest: cumulative maturity arc changed")
    root_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    roadmap = re.findall(
        r"^\| (M(?:10|[0-9])) \|[^\n]*\| \[[^\]]+\]\((milestones/[^)]+/README\.md)\) \|$",
        root_readme,
        re.MULTILINE,
    )
    expected_roadmap = [
        (str(entry.get("id")), f"milestones/{entry.get('directory')}/README.md")
        for entry in milestones
        if isinstance(entry, dict)
    ]
    if roadmap != expected_roadmap:
        errors.append("README.md: roadmap must link once to each ordered milestone controller")
    for marker in (
        "cd projects/catalog",
        "uv sync --locked",
        "uv run --locked pytest",
        "Expected:",
        "Catalog setup recovery",
    ):
        if marker not in root_readme:
            errors.append(f"README.md: first action missing {marker!r}")
    for entry in milestones:
        if not isinstance(entry, dict):
            errors.append("curriculum manifest: milestone entry must be an object")
            continue
        code = str(entry.get("id"))
        if entry.get("project") not in PROJECTS:
            errors.append(f"{code}: unknown project owner")
        if not isinstance(entry.get("conditional"), list) or not entry.get("conditional"):
            errors.append(f"{code}: conditional gates missing")
        directory = ROOT / "milestones" / str(entry.get("directory"))
        by_code[code] = directory
        if not directory.is_dir():
            errors.append(f"{code}: milestone directory missing")
            continue
        files = {p.name for p in directory.iterdir() if p.is_file()}
        if files != {"README.md"}:
            errors.append(
                f"{code}: exactly one learner controller README is required; found {sorted(files)}"
            )
            continue
        text = (directory / "README.md").read_text(encoding="utf-8")
        if not text.startswith(f"# {code} — {entry.get('outcome')}"):
            errors.append(f"{code}: controller outcome disagrees with manifest")
        for heading in (
            "Business problem",
            "Product objective",
            "Start here",
            "Build",
            "Understand",
            "Use a tool if earned",
            "Prove it",
            "Done / next",
            "Challenge brief",
            "Acceptance gate",
            "Core",
            "Stretch",
            "Reference",
        ):
            if not re.search(rf"^## {re.escape(heading)}$", text, re.MULTILINE):
                errors.append(f"{code}: missing controller section {heading!r}")
        expected_c = set(entry.get("challenges", []))
        expected_a = set(entry.get("core", []))
        if ids(text, "C") != expected_c:
            errors.append(f"{code}: challenge IDs disagree with manifest")
        if ids(text, "A") != expected_a:
            errors.append(f"{code}: Core IDs disagree with manifest")
        for challenge in expected_c:
            match = re.search(
                rf"^## \*\*{challenge}[^\n]*\n(.*?)(?=^## \*\*C\d+|^---$)",
                text,
                re.MULTILINE | re.DOTALL,
            )
            if not match:
                errors.append(f"{code}: {challenge} scenario missing")
                continue
            section = match.group(1)
            if sum(marker in section for marker in ("**PROVIDED**", "**YOU BUILD**")) != 1:
                errors.append(f"{code}: {challenge} must declare one challenge mode")
            for marker in ("### Steps", "### Hints", "### Reset"):
                if marker not in section:
                    errors.append(f"{code}: {challenge} missing {marker}")
        for marker in ("evidence/", "Expected", "Recovery"):
            if marker.lower() not in text.lower():
                errors.append(f"{code}: controller missing {marker!r} boundary")
    actual_dirs = {p for p in (ROOT / "milestones").glob("m*") if p.is_dir()}
    if actual_dirs != set(by_code.values()):
        errors.append("milestones: unexpected or missing milestone directory")
    return errors, by_code


def check_concept_trace(by_code: dict[str, Path]) -> list[str]:
    errors: list[str] = []
    path = ROOT / "docs/reference/curriculum-map.md"
    text = path.read_text(encoding="utf-8")
    section = text.split("## Concept coverage matrix", 1)
    if len(section) != 2:
        return ["curriculum map: concept coverage matrix missing"]
    rows = []
    for line in section[1].splitlines():
        if line.startswith("| ") and not line.startswith(("| Engineering concept", "|---")):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) == 4:
                rows.append(cells)
    if len(rows) != 58:
        errors.append(
            "curriculum map: expected 58 named concept traces during "
            f"consolidation; found {len(rows)}"
        )
    seen: set[str] = set()
    for concept, introduced, practiced, proven in rows:
        if concept in seen:
            errors.append(f"curriculum map: duplicate concept {concept}")
        seen.add(concept)
        if not re.search(r"M(?:10|[0-9])", introduced):
            errors.append(f"{concept}: missing introduction milestone")
        for value, prefix in ((practiced, "C"), (proven, "A")):
            for group in value.split(";"):
                if (concept, prefix, group.strip()) in {
                    ("Release discipline", "C", "every Ship step"),
                    ("Release discipline", "A", "each gate"),
                }:
                    continue
                code_match = re.search(r"M(?:10|[0-9])", group)
                if not code_match:
                    errors.append(f"{concept}: malformed {prefix} mapping {group!r}")
                    continue
                code = code_match.group(0)
                controller = by_code.get(code)
                for identifier in re.findall(rf"{prefix}\d+", group):
                    body = (
                        (controller / "README.md").read_text(encoding="utf-8") if controller else ""
                    )
                    if not re.search(rf"\*\*{identifier}(?:\s|\u2014|:)", body):
                        errors.append(f"{concept}: {code} {identifier} missing from controller")
    return errors


def check_runtime_and_safety() -> list[str]:
    errors: list[str] = []
    for relative in EXPECTED_SPECS:
        if not (ROOT / relative).is_file():
            errors.append(f"stable project contract missing: {relative}")
    templates = {p.name for p in (ROOT / "templates").glob("*.md")}
    missing = REQUIRED_TEMPLATE_CAPABILITIES - templates
    if missing:
        errors.append(f"template capabilities missing: {sorted(missing)}")
    for project in PROJECTS:
        base = ROOT / "projects" / project
        manifest = (base / "pyproject.toml").read_text(encoding="utf-8")
        version = (base / ".python-version").read_text(encoding="utf-8").strip()
        lock = (base / "uv.lock").read_text(encoding="utf-8")
        web = (base / "src" / f"{project}_api" / "web.py").read_text(encoding="utf-8")
        composition = web + (base / "src" / f"{project}_api" / "main.py").read_text(
            encoding="utf-8"
        )
        if (
            version != "3.13"
            or 'requires-python = "==3.13.*"' not in manifest
            or '"air==0.48.1"' not in manifest
        ):
            errors.append(f"{project}: Python 3.13 and exact Air 0.48.1 runtime required")
        if 'name = "air"\nversion = "0.48.1"' not in lock:
            errors.append(f"{project}: exact Air 0.48.1 is not locked")
        if (
            "air.Air(fastapi_app=api)" not in composition
            or "air.AirRouter(include_in_schema=False)" not in web
        ):
            errors.append(f"{project}: shared Air/FastAPI composition or OpenAPI exclusion missing")
        app_source = (base / "src" / f"{project}_api" / "app.py").read_text(encoding="utf-8")
        api_tests = (base / "tests" / "test_api.py").read_text(encoding="utf-8")
        if '@app.get("/health"' not in app_source or "/openapi.json" not in api_tests:
            errors.append(f"{project}: health or API/OpenAPI regression boundary missing")
        for source in (base / "src").rglob("*.py"):
            body = source.read_text(encoding="utf-8")
            if re.search(r"^(?:from|import)\s+(?:httpx|requests)\b", body, re.MULTILINE):
                errors.append(
                    f"{source.relative_to(ROOT)}: web/application layer must not "
                    "call its own API over HTTP"
                )
        for name in ("package.json", "vite.config.js", "vite.config.ts"):
            if (base / name).exists():
                errors.append(f"{project}: second frontend runtime marker exists: {name}")
        if any((base / "src").rglob("*.js")):
            errors.append(f"{project}: custom project JavaScript exists")
    prohibited = {
        "catalog": ("ProductDraft", "ProductDraftForm", "/app/products/draft"),
        "ecommerce": (
            "hx_get",
            "/app/payments/{operation_id}",
            "/app/jobs",
            "/app/login",
            "/app/orders",
        ),
        "social": ("SSEResponse", "sse_connect", "hx_ext", "/app/feed/events"),
        "pos": ("/app/checkout", "/app/operator"),
    }
    for project, markers in prohibited.items():
        paths = list((ROOT / "projects" / project / "src").rglob("*.py"))
        body = "\n".join(path.read_text(encoding="utf-8") for path in paths)
        for marker in markers:
            if marker in body:
                errors.append(
                    f"{project}: completed or premature learner behavior remains: {marker}"
                )
    ecommerce_source = "\n".join(
        p.read_text(encoding="utf-8") for p in (ROOT / "projects/ecommerce/src").rglob("*.py")
    )
    if "VULNERABLE_ROUTE" in ecommerce_source or '"/debug/login-as"' in ecommerce_source:
        errors.append("ecommerce: callable vulnerable teaching fixture")
    for path in ROOT.rglob("*"):
        if (
            path.is_file()
            and path.suffix.lower() in {".tar", ".tgz", ".zip"}
            and "dist" not in path.parts
        ):
            errors.append(f"generated archive outside dist/: {path.relative_to(ROOT)}")
    secret_patterns = (r"ghp_[A-Za-z0-9]{30,}", r"sk-[A-Za-z0-9]{20,}")
    for path in ROOT.rglob("*"):
        if (
            not path.is_file()
            or path.name == "test_validator_mutations.py"
            or any(
                part
                in {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}
                for part in path.parts
            )
        ):
            continue
        try:
            body = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(re.search(pattern, body) for pattern in secret_patterns):
            errors.append(f"likely secret in {path.relative_to(ROOT)}")
    workflow = ROOT / ".github/workflows/repository-hygiene.yml"
    if workflow.exists() and re.search(
        r"uses:\s+[^\s]+@v\d+", workflow.read_text(encoding="utf-8")
    ):
        errors.append("repository hygiene action is not commit-pinned")
    external = (
        (ROOT / "TODO.md")
        .read_text(encoding="utf-8")
        .split("## External evidence — unchanged and unchecked", 1)
    )
    if len(external) != 2 or re.search(r"^- \[x\]", external[-1], re.MULTILINE):
        errors.append("TODO.md: external evidence must remain visible and unchecked")
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: curriculum manifest unreadable: {exc}")
        return 1
    manifest_errors, by_code = check_manifest(data)
    errors.extend(manifest_errors)
    errors.extend(check_concept_trace(by_code))
    errors.extend(check_links())
    errors.extend(check_runtime_and_safety())
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(
        "OK: 11 one-README milestones; 58 concept traces; semantic manifest, "
        "links, safety, no-solution, and five Air/FastAPI runtimes pass."
    )
    print(
        "LIMIT: local structural checks do not establish provider, hosted, "
        "deployment, or human evidence."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
