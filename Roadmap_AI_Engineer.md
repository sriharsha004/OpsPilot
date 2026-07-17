# Applied AI Engineer Roadmap v6 — MCP-Centric Product Engineering

## Changelog from v5

1. Repositioned Applied AI Engineer on product teams as the primary target role.
2. Reframed AI Deployment Engineer and engineering-heavy FDE as secondary role variants.
3. Retained discovery, pilot, and customer work as deployment evidence supporting product-engineering candidacy.
4. Rebuilt Week 5 around measured pgvector-versus-graph-augmented retrieval on one PostgreSQL instance.
5. Made the MCP server the canonical tool layer and moved its core construction into Week 6.
6. Retained GCP infrastructure and Gemini while treating ADK as one MCP consumer rather than the center.
7. Refocused Week 8 on two external integrations plus MCP permission and contract testing.
8. Added a thin non-Google MCP consumer and 15-case portability run in Week 12.
9. Promoted the sanitized MCP repository and official registry submission to a Week 13 must-pass artifact.
10. Reduced customer-scenario mocks to one, added coding/system-design mocks, and verified or replaced stale links.

**Start:** Wednesday, July 15, 2026  
**Portfolio-ready target:** Sunday, October 18, 2026  
**Full interview-ready target:** Sunday, November 8, 2026  
**Primary role:** Applied AI Engineer on product teams  
**Secondary roles:** AI Deployment Engineer / engineering-heavy Forward Deployed Engineer  
**Primary stack:** Python, FastAPI, PostgreSQL, Google Cloud, Gemini, MCP-centric tools, ADK as one consumer, React  
**Normal weekly capacity:** about 12 hours  
**Family-buffer weeks:** July 27–August 16 use a reduced 5–8 hour must-pass plan  
---

## How to use this roadmap

- Every task uses a Markdown checkbox: `- [ ]`.
- Copy this file into Notion, Obsidian, GitHub, or any Markdown editor.
- Complete **Must-pass** tasks before touching **Stretch** tasks.
- Every Sunday ends with:
  - a Git commit,
  - a short demo,
  - a one-paragraph retrospective,
  - an interview-prep score.
- Do not compensate for a missed week by doubling the next week. Resume from the must-pass spine.
- Learning without a build artifact does not count as completion.

---

## The capstone: OpsPilot

Build **OpsPilot**, a production-style enterprise AI operations platform. Start with one real, narrow operational workflow and generalize only after it works.

### Recommended pilot workflow

Use a workflow where you can reach actual users. A practical option is enrollment and operations management using synthetic or carefully anonymized data.

### Core capabilities

1. **Pipeline assistant**
   - Reviews inbound leads
   - Checks capacity and pricing policies
   - Retrieves relevant playbooks
   - Recommends next steps
   - Drafts communications
   - Creates approved tasks

2. **Support assistant**
   - Answers from approved documents
   - Provides citations
   - Enforces tenant and role permissions
   - Escalates when evidence is insufficient

3. **Operations assistant**
   - Detects missed follow-ups, capacity issues, and SLA risks
   - Proposes actions
   - Requires approval before mutations

4. **Revenue analyst**
   - Queries structured data
   - Explains trends
   - Separates facts, assumptions, and recommendations

### Product-engineering narrative with deployment evidence

Your primary story is that you built and improved a production-grade AI product. The discovery, pilot, and customer-facing artifacts serve as deployment evidence that shows the product can survive real workflows and constraints.

**Product problem → data assessment → architecture → implementation → evaluation → production controls → deployment evidence → user feedback → measurable result → reusable component**

---

# Resource library

> Link check completed July 15, 2026. Unverified deep links were replaced with verified official documentation or product landing pages.

## A. LLM and AI foundations

- Andrej Karpathy — **Intro to Large Language Models**  
  https://www.youtube.com/watch?v=zjkBMFhNj_g
- Andrej Karpathy — **Deep Dive into LLMs like ChatGPT**  
  https://www.youtube.com/watch?v=7xTGNNLPyMI
- DeepLearning.AI — **Retrieval Augmented Generation**  
  https://www.deeplearning.ai/courses/retrieval-augmented-generation/
- DeepLearning.AI — **Building and Evaluating Advanced RAG**  
  https://www.deeplearning.ai/courses/building-evaluating-advanced-rag/
- Anthropic — **Building Effective Agents**  
  https://www.anthropic.com/engineering/building-effective-agents
- Anthropic — **Writing Effective Tools for Agents**  
  https://www.anthropic.com/engineering/writing-tools-for-agents

## B. Python backend and testing

- FastAPI official tutorial  
  https://fastapi.tiangolo.com/tutorial/
- SQLAlchemy 2.0 ORM quickstart  
  https://docs.sqlalchemy.org/en/20/orm/quickstart.html
- Alembic tutorial  
  https://alembic.sqlalchemy.org/en/latest/tutorial.html
- pytest getting started  
  https://docs.pytest.org/en/stable/getting-started.html
- pytest fixtures  
  https://docs.pytest.org/en/stable/how-to/fixtures.html
- Docker Compose quickstart  
  https://docs.docker.com/compose/gettingstarted/
- GitHub Actions: build and test Python  
  https://docs.github.com/en/actions/tutorials/build-and-test-code/python

## C. Google Cloud, Gemini, and ADK as an MCP consumer

- Google ADK official documentation  
  https://adk.dev/
- Google ADK Python quickstart  
  https://adk.dev/get-started/python/
- Google ADK introduction video  
  https://www.youtube.com/watch?v=zgrOwow_uTQ
- Google Cloud — deploy an ADK agent to Cloud Run  
  https://docs.cloud.google.com/run/docs/ai/build-and-deploy-ai-agents/deploy-adk-agent
- Vertex AI generative AI documentation  
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/
- Gemini controlled JSON output example  
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-controlled-generation-response-schema-2
- Google Cloud RAG reference architecture  
  https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai
- Google Cloud multi-agent reference architecture  
  https://docs.cloud.google.com/architecture/multiagent-ai-system
- Google Cloud Well-Architected Framework  
  https://docs.cloud.google.com/architecture/framework
- Google Cloud billing budgets  
  https://docs.cloud.google.com/billing/docs/how-to/budgets
- Google Cloud Secret Manager quickstart  
  https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart

## D. Retrieval and vector storage

- pgvector repository and documentation  
  https://github.com/pgvector/pgvector
- Microsoft GraphRAG documentation  
  https://microsoft.github.io/graphrag/
- Google Cloud RAG overview  
  https://cloud.google.com/use-cases/retrieval-augmented-generation
- Google Cloud RAG architecture collection  
  https://docs.cloud.google.com/architecture/rag-reference-architectures

## E. MCP, evaluation, observability, and security

- MCP Python SDK  
  https://py.sdk.modelcontextprotocol.io/
- Official MCP Python repository  
  https://github.com/modelcontextprotocol/python-sdk
- Official MCP Registry publishing quickstart  
  https://modelcontextprotocol.io/registry/quickstart
- Vertex AI Gen AI evaluation overview  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Evaluate AI agents: final response and trajectory  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents
- Google Cloud agent observability  
  https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability
- OWASP GenAI / LLM Top 10  
  https://genai.owasp.org/llm-top-10/

## F. Deployment evidence and customer discovery

- Nielsen Norman Group — User Interviews 101  
  https://www.nngroup.com/articles/user-interviews/
- IDEO Design Kit — Interview method  
  https://www.designkit.org/methods/interview.html
- Google Cloud Well-Architected Framework  
  https://docs.cloud.google.com/architecture/framework
- Google Cloud Architecture Center  
  https://docs.cloud.google.com/architecture

## G. Coding interview preparation

- Google Careers preparation resources  
  https://www.google.com/about/careers/applications/buildyourfuture/resources/
- Google Careers interview-preparation resources  
  https://www.google.com/about/careers/applications/buildyourfuture/resources/
- Google mock coding question  
  https://www.youtube.com/watch?v=Ti5vfu9arXQ
- NeetCode roadmap  
  https://neetcode.io/roadmap
- NeetCode YouTube channel  
  https://www.youtube.com/c/neetcode
- MIT 6.006 Introduction to Algorithms playlist  
  https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY
- Tech Interview Handbook algorithm cheatsheets  
  https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/

## H. System-design interview preparation

- ByteByteGo YouTube  
  https://www.youtube.com/@ByteByteGo
- Gaurav Sen system-design playlist  
  https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX
- System Design Primer  
  https://github.com/donnemartin/system-design-primer

---

# Weekly operating rules

## Normal week

| Day | Target time | Main purpose |
|---|---:|---|
| Monday | 60 min | Learn and plan |
| Tuesday | 90 min | Build + coding problem |
| Wednesday | 90 min | Build |
| Thursday | 90 min | Build + system design/deployment evidence |
| Friday | 60 min | Test, refactor, document |
| Saturday | 180 min | Deep build + coding |
| Sunday | 150 min | Integrate, demo, review |

## Family-buffer week

| Day | Target time | Main purpose |
|---|---:|---|
| Monday | 45 min | Learn |
| Tuesday | 45 min | Small implementation |
| Wednesday | 45 min | Coding or test |
| Thursday | 45 min | Small implementation |
| Friday | 0–30 min | Optional review |
| Saturday | 120 min | Must-pass build |
| Sunday | 90 min | Integrate and commit |

---
# Career Target:

- **Applied AI Engineer on a product team**
- **AI Deployment Engineer / engineering-heavy FDE**.

