# Success Metrics v1

**Workflow:** Lead Handling  
**Version:** 1.0  
**Date:** 2026-07-19

---

## 1. Task Completion Rate

**Definition:** % of initiated tasks the agent completes without human correction or abandonment.

**Target:** ≥ 85% by end of Milestone 1

**Measurement:**
- Numerator: tasks where the agent produced a usable output (scored lead, drafted message, flagged stale lead)
- Denominator: all tasks initiated
- Tracked per task type (score / draft / flag)

**Failure signals:** agent returns an error, produces an empty output, or the user discards the output without using it

---

## 2. Grounded Answer Rate

**Definition:** % of agent outputs that cite or correctly reference the actual lead data in the GSheet (no hallucinated names, dates, or statuses).

**Target:** ≥ 95%

**Measurement:**
- Spot-check sampled outputs weekly against raw GSheet records
- Flag any output where lead name, inquiry date, channel, or contact detail doesn't match source

**Why it matters:** A drafted follow-up with the wrong child's name or wrong enquiry date destroys trust immediately.

---

## 3. Unauthorized Action Rate

**Definition:** % of agent actions that bypass the approval requirement (e.g. sending a message, updating a record, closing a lead without human sign-off).

**Target:** 0% — hard guardrail, no tolerance

**Measurement:**
- Log every action attempted by the agent
- Flag any action taken on an external system (GSheet write, WhatsApp send) without a preceding human approval event
- Reviewed on every deploy and audited weekly

---

## 4. Latency

**Definition:** Time from user triggering a task to agent returning a usable output.

**Targets:**

| Task | Target |
|------|--------|
| Score a lead | < 5 seconds |
| Draft a follow-up message | < 8 seconds |
| Flag stale leads (batch) | < 15 seconds |

**Measurement:** Instrument each agent call with start/end timestamps, log p50 and p95.

---

## 5. Cost Per Successful Task

**Definition:** Total LLM + infrastructure cost (USD) divided by number of successfully completed tasks.

**Target:** < $0.05 per task at launch; reduce to < $0.02 by Milestone 3

**Measurement:**
- Track Anthropic API token usage per task type
- Add GCP Cloud Run and other infra costs monthly
- Report weekly cost per task broken down by type

**Optimization levers:** prompt caching, shorter context windows, batching stale-lead checks

---

## 6. User Time Saved

**Definition:** Estimated minutes saved per week compared to the current fully manual process.

**Baseline (manual):**
- Lead entry: ~3 min/lead
- Follow-up drafting: ~5 min/lead
- Identifying stale leads: ~20 min/week manually scanning sheet

**Target:** Save ≥ 60 minutes/week for the admin team by end of Milestone 1

**Measurement:**
- Self-reported weekly by admin team (short Slack check-in or form)
- Validated by comparing # of leads processed per hour before and after

---

## Review Cadence

| Metric | Reviewed |
|--------|----------|
| Task completion rate | Weekly |
| Grounded answer rate | Weekly (spot-check) |
| Unauthorized action rate | Every deploy + weekly audit |
| Latency | Per release |
| Cost per task | Weekly |
| User time saved | Bi-weekly (user report) |
