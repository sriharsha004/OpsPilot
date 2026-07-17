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
# fill in .env values

# backend
cd backend
pip install -r requirements.txt
python main.py

# frontend
cd frontend
npm install
npm run dev
```

## Current Focus

Milestone 1 — Lead Handling workflow for preschool admissions.  
See [`docs/problem_brief.md`](docs/problem_brief.md) for context.

## Guardrails

The AI will never:
- Send messages or emails without human approval
- Mark a lead as lost or closed without confirmation
- Share lead data with external services without explicit sign-off