Desire job mix: 70–80% product engineering, with purposeful deployment/customer collaboration and no sales quota.

---


# Week 0 — Orientation and baseline

**Dates:** Wednesday, July 15–Sunday, July 19  
**Capacity:** 6–7 hours  
**Goal:** Establish the repository, product scope, cloud account, and interview baseline.

## Resources

- Karpathy — Intro to LLMs  
  https://www.youtube.com/watch?v=zjkBMFhNj_g
- Google ADK introduction  
  https://www.youtube.com/watch?v=zgrOwow_uTQ
- Google Careers interview-preparation resources  
  https://www.google.com/about/careers/applications/buildyourfuture/resources/
- Nielsen Norman Group — User Interviews 101  
  https://www.nngroup.com/articles/user-interviews/

## Wednesday, July 15 — Define the target

- [x] Create a document called `career_target.md`.
- [x] Write your primary target: **Applied AI Engineer on a product team**.
- [x] Write your secondary target: **AI Deployment Engineer / engineering-heavy FDE**.
- [x] Define your desired job mix: 70–80% product engineering, with purposeful deployment/customer collaboration and no sales quota.
- [x] Read this entire roadmap once without beginning implementation.
- [x] Watch the first 30 minutes of Karpathy’s Intro to LLMs.
- [x] Write five concepts you understood and three concepts that remain unclear.

## Thursday, July 16 — Define the capstone and users

- [ ] Create `docs/problem_brief.md`.
- [ ] Choose one initial workflow: lead handling, support Q&A, operations follow-up, or revenue analysis.
- [ ] Identify one or two potential users who understand the workflow.
- [ ] Write the current process in 8–12 steps.
- [ ] Record current pain points, delays, repeated manual work, and risky decisions.
- [ ] Define three actions the AI may recommend.
- [ ] Define three actions the AI must never execute without approval.
- [ ] Read Nielsen Norman Group’s User Interviews 101.
- [ ] Draft ten open-ended discovery questions.

## Friday, July 17 — Repository and local tools

- [ ] Create a GitHub repository named `opspilot-gcp`.
- [ ] Add directories: `backend`, `frontend`, `agents`, `mcp`, `infra`, `tests`, `docs`, `evals`.
- [ ] Create a Python 3.12 virtual environment.
- [ ] Add Ruff, mypy, pytest, pre-commit, and a basic `pyproject.toml`.
- [ ] Add a `.gitignore`, `.env.example`, and initial README.
- [ ] Make the first commit: `chore: initialize OpsPilot project`.

## Saturday, July 18 — Cloud setup and coding diagnostic

- [ ] Create or select a Google Cloud project.
- [ ] Configure a billing budget and email alerts.
- [ ] Install and authenticate the Google Cloud CLI.
- [ ] Record project ID, region choice, and naming conventions in `docs/gcp_setup.md`.
- [ ] Solve **Contains Duplicate** without assistance.  
  https://leetcode.com/problems/contains-duplicate/
- [ ] Solve **Valid Anagram** without assistance.  
  https://leetcode.com/problems/valid-anagram/
- [ ] For each problem, write time complexity, space complexity, edge cases, and one improved implementation.
- [ ] Watch the Google example coding interview and note five communication behaviors.

## Sunday, July 19 — Architecture baseline and weekly close

- [ ] Draw a simple architecture: React → FastAPI → PostgreSQL → canonical MCP server → Gemini/ADK consumer → integrations.
- [ ] Add Cloud Run, Cloud SQL, BigQuery/Sheets, Cloud Storage/Drive, Logging, and Monitoring as future components; label ADK as one replaceable MCP client.
- [ ] Write the first version of success metrics:
  - task completion,
  - grounded answer rate,
  - unauthorized action rate,
  - latency,
  - cost per successful task,
  - user time saved.
- [ ] Record a 3-minute project-introduction video.
- [ ] Commit the architecture and discovery documents.
- [ ] Score yourself from 1–5 on Python, SQL, cloud, RAG, agents, system design, and coding interviews.

### Week 0 must-pass

- [ ] Repository exists and runs basic tooling.
- [ ] Problem brief and discovery questions exist.
- [ ] GCP project and budget alert exist.
- [ ] Two coding problems completed.
- [ ] First architecture diagram and demo recorded.

### Week 0 stretch

- [ ] Complete the full Karpathy Intro to LLMs video.
- [ ] Schedule the first real discovery conversation.

---

# Week 1 — Production backend and deployment discovery

**Dates:** July 20–26  
**Capacity:** 12 hours  
**Goal:** A tested multi-tenant FastAPI/PostgreSQL backend and a validated workflow problem.

## Resources

- FastAPI tutorial  
  https://fastapi.tiangolo.com/tutorial/
- SQLAlchemy ORM quickstart  
  https://docs.sqlalchemy.org/en/20/orm/quickstart.html
- Alembic tutorial  
  https://alembic.sqlalchemy.org/en/latest/tutorial.html
- Docker Compose quickstart  
  https://docs.docker.com/compose/gettingstarted/
- pytest fixtures  
  https://docs.pytest.org/en/stable/how-to/fixtures.html
- MIT 6.006 — data structures and dynamic arrays  
  https://www.youtube.com/watch?v=CHhwJjR0mZA

## Monday, July 20 — Backend design

- [ ] Read FastAPI’s sections on path operations, request bodies, dependencies, and error handling.
- [ ] Read the SQLAlchemy ORM quickstart.
- [ ] Define database tables: tenants, users, leads, capacity, pricing_rules, documents, tasks, communications, audit_events.
- [ ] Draw relationships and identify tenant-owned tables.
- [ ] Write five authorization rules in `docs/authorization_rules.md`.

## Tuesday, July 21 — Database foundation + coding

- [ ] Add PostgreSQL to Docker Compose.
- [ ] Configure SQLAlchemy engine and session management.
- [ ] Implement Tenant, User, and Lead models.
- [ ] Initialize Alembic and create the first migration.
- [ ] Solve **Two Sum**.  
  https://leetcode.com/problems/two-sum/
- [ ] Explain the solution aloud before coding.

## Wednesday, July 22 — CRUD and validation

- [ ] Implement Pydantic request and response schemas.
- [ ] Build create/read/update endpoints for tenants and leads.
- [ ] Add standardized API error responses.
- [ ] Prevent direct assignment of another tenant’s ID.
- [ ] Add API tests for valid and invalid requests.

## Thursday, July 23 — Deployment-evidence discovery + system design

- [ ] Conduct a 30–45 minute discovery conversation or realistic role-play.
- [ ] Ask about the current workflow, exceptions, data sources, success, and unacceptable failures.
- [ ] Write a session summary without proposing solutions during the first section.
- [ ] Create a first pilot scope with one user, one workflow, and one success metric.
- [ ] System-design prompt: design a multi-tenant task API.
- [ ] Spend 15 minutes clarifying requirements before drawing components.

## Friday, July 24 — Test isolation and CI

- [ ] Add pytest fixtures for app, test database, tenant, and user.
- [ ] Add at least three cross-tenant access tests.
- [ ] Add GitHub Actions for linting, type checking, and tests.
- [ ] Make sure CI creates a test database or uses a PostgreSQL service container.
- [ ] Document local startup commands.

## Saturday, July 25 — Complete the backend spine + coding

- [ ] Implement Capacity, PricingRule, Task, and AuditEvent models.
- [ ] Create CRUD endpoints needed for the initial workflow.
- [ ] Add seed data for two tenants.
- [ ] Add a tenant-aware repository/service layer.
- [ ] Reach at least 15 meaningful tests.
- [ ] Solve **Group Anagrams**.  
  https://leetcode.com/problems/group-anagrams/
- [ ] Solve **Top K Frequent Elements**.  
  https://leetcode.com/problems/top-k-frequent-elements/

## Sunday, July 26 — Integrate and explain

- [ ] Run the entire application with one command.
- [ ] Run migrations from an empty database.
- [ ] Test one normal workflow using the OpenAPI interface.
- [ ] Update the architecture diagram.
- [ ] Record a 4-minute backend demo.
- [ ] Commit all code.
- [ ] Write a retrospective: what was harder than expected, and what must change next week?

### Week 1 must-pass

- [ ] FastAPI and PostgreSQL run through Docker Compose.
- [ ] Alembic migrations work.
- [ ] Core tenant-aware models and endpoints work.
- [ ] CI passes.
- [ ] At least 15 tests, including tenant-isolation tests.
- [ ] One discovery summary and pilot scope exist.
- [ ] Three coding problems completed.

### Week 1 stretch

- [ ] Add pagination and filtering.
- [ ] Add polished OpenAPI descriptions.
- [ ] Add test coverage reporting.

---

# Week 2 — GCP and Gemini foundation

**Dates:** July 27–August 2  
**Capacity:** 6–8 hour family-buffer week  
**Goal:** Secure Gemini access through Vertex AI and one reliable structured-output workflow.

## Resources

- Vertex AI generative AI docs  
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/
- Gemini controlled JSON output  
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-controlled-generation-response-schema-2
- Secret Manager quickstart  
  https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart
- Karpathy Intro to LLMs, remaining sections  
  https://www.youtube.com/watch?v=zjkBMFhNj_g
- NeetCode arrays and hashing roadmap  
  https://neetcode.io/roadmap

## Monday, July 27 — Gemini mental model

- [ ] Study tokens, context windows, temperature, top-p, structured output, and hallucination.
- [ ] Write one paragraph for each concept in `docs/llm_fundamentals.md`.
- [ ] Record how model nondeterminism affects testing.
- [ ] Note which application decisions must remain deterministic.

