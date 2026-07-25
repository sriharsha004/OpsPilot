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

# database
docker compose up -d database

# backend - install deps (from repo root; pyproject.toml is the source of truth)
pip install -e ".[dev]"

# apply migrations
cd backend
alembic upgrade head

# run the API
uvicorn app.main:app --reload

# frontend
cd frontend
npm install
npm run dev
```

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
