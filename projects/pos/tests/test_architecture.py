"""Small M4 boundary check; extend the forbidden imports as the POS grows."""

import ast
from pathlib import Path


def test_api_modules_do_not_construct_database_engines() -> None:
    api_root = Path("src/pos_api")
    violations: list[str] = []
    for path in api_root.glob("*.py"):
        if path.name in {"database.py"}:
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == "sqlalchemy":
                if any(alias.name == "create_engine" for alias in node.names):
                    violations.append(str(path))
    assert not violations, f"construct engines only in database.py: {violations}"