## Tuesday, July 28 — Vertex AI authentication

- [ ] Enable the required Vertex AI API.
- [ ] Configure Application Default Credentials locally.
- [ ] Create a minimal Python script that calls Gemini through Vertex AI.
- [ ] Move configuration into environment variables.
- [ ] Confirm secrets are not committed.

## Wednesday, July 29 — Structured output + coding

- [ ] Define a Pydantic model for `LeadAnalysis`.
- [ ] Make Gemini return schema-constrained JSON.
- [ ] Validate the response before using it.
- [ ] Add a malformed-response test using a mocked model response.
- [ ] Solve **Best Time to Buy and Sell Stock**.  
  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Thursday, July 30 — Provider service

- [ ] Create `ModelProvider` and `GeminiProvider` interfaces.
- [ ] Add timeout, retry, request ID, and structured logging.
- [ ] Record input/output token counts when available.
- [ ] Record total request latency.
- [ ] Return typed application errors rather than SDK-specific exceptions.

## Friday, July 31 — Optional review

- [ ] Review the code for secret leakage and hard-coded project IDs.
- [ ] Add `.env.example` entries.
- [ ] Skip this session without guilt if personal availability is limited.

## Saturday, August 1 — Lead-analysis endpoint

- [ ] Add `/ai/analyze-lead`.
- [ ] Retrieve lead, capacity, and pricing information from the database.
- [ ] Construct a compact prompt using only required data.
- [ ] Return structured recommendations and uncertainty.
- [ ] Add tests for timeout, malformed output, and missing lead.
- [ ] Solve **Valid Palindrome**.  
  https://leetcode.com/problems/valid-palindrome/

## Sunday, August 2 — Close the week

- [ ] Run ten sample lead analyses.
- [ ] Record success, failure, token, and latency data in a CSV.
- [ ] Review at least two failures manually.
- [ ] Record a 3-minute Gemini integration demo.
- [ ] Commit and tag the build `week-02`.
- [ ] Write one deployment-evidence story: how you would explain model uncertainty to a user or customer.

### Week 2 must-pass

- [ ] Vertex AI Gemini call works.
- [ ] Structured output is validated.
- [ ] Timeout and malformed-response tests pass.
- [ ] Lead-analysis endpoint works.
- [ ] Token and latency data are recorded.
- [ ] Two coding problems completed.

### Week 2 stretch

- [ ] Add streaming.
- [ ] Add prompt-version metadata.
- [ ] Add Secret Manager integration now rather than in the security phase.

---

# Week 3 — Reliable model service and prompt evaluation

**Dates:** August 3–9  
**Capacity:** 5–7 hour family-buffer week  
**Goal:** Turn one working model call into a testable, measurable model integration layer.

## Resources

- Karpathy — Deep Dive into LLMs  
  https://www.youtube.com/watch?v=7xTGNNLPyMI
- Vertex AI samples  
  https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples
- Google mock coding question  
  https://www.youtube.com/watch?v=Ti5vfu9arXQ

## Monday, August 3 — Failure modes

- [ ] Study hallucination, refusal, context overflow, stale context, prompt injection, and malformed JSON.
- [ ] Create `docs/model_failure_modes.md`.
- [ ] Add a mitigation and observable signal for each failure mode.

## Tuesday, August 4 — Prompt contracts

- [ ] Create a versioned prompt file for lead analysis.
- [ ] Separate system instructions, task instructions, context, and output schema.
- [ ] Add explicit unknown/insufficient-evidence behavior.
- [ ] Add prompt version to logs and responses.

## Wednesday, August 5 — Small evaluation set + coding

- [ ] Create 15 lead-analysis test cases.
- [ ] Include normal, incomplete, contradictory, and unsafe requests.
- [ ] Define expected structured fields and hard constraints.
- [ ] Solve **Longest Substring Without Repeating Characters**.  
  https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Thursday, August 6 — Lightweight run

- [ ] Execute the 15-case set.
- [ ] Categorize failures.
- [ ] Fix only the highest-frequency failure.
- [ ] Avoid adding new features.

## Friday, August 7 — Optional rest/review

- [ ] Review one model trace and write what the system knew, assumed, and invented.
- [ ] Skip if unavailable.

## Saturday, August 8 — Follow-up drafting

- [ ] Define a `FollowUpDraft` schema.
- [ ] Add a drafting endpoint that consumes approved lead-analysis fields.
- [ ] Ensure it does not send communications.
- [ ] Add unsafe-content and unsupported-claim checks.
- [ ] Solve **Minimum Size Subarray Sum**.  
  https://leetcode.com/problems/minimum-size-subarray-sum/

## Sunday, August 9 — Interview communication

- [ ] Give a 5-minute explanation of tokens, context, temperature, hallucination, and structured output.
- [ ] Explain why model output must be validated like untrusted external input.
- [ ] Record a demo of lead analysis and draft generation.
- [ ] Commit and write the weekly retrospective.

### Week 3 must-pass

- [ ] Versioned prompts exist.
- [ ] Fifteen-case evaluation runs.
- [ ] Lead analysis and drafting are separate steps.
- [ ] No communication is automatically sent.
- [ ] Two coding problems completed.

### Week 3 stretch

- [ ] Add request caching.
- [ ] Compare two current Gemini models on five cases.
- [ ] Add a secondary provider interface.

---

# Week 4 — Structured and unstructured data readiness

**Dates:** August 10–16  
**Capacity:** 7–8 hour family-buffer week  
**Goal:** Build reliable ingestion pipelines before building RAG.

## Resources

- Google Cloud RAG architecture  
  https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai
- Google Cloud Storage documentation  
  https://docs.cloud.google.com/storage/docs/
- BigQuery introduction  
  https://docs.cloud.google.com/bigquery/docs/introduction
- DeepLearning.AI RAG course  
  https://www.deeplearning.ai/courses/retrieval-augmented-generation/

## Monday, August 10 — Data-source inventory

- [ ] Create `docs/data_inventory.md`.
- [ ] List structured sources, unstructured sources, owners, refresh frequency, sensitivity, and access rules.
- [ ] Define a canonical lead and billing schema.
- [ ] Define required document metadata.

## Tuesday, August 11 — Structured ingestion

- [ ] Create CSV or Google Sheets ingestion for leads/billing records.
- [ ] Validate types and required fields.
- [ ] Generate a rejected-record report.
- [ ] Add source ID and ingestion timestamp.

## Wednesday, August 12 — Data quality + coding

- [ ] Add duplicate detection.
- [ ] Add missing-value and invalid-date reporting.
- [ ] Add idempotent re-import behavior.
- [ ] Solve **Valid Parentheses**.  
  https://leetcode.com/problems/valid-parentheses/

## Thursday, August 13 — Unstructured ingestion

- [ ] Create document ingestion from a local folder or Cloud Storage.
- [ ] Capture source path, tenant ID, version, hash, title, and access metadata.
- [ ] Reject unsupported file types.
- [ ] Preserve source provenance.

## Friday, August 14 — Optional review

- [ ] Manually inspect ten structured records and five documents.
- [ ] Compare the source with stored data.
- [ ] Skip if unavailable.

## Saturday, August 15 — Versioning and deletion

- [ ] Add document hash-based duplicate detection.
- [ ] Add document version tracking.
- [ ] Define deletion and re-indexing behavior.
- [ ] Generate a data-readiness report.
- [ ] Solve **Merge Two Sorted Lists**.  
  https://leetcode.com/problems/merge-two-sorted-lists/

## Sunday, August 16 — Data workshop simulation

- [ ] Present the data-readiness report as if speaking to a customer data team.
- [ ] Explain missing fields, duplicates, stale data, and permission gaps.
- [ ] Record unresolved data risks.
- [ ] Commit the ingestion pipeline and report.
- [ ] Record a 4-minute ingestion demo.

### Week 4 must-pass

- [ ] One structured ingestion path works.
- [ ] One unstructured ingestion path works.
- [ ] Invalid data is quarantined or reported.
- [ ] Provenance and tenant metadata are preserved.
- [ ] Data-readiness report exists.
- [ ] Two coding problems completed.

### Week 4 stretch

- [ ] Read directly from Google Sheets or Drive.
- [ ] Add Pub/Sub or event-driven ingestion.
- [ ] Add PII detection.

---

# Week 5 — Baseline RAG and graph-augmented retrieval

**Dates:** August 17–23  
**Capacity:** 10–12 hours  
**Goal:** Serve the same authorized corpus through baseline pgvector retrieval and graph-augmented retrieval, then measure where each path wins.

## Resources

- DeepLearning.AI RAG course  
  https://www.deeplearning.ai/courses/retrieval-augmented-generation/
- pgvector  
  https://github.com/pgvector/pgvector
- Microsoft GraphRAG documentation  
  https://microsoft.github.io/graphrag/
- Google Cloud RAG reference architecture  
  https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai

## Monday, August 17 — Dual-path retrieval architecture

- [ ] Study embeddings, chunking, dense retrieval, graph-augmented retrieval, and reranking.
- [ ] Draw the shared ingestion flow and two separate query-time paths.
- [ ] Define chunk, entity, relation, citation, tenant, and role metadata.
- [ ] Define where graph traversal should plausibly outperform dense retrieval: multi-hop, cross-document, and relationship questions.

## Tuesday, August 18 — Baseline pgvector path + coding

