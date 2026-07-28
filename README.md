# OpsPilot

AI-assisted operations co-pilot for small businesses. Starts with lead handling for preschool admissions — surfaces stale leads, drafts follow-ups, and scores inbound inquiries. Humans stay in the loop; the AI recommends, never acts unilaterally.

## Structure

```
backend/    API server and business logic
frontend/   Dashboard UI
agents/     AI agent definitions and prompts
mcp/        MCP server integrations
infra/      Deployment and infrastructure config
tests/      Test suites
docs/       Project documentation
evals/      Agent evaluation scripts and datasets
```

## Quickstart

```bash
cp .env.example .env
# fill in .env values (POSTGRES_USER/PASSWORD/DB, DATABASE_URL, TEST_DATABASE_URL)

# backend - install deps once (from repo root; pyproject.toml is the source of truth)
pip install -e ".[dev]"

# run everything - Postgres, migrations, API - with one command
./scripts/dev.sh

# frontend
cd frontend
npm install
npm run dev
```

`scripts/dev.sh` starts Postgres via Docker Compose, waits for its healthcheck, applies
migrations, then runs the API with reload at http://localhost:8000 (docs at `/docs`).
For the individual steps (e.g. to run migrations without starting the API), see
`docker-compose.yml`, `backend/alembic/`, and `backend/app/main.py`.

## Tests

```bash
# from repo root - requires TEST_DATABASE_URL in .env, pointing at a separate
# database from DATABASE_URL (tests truncate all tables before each test)
python -m pytest tests/ -v

# lint + type check (also run in CI, see .github/workflows/ci.yml)
ruff check .
mypy backend/app
```

## Current Focus

Milestone 1 — Lead Handling workflow for preschool admissions.  
See [`docs/problem_brief.md`](docs/problem_brief.md) for context.

## Guardrails

The AI will never:
- Send messages or emails without human approval
- Mark a lead as lost or closed without confirmation
- Share lead data with external services without explicit sign-off
