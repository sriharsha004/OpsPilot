# OpsPilot Authorization Rules v0

Tenancy is hierarchical (`franchisors` → `tenants`), so "the user's tenant" is not always a single fixed row — it depends on role and scope. These rules replace a flat "user.tenant_id == record.tenant_id" check with an authorized-scope check.

## Access scopes

| Role | Scope |
|---|---|
| `platform_admin` | Every tenant |
| `franchisor_admin` | Every tenant under their `franchisor_id` |
| `regional_admin` | Only tenants with an explicit `user_tenant_access` grant |
| `tenant_admin` / `tenant_user` | Only their `home_tenant_id` |

## Rules

1. Every business record must belong to a tenant.
2. A user may read only records belonging to a tenant within their authorized scope (see table above) — not necessarily one fixed tenant.
3. A tenant ID must come from the authenticated user context or an explicitly authorized route parameter, never trusted directly from an untrusted request body.
4. Tenant/scope filtering must occur in the repository or service layer, not only in the frontend.
5. Only authorized roles (e.g. `tenant_admin`, `franchisor_admin`, `platform_admin`) may approve communications, discounts, or other sensitive actions.
6. AI agents may recommend actions but may not bypass user permissions, choose their own tenant scope, or send/close/approve on their own — the backend hands them an already-authorized scope.
7. Sensitive actions must create an audit event.
8. Documents and document chunks must inherit tenant and access-level restrictions.
9. Cross-tenant requests outside a user's authorized scope must return a generic authorization error without exposing whether the requested record exists.
10. Background jobs, MCP tools, and agent runtimes must follow the same authorization rules as API users.
11. Selecting a tenant in the UI (e.g. a franchisor's location selector) does not itself grant access — the backend independently re-authorizes the requested `tenant_id` on every call.
12. Every cross-location view, export, or aggregation by a franchisor/regional/platform actor must be audited, including `actor_role`, `franchisor_id`, and a reason/session context.
13. Aggregated franchisor dashboards must preserve tenant identity in underlying records — never merge locations into anonymous totals before the audit/authorization boundary.
14. Franchisor-wide access may still exclude sensitive tenant-specific fields (e.g. individual family contact PII) at the API layer, independent of row-level tenant access.
15. A tenant admin/user must never access sibling tenants under the same franchisor without an explicit `user_tenant_access` grant.

## Authorization flow

```text
1. Authenticate the user.
2. Read the requested tenant ID from the route or active context.
3. Load the tenant and its franchisor ID.
4. Determine whether the user:
   - is a platform_admin,
   - is a franchisor_admin whose franchisor_id matches the tenant's franchisor_id,
   - has an explicit user_tenant_access grant for the tenant, or
   - has home_tenant_id == the requested tenant.
5. Apply the resolved tenant_id to every downstream query.
6. If the access was cross-tenant (not the user's home tenant), write an audit_events row.
```

Preferred API shape — scope is explicit in the path, not inferred from a query param:

```text
GET /franchisors/{franchisor_id}/dashboard
GET /tenants/{tenant_id}/leads
GET /tenants/{tenant_id}/capacity
```

rather than `GET /leads?tenant_id=...`, where the authorized scope is less obvious to reason about (and easier to get wrong).