- [ ] Enable pgvector in the existing PostgreSQL instance.
- [ ] Add document and chunk tables.
- [ ] Generate embeddings for ingested chunks.
- [ ] Implement cosine-similarity dense retrieval with citations.
- [ ] Solve **Reverse Linked List**.  
  https://leetcode.com/problems/reverse-linked-list/

## Wednesday, August 19 — Graph extraction in PostgreSQL

- [ ] Add entity-node and relation-edge tables in the same PostgreSQL instance; do not add another database.
- [ ] Use an LLM extraction schema to identify entities and typed relations from the existing chunks.
- [ ] Preserve source chunk IDs, document IDs, tenant IDs, roles, and extraction version on every node and edge.
- [ ] Add deduplication or canonicalization for repeated entity names.

## Thursday, August 20 — Graph-augmented retrieval + AI design

- [ ] Implement entity matching from the user query.
- [ ] Traverse a bounded one-hop or two-hop neighborhood.
- [ ] Retrieve the source chunks attached to matched nodes and edges.
- [ ] Merge graph-derived chunks with pgvector results using a documented scoring rule.
- [ ] AI system-design prompt: design tenant-safe dual-path retrieval in one PostgreSQL system.

## Friday, August 21 — Authorization and grounded answering

- [ ] Apply tenant and role authorization before both dense retrieval and graph traversal.
- [ ] Add tests proving unauthorized nodes, edges, and chunks never enter either candidate set.
- [ ] Build one grounded answering endpoint that accepts either retrieval path.
- [ ] Require citations and add “insufficient evidence” behavior.
- [ ] Log retrieval path, candidate IDs, scores, graph hops, answer, and citations.

## Saturday, August 22 — Comparative retrieval evaluation + coding

- [ ] Expand to a 30-question RAG evaluation set served against BOTH retrieval paths.
- [ ] Include factual, unanswerable, ambiguous, stale, cross-tenant, cross-document, and multi-hop questions.
- [ ] Label the multi-hop questions where graph traversal is expected to help.
- [ ] Score both paths on retrieval hit rate, faithfulness, and citation correctness.
- [ ] Manually label failures and record path-specific latency and token use.
- [ ] Solve **Min Stack**.  
  https://leetcode.com/problems/min-stack/
- [ ] Solve **Binary Search**.  
  https://leetcode.com/problems/binary-search/

## Sunday, August 23 — Graph-versus-vanilla report

- [ ] Run all 30 questions through both paths using the same answer-generation configuration.
- [ ] Fix one dense-retrieval failure and one graph-retrieval failure.
- [ ] Create `docs/retrieval-comparison.md` with method, metrics, multi-hop results, latency, limitations, and recommendation.
- [ ] Record a 5-minute demo showing one question where dense retrieval wins and one where graph traversal wins.
- [ ] Explain chunking, graph extraction, authorization, citations, and when not to use the graph path.
- [ ] Commit and publish the measured Graph-versus-vanilla comparison as a headline artifact.

### Week 5 must-pass

- [ ] Baseline pgvector dense retrieval works.
- [ ] Graph-augmented retrieval works from node/edge tables in the same PostgreSQL instance.
- [ ] Thirty-question evaluation scores BOTH paths on hit rate, faithfulness, and citation correctness.
- [ ] Multi-hop questions are explicitly represented and analyzed.
- [ ] Tenant and role authorization tests pass for BOTH paths.
- [ ] `docs/retrieval-comparison.md` is complete.
- [ ] Three coding problems completed.

### Week 5 stretch

- [ ] Add PostgreSQL full-text/BM25-style retrieval as a third signal in the merge.
- [ ] Add a reranker after candidate merging.
- [ ] Compare one-hop versus two-hop traversal limits.

# Week 6 — MCP-centric single-agent workflow

**Dates:** August 24–30  
**Capacity:** 12 hours  
**Goal:** A bounded, traceable agent that consumes all application tools through the canonical MCP server from day one; ADK is one client, not the tool source of truth.

## Resources

- MCP Python SDK  
  https://py.sdk.modelcontextprotocol.io/
- Official MCP Python repository  
  https://github.com/modelcontextprotocol/python-sdk
- ADK Python quickstart  
  https://adk.dev/get-started/python/
- ADK MCP documentation  
  https://adk.dev/mcp/
- Anthropic — Building Effective Agents  
  https://www.anthropic.com/engineering/building-effective-agents

## Monday, August 24 — Workflow, agent, and MCP boundaries

- [ ] Read Anthropic’s Building Effective Agents.
- [ ] List which OpsPilot steps are deterministic workflows.
- [ ] List which steps require model judgment.
- [ ] Define the MCP server as the canonical tool-contract and permission boundary.
- [ ] Define a bounded agent goal and explicit termination conditions.

## Tuesday, August 25 — First MCP tools and ADK consumer + coding

- [ ] Create the core MCP server in the `mcp` package.
- [ ] Expose a read-only lead lookup tool with typed input/output and structured errors.
- [ ] Complete the ADK Python quickstart and connect ADK to the MCP server as a client.
- [ ] Confirm the ADK agent contains no duplicate direct implementation of the lead tool.
- [ ] Solve **Search a 2D Matrix**.  
  https://leetcode.com/problems/search-a-2d-matrix/

## Wednesday, August 26 — Canonical MCP tool set

- [ ] Expose capacity lookup through MCP.
- [ ] Expose pricing-rule lookup through MCP.
- [ ] Expose dual-path policy-document search through MCP.
- [ ] Expose task recommendation as a non-mutating MCP tool.
- [ ] Validate all tool arguments and enforce tenant/role context at the MCP boundary.

## Thursday, August 27 — Agent control + interview design

- [ ] Add maximum turns and timeout to the ADK consumer.
- [ ] Add explicit success, failure, and escalation states.
- [ ] Capture model, MCP tool-call, retrieval-path, and result traces.
- [ ] AI design prompt: when should a workflow use an agent rather than deterministic code?
- [ ] Prepare a 3-minute answer to: “Why MCP-centric with ADK as one consumer?”

## Friday, August 28 — MCP and agent tests

- [ ] Add MCP contract tests for every current tool.
- [ ] Mock tool successes and failures from the agent client.
- [ ] Test invalid arguments, permission failures, loops, and non-termination.
- [ ] Test insufficient evidence.
- [ ] Ensure the MCP server exposes no sensitive write actions yet.

## Saturday, August 29 — Task benchmark + coding

- [ ] Create 20 multi-step agent tasks.
- [ ] Run and manually classify them through the ADK-to-MCP path.
- [ ] Measure task completion, tool selection, argument correctness, and unnecessary calls.
- [ ] Fix the most common failure without duplicating tool logic in the client.
- [ ] Solve **Koko Eating Bananas**.  
  https://leetcode.com/problems/koko-eating-bananas/
- [ ] Solve **Invert Binary Tree**.  
  https://leetcode.com/problems/invert-binary-tree/

## Sunday, August 30 — MCP-centric project deep dive

- [ ] Record a 7-minute walkthrough of the MCP-centric single-agent architecture.
- [ ] Explain why ADK as one consumer is replaceable but the MCP contracts remain canonical.
- [ ] Explain why write actions are not yet enabled.
- [ ] Explain one evaluation failure and correction.
- [ ] Commit and tag `mcp-single-agent-v0.1`.
- [ ] Write the first polished interview story: “Why agent versus workflow, and why MCP-centric?”

### Week 6 must-pass

- [ ] Canonical MCP server works.
- [ ] ADK consumes all agent tools through MCP from day one.
- [ ] At least four typed read-only MCP tools work.
- [ ] MCP permission and contract tests pass.
- [ ] Iterations and time are bounded.
- [ ] Twenty-task benchmark exists.
- [ ] Agent and MCP traces are visible.
- [ ] Three coding problems completed.

### Week 6 stretch

- [ ] Add a fifth MCP tool.
- [ ] Add model-routing by task type without changing tool contracts.
- [ ] Add local MCP inspector/debugging instructions.

# Week 7 — Cloud Run deployment and usable fallback demo

**Dates:** August 31–September 6  
**Capacity:** 12 hours  
**Goal:** A public authenticated deployment that remains usable even if later agent work fails.

## Resources

- Deploy ADK to Cloud Run  
  https://docs.cloud.google.com/run/docs/ai/build-and-deploy-ai-agents/deploy-adk-agent
- Cloud Run ADK quickstart  
  https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service
- Google Cloud Well-Architected Framework  
  https://docs.cloud.google.com/architecture/framework

## Monday, August 31 — Deployment design

- [ ] Define development, test, and production configuration.
- [ ] Choose the deployment region.
- [ ] Define service account permissions.
- [ ] Create a deployment checklist.

## Tuesday, September 1 — Containerization + coding

- [ ] Create a production Dockerfile.
- [ ] Add health and readiness endpoints.
- [ ] Confirm configuration is environment-driven.
- [ ] Run the container locally.
- [ ] Solve **Maximum Depth of Binary Tree**.  
  https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Wednesday, September 2 — Deploy to Cloud Run

- [ ] Create a dedicated service account.
- [ ] Deploy the backend, canonical MCP server, and ADK consumer to Cloud Run.
- [ ] Store secrets outside the container.
- [ ] Verify authenticated access.
- [ ] Record deployment commands in `docs/deployment.md`.

## Thursday, September 3 — Failure and cost controls

- [ ] Set concurrency, timeout, and instance limits.
- [ ] Add basic rate limiting at the application layer.
- [ ] Verify billing-budget alerts.
- [ ] System-design prompt: design a serverless AI API with burst traffic and expensive model calls.
- [ ] Discuss cost controls and abuse prevention.

