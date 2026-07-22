# DB Schema v0 — OpsPilot (Hierarchical multi-tenant)

Tenancy is now two-level: a `franchisor` owns many `tenants` (locations). All business tables still carry `tenant_id` for row-level isolation; access to a given `tenant_id` is authorized via franchisor scope, explicit grants, or direct membership — see `authorization_rules.md`.

## franchisors
One row per franchise organization (e.g. "Building Kidz"). Groups multiple tenant locations under one owner.
- id (pk)
- name
- status
- created_at
- updated_at

## tenants
One row per business location using OpsPilot (e.g. one preschool campus). Everything else hangs off this for row-level isolation.
- id (pk)
- franchisor_id (fk → franchisors, nullable — null for a standalone, non-franchise business)
- name
- status
- created_at
- updated_at

## users
People who log into OpsPilot. A user is scoped by role: a `tenant_user`/`tenant_admin` belongs to one `home_tenant_id`; a `franchisor_admin` belongs to a `franchisor_id` and can reach every tenant under it; a `regional_admin` has no default scope and relies entirely on `user_tenant_access` grants; a `platform_admin` bypasses scoping.
- id (pk)
- franchisor_id (fk → franchisors, nullable — set for franchisor-scoped roles)
- home_tenant_id (fk → tenants, nullable — set for tenant-scoped roles)
- name
- email
- role (platform_admin | franchisor_admin | regional_admin | tenant_admin | tenant_user)
- is_active
- created_at

## user_tenant_access
Explicit per-tenant grants for users whose access doesn't come from `franchisor_id` or `home_tenant_id` alone — e.g. a regional manager covering two of a franchisor's locations, or a read-only auditor.
- id (pk)
- user_id (fk → users)
- tenant_id (fk → tenants)
- access_level (read | write | approve)
- created_at

## leads
The core object: one inbound inquiry, from first contact through converted/closed. Scoring, follow-up, and staleness all key off this table.
- id (pk)
- tenant_id (fk → tenants)
- name
- email
- phone
- source (fb_ads | ig_ads | google_ads | whatsapp | website_form | walk_in | referral)
- requested_service
- notes
- status (new | contacted | qualified | follow_up_required | converted | closed)
- score (nullable, AI-generated)
- assigned_to (fk → users, nullable)
- created_at
- updated_at

Staleness is not a stored status — compute "stale" as `updated_at > 48h ago AND status not in (converted, closed)`, since it's a moving condition, not a fact set once.

## capacity
Available operational capacity for a resource (classroom, appointment slot, service). The agent checks this before recommending a lead be accepted.
- id (pk)
- tenant_id (fk → tenants)
- resource_name
- resource_type
- total_capacity
- used_capacity
- available_capacity
- effective_date
- updated_at

## pricing_rules
Business rules for prices, discounts, fees, and promotions — the agent reads these but never invents pricing.
- id (pk)
- tenant_id (fk → tenants)
- name
- description
- rule_type
- amount
- percentage
- conditions
- requires_approval
- effective_from
- effective_until

## documents
Metadata for policies, playbooks, FAQs, and manuals used by the RAG system (chunked/embedded content lives elsewhere, e.g. a future `document_chunks` table).
- id (pk)
- tenant_id (fk → tenants)
- title
- source_uri
- document_type
- version
- checksum
- access_level
- created_at
- updated_at

## tasks
Work to be completed by a person — the agent may draft/suggest one, but creation of sensitive tasks may require approval.
- id (pk)
- tenant_id (fk → tenants)
- lead_id (fk → leads)
- title
- description
- status (open | done | skipped)
- priority
- assigned_user_id (fk → users, nullable)
- created_by
- due_date
- created_at
- completed_at (nullable)

## communications
Customer-facing messages and their history. The agent creates a draft; nothing sends without explicit approval.
- id (pk)
- tenant_id (fk → tenants)
- lead_id (fk → leads)
- channel (whatsapp | email | phone)
- subject
- body
- status (draft | pending_approval | approved | sent | rejected)
- created_by
- approved_by (fk → users, nullable) — required before status=sent
- sent_at (nullable)
- created_at

## audit_events
Append-only log of every action — human or agent — for security and accountability. Answers who/what/when/approved/result, and — for cross-tenant views — who looked at which location and why.
- id (pk)
- tenant_id (fk → tenants) — the tenant whose record was affected/viewed
- user_id (nullable — null when the actor is the agent)
- actor_role (nullable — role the actor was acting under, e.g. franchisor_admin)
- franchisor_id (nullable — set when access was authorized via franchisor scope)
- agent_run_id (nullable — set when the actor is the agent)
- action (e.g. lead_viewed, discount_proposed, message_approved, task_created, action_blocked, cross_tenant_view)
- access_type (summary | detail | export | modification | approval, nullable)
- resource_type
- resource_id
- request_data (jsonb, nullable)
- reason (nullable — session/support context for cross-tenant access)
- result
- timestamp

## Relationships
```text
Franchisor
├── Tenants
└── Users (franchisor-scoped)

Tenant
├── Users (home location)
├── Leads
├── Capacity records
├── Pricing rules
├── Documents
├── Tasks
├── Communications
├── Audit events
└── User_tenant_access grants

Lead
├── Tasks
├── Communications
└── Audit events

User
└── User_tenant_access grants
```

## Guardrail hooks (from problem_brief.md)
- `communications.status = sent` must have `approved_by` set — enforce at API layer, not DB constraint alone.
- `pricing_rules.requires_approval = true` (e.g. discounts above a threshold) must route through an approval step before use, logged to `audit_events`.
- `leads.status ∈ {converted, closed}` changes must always emit an `audit_events` row with a human `user_id`.
- No cross-tenant reads/writes except through an authorized scope (franchisor, `user_tenant_access`, or platform admin) — every query still scoped by `tenant_id`, just not always to a single fixed one. See `authorization_rules.md`.
- Every cross-tenant view (a franchisor/regional/platform actor reading a tenant that isn't their `home_tenant_id`) must write an `audit_events` row with `actor_role`, `franchisor_id`, and `reason` populated.

## Build order
1. `tenants`, `users`, `leads`, `capacity`, `pricing_rules`, `tasks`
2. `documents`, `communications`, `audit_events` — once RAG, approval, and agent capabilities come online
3. `franchisors`, `user_tenant_access` — once a franchise (multi-location) customer is onboarded; single-location tenants work fine with `franchisor_id`/`home_tenant_id` left null
