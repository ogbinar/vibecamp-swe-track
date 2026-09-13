#!/usr/bin/env sh
set -eu

: "${IMAGE_REF:?Set IMAGE_REF to the local image ID or immutable registry digest}"
PREVIOUS_IMAGE_REF=${PREVIOUS_IMAGE_REF:-$IMAGE_REF}

base_file="projects/pos/compose.production.yml"
bad_file="projects/pos/compose.unhealthy.yml"
staging="vibecamp-m10-staging"
recovery="vibecamp-m10-recovery"
rejected="vibecamp-m10-rejected"
archive="dist/m10-rehearsal.sql"

cleanup() {
  POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$IMAGE_REF" docker compose -p "$staging" -f "$base_file" down --volumes --remove-orphans >/dev/null 2>&1 || true
  POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" down --volumes --remove-orphans >/dev/null 2>&1 || true
  POSTGRES_PASSWORD=synthetic-rejected IMAGE_REF="$IMAGE_REF" docker compose -p "$rejected" -f "$base_file" -f "$bad_file" down --volumes --remove-orphans >/dev/null 2>&1 || true
}
trap cleanup EXIT INT TERM

mkdir -p dist

POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$IMAGE_REF" docker compose -p "$staging" -f "$base_file" up -d --wait
POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$IMAGE_REF" docker compose -p "$staging" -f "$base_file" exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/ready').read().decode())"

# Exercise the exact rollback/roll-forward commands. For release evidence, pass
# a distinct compatible PREVIOUS_IMAGE_REF; the starter smoke run may use the
# same image to verify command mechanics without claiming version compatibility.
POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$PREVIOUS_IMAGE_REF" docker compose -p "$staging" -f "$base_file" up -d --wait migrate api
POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$IMAGE_REF" docker compose -p "$staging" -f "$base_file" up -d --wait migrate api
POSTGRES_PASSWORD=synthetic-staging IMAGE_REF="$IMAGE_REF" docker compose -p "$staging" -f "$base_file" exec -T postgres pg_dump -U vibecamp -d vibecamp_pos --clean --if-exists > "$archive"
sha256sum "$archive" > "$archive.sha256"

POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" up -d postgres
POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" exec -T postgres sh -c 'until pg_isready -U vibecamp -d vibecamp_pos; do sleep 1; done'
POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" exec -T postgres psql -v ON_ERROR_STOP=1 -U vibecamp -d vibecamp_pos < "$archive"
POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" up -d --wait
POSTGRES_PASSWORD=synthetic-recovery IMAGE_REF="$IMAGE_REF" docker compose -p "$recovery" -f "$base_file" exec -T api python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/ready').read().decode())"

if POSTGRES_PASSWORD=synthetic-rejected IMAGE_REF="$IMAGE_REF" docker compose -p "$rejected" -f "$base_file" -f "$bad_file" up -d --wait; then
  echo "ERROR: synthetic unhealthy candidate was accepted" >&2
  exit 1
fi

echo "PASS: migration preceded readiness; rollback/roll-forward commands passed; isolated restore became ready; unhealthy candidate was rejected"
echo "Evidence: $archive and $archive.sha256 (local synthetic data only)"