## Friday, September 4 — Production smoke tests

- [ ] Run database, both RAG paths, MCP, and agent-consumer smoke tests against the deployed service.
- [ ] Confirm logs contain request IDs.
- [ ] Confirm no secret is printed.
- [ ] Document known limitations.

## Saturday, September 5 — Minimal interface + coding

- [ ] Add a minimal UI or authenticated Swagger-based demo flow.
- [ ] Support lead analysis, grounded Q&A, and agent recommendation.
- [ ] Add clear loading, failure, and refusal states.
- [ ] Solve **Diameter of Binary Tree**.  
  https://leetcode.com/problems/diameter-of-binary-tree/
- [ ] Solve **Same Tree**.  
  https://leetcode.com/problems/same-tree/

## Sunday, September 6 — Fallback demo milestone

- [ ] Have another person run three tasks from written instructions.
- [ ] Note setup confusion and usability problems.
- [ ] Record a 5-minute customer-oriented demo.
- [ ] Commit and tag `fallback-demo-v0.1`.
- [ ] Update your résumé project section with a private draft.

### Week 7 must-pass

- [ ] Cloud Run deployment is live.
- [ ] Authentication and service account are configured.
- [ ] Health/readiness checks work.
- [ ] Three principal workflows can be demonstrated through the deployed MCP-centric architecture.
- [ ] Another user completes three tasks.
- [ ] Three coding problems completed.

### Week 7 stretch

- [ ] Add Terraform.
- [ ] Add a custom domain.
- [ ] Add a polished React shell.

---

# Week 8 — External integrations and MCP hardening

**Dates:** September 7–13  
**Capacity:** 12 hours  
**Goal:** Extend the canonical MCP server with two real external systems, then harden permissions, contracts, and documentation.

## Resources

- MCP Python SDK  
  https://py.sdk.modelcontextprotocol.io/
- Official MCP Python repository  
  https://github.com/modelcontextprotocol/python-sdk
- ADK Model Context Protocol documentation  
  https://adk.dev/mcp/
- Anthropic — Writing Effective Tools for Agents  
  https://www.anthropic.com/engineering/writing-tools-for-agents
- Official MCP Registry publishing quickstart  
  https://modelcontextprotocol.io/registry/quickstart

## Monday, September 7 — Integration and publication plan

- [ ] Review the existing MCP server’s tool inventory and permission model.
- [ ] Select two external integrations: one unstructured/document source and one structured source.
- [ ] Define authentication, pagination, rate limits, retries, schema mapping, and audit requirements for each.
- [ ] Identify which tools can later be sanitized and published publicly without customer or tenant data.

## Tuesday, September 8 — Expand canonical MCP contracts + coding

- [ ] Refactor any tool logic that still exists outside the MCP server.
- [ ] Add or refine lead lookup and capacity lookup contracts.
- [ ] Add Pydantic validation and stable structured error codes.
- [ ] Add a backward-compatible tool-version field or documented versioning policy.
- [ ] Solve **Subtree of Another Tree**.  
  https://leetcode.com/problems/subtree-of-another-tree/

## Wednesday, September 9 — Document integration

- [ ] Connect Cloud Storage, Google Drive, or another document source through MCP.
- [ ] Handle pagination or continuation tokens.
- [ ] Preserve source permissions, tenant/role metadata, and provenance.
- [ ] Add retry behavior and an integration test.
- [ ] Confirm the integration can feed both dense and graph-augmented retrieval paths.

## Thursday, September 10 — Structured integration + deployment-evidence workshop

- [ ] Connect Google Sheets, BigQuery, or a structured external source through MCP.
- [ ] Map the external schema to the canonical model.
- [ ] Handle invalid, duplicate, missing, and stale fields.
- [ ] Deployment-evidence scenario: a user environment has a legacy API with missing documentation and strict rate limits.
- [ ] Write discovery questions, assumptions, integration risks, and a safe pilot plan.

## Friday, September 11 — Contract and permission testing

- [ ] Add contract tests for every MCP tool schema.
- [ ] Add denied-permission and cross-tenant tests.
- [ ] Add invalid-argument and rate-limit tests.
- [ ] Ensure tool errors do not expose credentials or internal stack traces.
- [ ] Confirm ADK receives the same stable MCP contracts used by any future client.

## Saturday, September 12 — End-to-end integration benchmark + coding

- [ ] Run the existing 20-task benchmark through the two external integrations.
- [ ] Measure added latency, retry rate, tool errors, and task success.
- [ ] Document integration-specific failure handling and maintainability tradeoffs.
- [ ] Begin a sanitized public package boundary for the publishable MCP server subset.
- [ ] Solve **Lowest Common Ancestor of a BST**.  
  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- [ ] Solve **Kth Largest Element in an Array**.  
  https://leetcode.com/problems/kth-largest-element-in-an-array/

## Sunday, September 13 — Integration demo and registry-ready design

- [ ] Write complete MCP tool documentation for external users.
- [ ] Draw the canonical MCP integration boundary and show ADK as one consumer.
- [ ] Record a demo showing both external systems.
- [ ] Commit the MCP server as a separately testable package or repository boundary.
- [ ] Write a one-page reusable-component description and a registry-publication checklist.

### Week 8 must-pass

- [ ] Canonical MCP server remains the single source of tool truth.
- [ ] At least six typed MCP tools work.
- [ ] At least two external integrations work.
- [ ] Contract, permission, tenant, and error tests pass.
- [ ] ADK consumes the integrations through MCP without duplicated tool logic.
- [ ] Public sanitization and packaging plan exists.
- [ ] Three coding problems completed.

### Week 8 stretch

- [ ] Add automated backward-compatibility tests.
- [ ] Add per-tool rate limits.
- [ ] Create the first draft of `server.json` for the official MCP Registry.

# Week 9 — Durable execution and state management

**Dates:** September 14–20  
**Capacity:** 12 hours  
**Goal:** Agent runs survive failures without duplicating side effects.

## Resources

- ADK state documentation  
  https://adk.dev/sessions/state/
- Google agent platform scaling and sessions  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale
- Temporal workflow concepts  
  https://docs.temporal.io/workflows
- Google Cloud Well-Architected reliability guidance  
  https://docs.cloud.google.com/architecture/framework/reliability

## Monday, September 14 — State design

- [ ] Separate conversational state, workflow state, durable business state, and audit history.
- [ ] Draw the run-state machine.
- [ ] Define terminal and recoverable states.
- [ ] Define what must survive process restarts.

## Tuesday, September 15 — Persistent runs + coding

- [ ] Create agent_run and agent_step tables.
- [ ] Persist state transitions.
- [ ] Add correlation and idempotency keys.
- [ ] Solve **Merge Intervals**.  
  https://leetcode.com/problems/merge-intervals/

## Wednesday, September 16 — Checkpoint and resume

- [ ] Add checkpoint creation after meaningful steps.
- [ ] Add resume from the last valid checkpoint.
- [ ] Reject invalid state transitions.
- [ ] Add tests for process restart.

## Thursday, September 17 — Retry and timeout design

- [ ] Add retry categories: transient, permanent, authorization, validation.
- [ ] Add exponential backoff with limits.
- [ ] Add tool-level timeout and cancellation.
- [ ] System-design prompt: design durable execution for an AI workflow that may call external APIs.
- [ ] Explain at-least-once versus exactly-once behavior.

## Friday, September 18 — Dead-letter and diagnosis

- [ ] Add dead-letter status and reason.
- [ ] Add an operator-readable failure summary.
- [ ] Add replay protection.
- [ ] Document manual recovery steps.

## Saturday, September 19 — Failure injection + coding

- [ ] Inject model timeout.
- [ ] Inject external API failure.
- [ ] Inject database disconnection.
- [ ] Verify recovery without duplicate tasks.
- [ ] Record recovery metrics.
- [ ] Solve **Insert Interval**.  
  https://leetcode.com/problems/insert-interval/
- [ ] Solve **Number of Islands**.  
  https://leetcode.com/problems/number-of-islands/

## Sunday, September 20 — Incident walkthrough

- [ ] Record a demo of a failed run resuming correctly.
- [ ] Write a production-incident interview story.
- [ ] Explain why idempotency is more important than “agent intelligence” for write actions.
- [ ] Commit and update the runbook.

### Week 9 must-pass

- [ ] State machine and persistent runs exist.
- [ ] Checkpoint/resume works.
- [ ] Retry and timeout behavior is bounded.
- [ ] Duplicate side effects are prevented.
- [ ] Failure injection tests pass.
- [ ] Three coding problems completed.

### Week 9 stretch

- [ ] Build a randomized chaos-test script.
- [ ] Add operator controls for replay and cancellation.
- [ ] Add state-size and resume-latency metrics.

---

# Week 10 — Human approval, identity, and AI security

**Dates:** September 21–27  
**Capacity:** 12 hours  
**Goal:** No sensitive action can occur without authorization, approval, and an audit record.

## Resources

- OWASP GenAI / LLM Top 10  
  https://genai.owasp.org/llm-top-10/
- Secret Manager quickstart  
  https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart
- Google Cloud IAM overview  
  https://docs.cloud.google.com/iam/docs/overview
- Google Cloud Well-Architected security guidance  
  https://docs.cloud.google.com/architecture/framework/security

## Monday, September 21 — Threat model

