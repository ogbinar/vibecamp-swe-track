"""Reset only the course-owned ecommerce schema after explicit confirmation."""

import os
import sys
from urllib.parse import urlsplit

from sqlalchemy import create_engine, text

if sys.argv[1:] != ["--confirm-destroy-course-data"]:
    raise SystemExit("Usage: python scripts/reset.py --confirm-destroy-course-data")
url = os.environ.get("ECOMMERCE_DATABASE_URL", "")
target = urlsplit(url.replace("postgresql+psycopg", "postgresql", 1))
if target.path != "/vibecamp_ecommerce" or target.hostname not in {
    "127.0.0.1",
    "localhost",
    "postgres",
}:
    raise SystemExit("Refusing reset: expected the local course database vibecamp_ecommerce")
with create_engine(url).begin() as connection:
    connection.execute(text("DROP SCHEMA public CASCADE"))
    connection.execute(text("CREATE SCHEMA public"))
print("Reset ecommerce course schema. Run Alembic upgrade next.")
