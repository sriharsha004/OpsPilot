#!/usr/bin/env bash
# One command to run the whole app locally: DB -> migrations -> API.
set -euo pipefail

echo "==> Starting Postgres..."
docker compose up -d database

echo "==> Waiting for Postgres to be healthy..."
until [ "$(docker inspect -f '{{.State.Health.Status}}' db_server 2>/dev/null)" = "healthy" ]; do
  sleep 1
done

echo "==> Applying migrations..."
(cd backend && alembic upgrade head)

echo "==> Starting API on http://localhost:8000 (docs at /docs, Ctrl+C to stop)..."
(cd backend && uvicorn app.main:app --reload)