- [ ] Identify assets, actors, trust boundaries, and sensitive actions.
- [ ] Map prompt injection, data leakage, excessive agency, insecure output, and tenant leakage.
- [ ] Define mitigations at the application and infrastructure layers.
- [ ] Write `docs/threat_model.md`.

## Tuesday, September 22 — Write tools + coding

- [ ] Add task creation as a write tool.
- [ ] Add communication drafting as a write tool.
- [ ] Make both produce a pending approval request.
- [ ] Solve **Clone Graph**.  
  https://leetcode.com/problems/clone-graph/

## Wednesday, September 23 — Approval workflow

- [ ] Create approval-request data model.
- [ ] Store proposed action, evidence, initiator, risk level, and expiration.
- [ ] Add approve and reject endpoints.
- [ ] Validate that approved arguments have not changed.

## Thursday, September 24 — Authorization and customer pushback

- [ ] Implement role checks for approvers.
- [ ] Enforce tenant checks at every write boundary.
- [ ] Deployment-evidence scenario: a customer wants launch despite unsafe evaluation results.
- [ ] Prepare a response using evidence, a limited pilot, and explicit launch conditions.

## Friday, September 25 — Secrets and audit

- [ ] Move production secrets to Secret Manager.
- [ ] Confirm the Cloud Run service account has only required access.
- [ ] Record actor, action, evidence, approval, result, and timestamp.
- [ ] Add audit-query endpoints.

## Saturday, September 26 — Adversarial tests + coding

- [ ] Create direct prompt-injection tests.
- [ ] Create indirect injection in retrieved documents.
- [ ] Test unauthorized tool calls.
- [ ] Test cross-tenant retrieval and writes.
- [ ] Test malicious tool arguments.
- [ ] Solve **Course Schedule**.  
  https://leetcode.com/problems/course-schedule/
- [ ] Solve **Rotting Oranges**.  
  https://leetcode.com/problems/rotting-oranges/

## Sunday, September 27 — Security review

- [ ] Run the complete authorization and adversarial suite.
- [ ] Demonstrate an attack being blocked.
- [ ] Demonstrate an approved action being executed once.
- [ ] Record a security-demo video.
- [ ] Commit the threat model and test report.
- [ ] Draft the interview story: “A security boundary prevented unsafe action.”

### Week 10 must-pass

- [ ] Sensitive actions require approval.
- [ ] Approval cannot be reused or modified.
- [ ] Authorization and tenant checks pass.
- [ ] Secrets are handled securely.
- [ ] Audit trail is complete.
- [ ] Adversarial tests include direct and indirect injection.
- [ ] Three coding problems completed.

### Week 10 stretch

- [ ] Add configurable approval policies.
- [ ] Add approval expiration.
- [ ] Add private networking design documentation.

---

# Week 11 — Evaluation engineering and observability

**Dates:** September 28–October 4  
**Capacity:** 12 hours  
**Goal:** A repeatable evaluation pipeline and production-quality traces, metrics, and dashboards.

## Resources

- Vertex AI Gen AI evaluation overview  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Evaluate AI agents  
  https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-agents
- Google Cloud agent observability  
  https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability
- DeepLearning.AI Advanced RAG evaluation  
  https://www.deeplearning.ai/courses/building-evaluating-advanced-rag/

## Monday, September 28 — Evaluation design

- [ ] Define evaluation categories and expected behavior.
- [ ] Add baseline-dense versus graph-augmented retrieval as a first-class comparison dimension.
- [ ] Define deterministic checks versus model-based graders.
- [ ] Define release-blocking metrics.
- [ ] Create an evaluation-data schema.

## Tuesday, September 29 — Expand benchmark + coding

- [ ] Expand the benchmark to 50–60 high-quality cases while preserving the 30-question dual-retrieval subset.
- [ ] Add ambiguity, missing data, tool failure, policy violation, injection, authorization, and multi-hop cases.
- [ ] Define expected final answer and expected tool trajectory where possible.
- [ ] Solve **Pacific Atlantic Water Flow**.  
  https://leetcode.com/problems/pacific-atlantic-water-flow/

## Wednesday, September 30 — Deterministic evaluators

- [ ] Implement task-completion checks.
- [ ] Implement tool-selection and argument checks.
- [ ] Implement citation and unauthorized-action checks.
- [ ] Implement path-specific retrieval hit rate, faithfulness, and citation-correctness aggregation.
- [ ] Implement cost and latency aggregation.

## Thursday, October 1 — Vertex evaluation + AI system design

- [ ] Run a small evaluation through Vertex AI’s evaluation service.
- [ ] Compare final-response and trajectory evaluation.
- [ ] AI system-design prompt: design a continuous evaluation platform for enterprise agents.
- [ ] Discuss sampling, labeling, regression gates, cost, and privacy.

## Friday, October 2 — Cloud observability

- [ ] Add structured logs with request, tenant, run, model, prompt version, and tool IDs.
- [ ] Add traces across API, model call, retrieval, and tool execution.
- [ ] Add metrics for latency, tokens, model calls, tool calls, retries, and errors.
- [ ] Ensure sensitive prompts are handled according to your logging policy.

## Saturday, October 3 — Dashboard and regression gates + coding

- [ ] Build dashboards for task success, p95 latency, cost per request, cost per successful task, and dense-versus-graph retrieval quality.
- [ ] Add CI evaluation for a smaller release-blocking subset.
- [ ] Define thresholds and failure behavior.
- [ ] Run the full benchmark and categorize failures.
- [ ] Solve **Graph Valid Tree**.  
  https://leetcode.com/problems/graph-valid-tree/
- [ ] Solve **Subsets**.  
  https://leetcode.com/problems/subsets/

## Sunday, October 4 — Evaluation report and mock

- [ ] Publish the first formal evaluation report with the measured Graph-versus-vanilla comparison as a headline section.
- [ ] Select one failure and document root cause and fix.
- [ ] Complete one 45-minute coding mock using an unseen medium problem.
- [ ] Record a 10-minute project deep dive focused on evaluation.
- [ ] Commit dashboards, metrics, and report.

### Week 11 must-pass

- [ ] Fifty or more strong evaluation cases exist.
- [ ] Deterministic checks run automatically.
- [ ] Final-response, trajectory, and dense-versus-graph retrieval quality are measured.
- [ ] Logs, traces, and metrics exist.
- [ ] Release-blocking subset runs in CI.
- [ ] Two coding problems plus one mock completed.

### Week 11 stretch

- [ ] Cross-check model graders with human labels.
- [ ] Add per-category dashboards.
- [ ] Add production-sampled evaluation.

---

# Week 12 — Multi-agent decision and bounded reflection

**Dates:** October 5–11  
**Capacity:** 12 hours  
**Goal:** Add multi-agent behavior only where evidence shows it improves outcomes.

## Resources

- Google Cloud multi-agent architecture  
  https://docs.cloud.google.com/architecture/multiagent-ai-system
- ADK multi-agent documentation  
  https://adk.dev/agents/multi-agents/
- Anthropic — Building Effective Agents  
  https://www.anthropic.com/engineering/building-effective-agents

## Monday, October 5 — Diagnose the single agent

- [ ] Review benchmark failures caused by context overload, tool confusion, conflicting instructions, or specialization needs.
- [ ] Identify no more than two justified specialist boundaries.
- [ ] Define a hypothesis for how multi-agent architecture will help.
- [ ] Define the metrics required to accept the change.

## Tuesday, October 6 — Specialist agent + coding

- [ ] Create one specialist ADK consumer for support or revenue.
- [ ] Keep tools least-privileged and available only through the canonical MCP server.
- [ ] Add explicit handoff input and output contracts.
- [ ] Solve **Combination Sum**.  
  https://leetcode.com/problems/combination-sum/

## Wednesday, October 7 — Orchestration

- [ ] Create a root ADK consumer or deterministic router over the same MCP tools.
- [ ] Add handoff termination and failure behavior.
- [ ] Add trace IDs across handoffs.
- [ ] Add tests for incorrect delegation.

## Thursday, October 8 — Reflection experiment + customer explanation

- [ ] Add one bounded evaluator-reviser cycle for a high-risk recommendation.
- [ ] Limit it to one critique and one revision.
- [ ] Measure quality, token cost, and latency.
- [ ] Product/deployment scenario: explain why a request for “five cooperating agents” may not be justified.
- [ ] Recommend the simplest architecture that meets success criteria.

## Friday, October 9 — Comparative evaluation

- [ ] Run the same benchmark on single-agent and multi-agent variants.
- [ ] Compare task success, cost, latency, unnecessary calls, and maintainability.
- [ ] Identify tasks where multi-agent behavior harms performance.
- [ ] Decide which architecture remains default.

## Saturday, October 10 — Decision report + coding

- [ ] Write the single-agent versus multi-agent decision report.
- [ ] Remove unnecessary multi-agent behavior.
- [ ] Document the reflection experiment.
- [ ] Solve **Permutations**.  
  https://leetcode.com/problems/permutations/
- [ ] Solve **House Robber**.  
  https://leetcode.com/problems/house-robber/

## Sunday, October 11 — Thin portability proof and architecture mock

- [ ] Time-box a thin non-Google consumer to no more than three hours: Claude Agent SDK or a plain MCP client harness.
- [ ] Connect it to the SAME canonical MCP server; do not recreate tools or build a second full agent system.
- [ ] Run a fixed 15-case subset of the benchmark and record task success, tool-contract compatibility, latency, and integration effort.
- [ ] Add the vendor-neutrality results to the architecture decision report.
- [ ] Complete a 45-minute AI system-design mock.
- [ ] Prompt: design an MCP-centric, multi-tenant agentic operations platform on GCP with ADK as one replaceable consumer.
- [ ] Record a demo comparing single-agent, justified multi-agent, and thin second-consumer behavior.
- [ ] Commit the decision and portability report.

### Week 12 must-pass

- [ ] Multi-agent architecture is justified by a specific failure hypothesis.
- [ ] One specialist and one orchestration path work.
- [ ] Bounded reflection is measured.
- [ ] Single-agent and multi-agent results are compared.
- [ ] Default architecture is chosen based on evidence.
- [ ] A thin non-Google consumer runs the same MCP tools across a 15-case benchmark subset.
- [ ] The portability work is capped at approximately three hours and does not duplicate the system.
- [ ] Three coding problems completed.

### Week 12 stretch

- [ ] Add safe parallel execution.
- [ ] Add another specialist only if evidence supports it.
- [ ] Package the thin portability harness for repeatable local execution.

---

# Week 13 — React interface, pilot, and adoption measurement

**Dates:** October 12–18  
**Capacity:** 12 hours  
**Goal:** A usable product, real-user pilot, and portfolio-ready release.

## Resources

- React official learning guide  
  https://react.dev/learn
- Google Cloud Well-Architected Framework  
  https://docs.cloud.google.com/architecture/framework
- IDEO interview method  
  https://www.designkit.org/methods/interview.html
- Official MCP Registry publishing quickstart  
  https://modelcontextprotocol.io/registry/quickstart

## Monday, October 12 — User flow and UI plan

- [ ] Draw the end-to-end user flow.
- [ ] Define pages: login, lead/work item, grounded Q&A, agent run, approval inbox, audit history, metrics.
- [ ] Define loading, refusal, error, and retry states.
- [ ] Select the minimum interface needed for the pilot.

## Tuesday, October 13 — React shell + coding

- [ ] Create the React/TypeScript frontend.
- [ ] Add API client and configuration.
- [ ] Add authentication flow or a clearly bounded demo authentication system.
- [ ] Add tenant-aware navigation.
- [ ] Solve **Coin Change**.  
  https://leetcode.com/problems/coin-change/

## Wednesday, October 14 — Core experience

- [ ] Add grounded Q&A with citations.
- [ ] Add agent progress and tool activity.
- [ ] Add approval inbox.
- [ ] Add clear error and escalation states.

## Thursday, October 15 — Pilot preparation and system design

- [ ] Write five realistic pilot tasks.
- [ ] Create a short user instruction sheet.
- [ ] Define measurements: completion time, success, acceptance, edits, escalation, and satisfaction.
- [ ] System-design prompt: design an enterprise AI pilot that can safely progress to production.
- [ ] Discuss rollout stages and launch gates.

## Friday, October 16 — Pilot session

- [ ] Observe at least one user completing five tasks.
- [ ] Do not intervene unless blocked.
- [ ] Record errors, confusion, workarounds, and comments.
- [ ] Ask what would make the user return.

## Saturday, October 17 — Fixes, portfolio, and coding

- [ ] Fix the two highest-impact usability problems.
- [ ] Calculate initial productivity or quality improvement.
- [ ] Prepare architecture, threat model, evaluation, pilot, and Graph-versus-vanilla retrieval visuals.
- [ ] Sanitize the publishable MCP server subset: remove tenant data, secrets, internal endpoints, and domain-specific private configuration.
- [ ] Finalize public README, license, package metadata, examples, security notes, and `server.json`.
- [ ] Solve **Longest Increasing Subsequence**.  
  https://leetcode.com/problems/longest-increasing-subsequence/
- [ ] Solve **Word Break**.  
  https://leetcode.com/problems/word-break/

## Sunday, October 18 — Portfolio-ready release

- [ ] Record a 5–8 minute customer-oriented demo.
- [ ] Record a 15–20 minute technical walkthrough.
- [ ] Publish or package:
  - discovery brief,
  - data-readiness report,
  - architecture,
  - evaluation report with headline Graph-versus-vanilla results,
  - `docs/retrieval-comparison.md`,
  - security threat model,
  - single-versus-multi-agent decision,
  - cost/latency report,
  - pilot feedback,
  - runbook,
  - sanitized public MCP server repository,
  - thin second-consumer portability report,
  - product-feedback memo.
- [ ] Publish the sanitized MCP server repository.
- [ ] Submit the server metadata to the official MCP Registry using the official publishing quickstart.
- [ ] Record the repository URL, registry namespace, submission result, and verification evidence.
- [ ] Tag release `v1.0`.
- [ ] Update résumé and LinkedIn project sections.
- [ ] Create a 30-company target list.

### Week 13 must-pass

- [ ] React interface supports the complete pilot flow.
- [ ] At least one user completes five tasks.
- [ ] User feedback is incorporated.
- [ ] Evaluation, Graph-versus-vanilla, security, architecture, portability, and pilot artifacts exist.
- [ ] Sanitized MCP server repository is public and submitted to the official MCP Registry.
- [ ] Public or shareable demo exists.
- [ ] Two coding problems completed.

### Week 13 stretch

- [ ] Add a second pilot user.
- [ ] Add a polished public case-study page.
- [ ] Automate future registry publication through GitHub Actions.

---

# Week 14 — Production hardening and Applied AI applications

**Dates:** October 19–25  
**Capacity:** 12 hours  
**Goal:** Production readiness plus simultaneous interview and application preparation.

## Resources

- Google Cloud operational excellence  
  https://docs.cloud.google.com/architecture/framework/operational-excellence
- Google Cloud agent observability  
  https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability
- ByteByteGo  
  https://www.youtube.com/@ByteByteGo
- Google Careers resources  
  https://www.google.com/about/careers/applications/buildyourfuture/resources/

## Monday, October 19 — SLOs and operations

- [ ] Define availability, p95 latency, task success, unauthorized action, and recovery objectives.
- [ ] Add alert thresholds.
- [ ] Add an operational dashboard checklist.
- [ ] Review cost per successful task.

## Tuesday, October 20 — Backup, restore, rollback + coding mock

- [ ] Test database backup and restore.
- [ ] Demonstrate deployment rollback.
- [ ] Document RTO and RPO assumptions.
- [ ] Complete a 45-minute coding mock.
- [ ] Review communication, correctness, complexity, and testing.

## Wednesday, October 21 — Load and failure test

- [ ] Run a small load test.
- [ ] Measure p50 and p95 latency.
- [ ] Identify model, retrieval, database, and integration bottlenecks.
- [ ] Fix one bottleneck or document the tradeoff.

## Thursday, October 22 — Primary résumé and secondary variant

- [ ] Create the primary **Applied AI Engineer** résumé focused on product ownership, AI quality, reliability, reusable systems, and user outcomes.
- [ ] Create a secondary **AI Deployment Engineer / engineering-heavy FDE** variant using the same evidence with greater emphasis on discovery, integrations, pilot delivery, and customer constraints.
- [ ] Create a five-minute executive project walkthrough.
- [ ] Create a twenty-minute technical walkthrough.
- [ ] Rehearse both once.

## Friday, October 23 — Applications and referrals

- [ ] Submit two highly targeted applications.
- [ ] Send two referral or networking messages.
- [ ] Tailor each message first to product-engineering requirements; use deployment evidence only where the role asks for customer or field delivery.
- [ ] Track applications in a spreadsheet.

## Saturday, October 24 — System-design mock and mixed coding

- [ ] Complete one AI system-design mock.
- [ ] Complete two unseen medium coding problems.
- [ ] Review your strongest and weakest topic.
- [ ] Update the interview weakness register.

## Sunday, October 25 — Full production review

- [ ] Run the complete production-readiness checklist.
- [ ] Perform one recovery drill.
- [ ] Record the final production demo.
- [ ] Submit three more targeted applications.
- [ ] Commit all operations documents.

### Week 14 must-pass

- [ ] SLOs, alerts, backup/restore, and rollback are demonstrated.
- [ ] Primary Applied AI Engineer résumé and secondary deployment/FDE variant exist.
- [ ] One coding mock and one system-design mock completed.
- [ ] Five applications and two networking messages completed.

### Week 14 stretch

- [ ] Add Terraform for remaining manual resources.
- [ ] Add blue/green deployment.
- [ ] Publish a technical article about deterministic controls.

---

# Week 15 — Applied AI and technical interview sprint

**Dates:** October 26–November 1  
**Capacity:** 12 hours  
**Goal:** Practice the actual interview loop rather than continuing to add features.

## Resources

- Google Careers interview-preparation resources  
  https://www.google.com/about/careers/applications/buildyourfuture/resources/
- Google mock coding question  
  https://www.youtube.com/watch?v=Ti5vfu9arXQ
- Gaurav Sen system-design playlist  
  https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX
- Tech Interview Handbook  
  https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/

## Monday, October 26 — Behavioral story bank

- [ ] Prepare eight stories:
  - ambiguity,
  - customer discovery,
  - difficult stakeholder,
  - technical tradeoff,
  - production failure,
  - unsafe request,
  - reusable solution,
  - measurable impact.
- [ ] Write each in Situation–Task–Action–Result–Learning format.
- [ ] Ensure your personal contribution is explicit.

## Tuesday, October 27 — Coding mock 1

- [ ] Complete a 45-minute coding mock.
- [ ] Clarify, propose brute force, optimize, code, test, and analyze.
- [ ] Re-solve the problem cleanly after the mock.
- [ ] Record repeated mistakes.

## Wednesday, October 28 — Deployment-evidence discovery mock

- [ ] Role-play a customer asking for an undefined support agent.
- [ ] Ask questions about users, workflow, data, security, success, and rollout.
- [ ] Propose a narrow pilot.
- [ ] Define measurable launch conditions.
- [ ] Review whether you led with the problem rather than technology.

## Thursday, October 29 — AI system-design mock

- [ ] Design an enterprise RAG and agent system.
- [ ] Cover ingestion, retrieval, tools, state, security, evaluation, observability, cost, and deployment.
- [ ] Record the mock.
- [ ] Review requirement clarification and tradeoff quality.

## Friday, October 30 — Project deep dive

- [ ] Present OpsPilot for twenty minutes.
- [ ] Answer:
  - Why this problem?
  - Why agent?
  - Why MCP-centric?
  - Why ADK as one consumer?
  - What failed?
  - How did you measure quality?
  - How did you secure actions?
  - What business value was observed?
- [ ] Shorten any rambling section.

## Saturday, October 31 — Practical take-home simulation

- [ ] Time-box four hours.
- [ ] Build a small AI workflow from an ambiguous brief.
- [ ] Document assumptions.
- [ ] Add tests and a README.
- [ ] Present the result in five minutes.
- [ ] Do not reuse OpsPilot code blindly.

## Sunday, November 1 — Coding mock 2 and applications

- [ ] Complete a second 45-minute coding mock.
- [ ] Review both mock scores.
- [ ] Submit five targeted applications.
- [ ] Send two referral requests.
- [ ] Update the weakness register and next-week correction plan.

### Week 15 must-pass

- [ ] Eight behavioral stories prepared.
- [ ] Two coding mocks completed.
- [ ] One discovery mock completed.
- [ ] One system-design mock completed.
- [ ] One take-home simulation completed.
- [ ] Five applications and two referral requests completed.

### Week 15 stretch

- [ ] Conduct one mock with a real engineer.
- [ ] Publish an article on the single-agent versus multi-agent decision.
- [ ] Contribute a documentation improvement to an open-source tool used in the project.

---

# Week 16 — Full interview-loop readiness

**Dates:** November 2–8  
**Capacity:** 12 hours  
**Goal:** Complete two realistic loops, fix weaknesses, and finalize the application package.

## Monday, November 2 — Loop 1: coding and behavioral

- [ ] Complete one 45-minute coding round.
- [ ] Complete one 45-minute behavioral round.
- [ ] Score requirement clarification, technical correctness, communication, and evidence.
- [ ] Write corrective actions.

## Tuesday, November 3 — Loop 1: system design and project

- [ ] Complete one 60-minute AI system-design round.
- [ ] Complete one 45-minute project deep dive.
- [ ] Review whether you discussed security, evaluation, operations, and adoption.
- [ ] Correct one weak answer immediately.

## Wednesday, November 4 — Additional coding mock

- [ ] Complete one additional 45-minute coding mock using an unseen medium problem.
- [ ] Clarify requirements, state brute force, optimize, code, test, and analyze complexity.
- [ ] Re-solve the problem cleanly after the mock.
- [ ] Compare recurring mistakes with the Week 15 coding mocks and update the weakness register.

## Thursday, November 5 — Weakness correction

- [ ] Re-solve two coding patterns that caused difficulty.
- [ ] Redesign one weak system-design area.
- [ ] Rewrite one weak behavioral story.
- [ ] Rehearse the executive and technical OpsPilot walkthroughs.

## Friday, November 6 — Loop 2: condensed mock

- [ ] Complete one coding round.
- [ ] Complete one 45-minute system-design round.
- [ ] Complete one additional 30-minute AI system-design round focused on evaluation, retrieval, or MCP tool architecture.
- [ ] Compare Loop 2 scores with Loop 1.

## Saturday, November 7 — Final application package and adoption signals

- [ ] Check and record adoption signals for the public MCP artifact: GitHub stars, clones/traffic, forks, issues, registry visibility/views where available, and external feedback.
- [ ] Add the measured adoption signal—or an honest zero-baseline—to the interview evidence file.
- [ ] Finalize both résumés.
- [ ] Finalize LinkedIn and GitHub.
- [ ] Confirm the demo and documentation links work.
- [ ] Create a one-page target-role scorecard.
- [ ] Submit five targeted applications.
- [ ] Send three networking messages.

## Sunday, November 8 — Readiness decision

- [ ] Run the final hiring scorecard below.
- [ ] Record a final five-minute executive demo.
- [ ] Record a final twenty-minute technical deep dive.
- [ ] List remaining gaps honestly.
- [ ] Create a maintenance cadence: two coding sessions, one system-design session, and applications each week.
- [ ] Tag the final portfolio release.

### Week 16 must-pass

- [ ] Three coding rounds completed.
- [ ] Three system-design rounds completed.
- [ ] One behavioral round completed; the single deployment/customer scenario was completed in Week 15.
- [ ] One project deep dive completed.
- [ ] Weaknesses corrected and rescored.
- [ ] Public MCP adoption signals are recorded as an interview data point.
- [ ] Application package finalized.
- [ ] Five applications and three networking messages completed.

---

# Final Applied AI Engineer hiring scorecard

## Applied AI product engineering

- [ ] Python code is typed, tested, and clearly structured.
- [ ] FastAPI, PostgreSQL, migrations, Docker, and CI work.
- [ ] GCP deployment is authenticated and observable.
- [ ] Structured and unstructured ingestion works.
- [ ] Tenant-safe baseline and graph-augmented RAG paths work with citations.
- [ ] Measured Graph-versus-vanilla retrieval results exist.
- [ ] MCP is the canonical typed tool layer.
- [ ] ADK is a bounded consumer of the MCP layer rather than the tool source of truth.
- [ ] A thin non-Google MCP consumer passes the 15-case portability subset.
- [ ] Persistent state, retries, timeouts, and idempotency work.
- [ ] Sensitive actions require human approval.
- [ ] Security and tenant-isolation tests pass.
- [ ] Evaluation runs automatically.
- [ ] Cost, latency, token, and success metrics are visible.
- [ ] Backup, restore, rollback, and a runbook exist.

## Deployment evidence supporting Applied AI candidacy

- [ ] Customer/user discovery brief exists.
- [ ] Current-state workflow and pain points are documented.
- [ ] Data-readiness report exists.
- [ ] Pilot scope and success metrics exist.
- [ ] User feedback is documented.
- [ ] Adoption or productivity result is measured.
- [ ] Sanitized reusable MCP component is public and submitted to the official registry.
- [ ] Public adoption signals are recorded honestly.
- [ ] Product-feedback memo exists.
- [ ] Executive and technical presentations are ready.
- [ ] You can explain tradeoffs without hiding limitations.

## Interview readiness

- [ ] At least 35–45 focused coding problems completed.
- [ ] At least seven timed coding rounds completed.
- [ ] At least five AI/system-design mocks completed.
- [ ] One deployment/customer discovery scenario completed.
- [ ] Eight behavioral stories are polished.
- [ ] Five-minute and twenty-minute project walkthroughs are ready.
- [ ] You can debug code and communicate while coding.
- [ ] You can discuss dual-path RAG, graph tradeoffs, agents, MCP-centric architecture, evaluation, security, state, cloud, cost, and rollout.
- [ ] You have an active application and networking pipeline.

---

# Rules for coding interview practice

For every coding problem:

- [ ] Restate the problem.
- [ ] Ask clarifying questions.
- [ ] Give one small example.
- [ ] State a brute-force solution.
- [ ] Explain the improved approach.
- [ ] Write clean Python without copying.
- [ ] Test normal and edge cases.
- [ ] State time and space complexity.
- [ ] Re-solve failed problems within 72 hours.

Do not chase hundreds of questions. Master patterns and communication.

---

# Standard AI system-design framework

Use this sequence in every design interview:

1. Clarify users, workflow, and success.
2. Define functional and non-functional requirements.
3. Define data sources, quality, ownership, and permissions.
4. Decide deterministic workflow versus agentic reasoning.
5. Design ingestion and retrieval.
6. Design model and tool interfaces.
7. Define state, memory, and idempotency.
8. Define authentication, authorization, and security.
9. Define evaluation and launch gates.
10. Define logs, traces, metrics, cost, and SLOs.
11. Define rollout, adoption, and human escalation.
12. Discuss tradeoffs and alternatives.

---

# Standard deployment-discovery framework

Use these categories in customer interviews:

## Problem and users

- [ ] Who performs the workflow?
- [ ] What triggers it?
- [ ] What is slow, expensive, or error-prone?
- [ ] What exceptions occur?

## Data and systems

- [ ] Which systems contain the required data?
- [ ] Who owns them?
- [ ] How fresh and complete is the data?
- [ ] What APIs, exports, or security perimeters exist?

## Risk and governance

- [ ] What actions are irreversible or high-risk?
- [ ] What requires human approval?
- [ ] What information is sensitive?
- [ ] What must be audited?

## Success and rollout

- [ ] What baseline exists?
- [ ] What measurable improvement matters?
- [ ] Who decides whether the pilot succeeds?
- [ ] What is the safest first production scope?
- [ ] How will users be trained and supported?

---

# The one rule

Every week ends with:

- [ ] A Git commit
- [ ] A short demo
- [ ] A written retrospective
- [ ] An updated interview weakness register

Watching does not count by itself. Notes do not count by themselves. Every concept must become code, a design decision, an evaluation, or an interview-ready explanation.
