import datetime
import uuid

from app.models.audit_event import AuditEvent
from app.models.capacity import Capacity
from app.models.enums import AuditResult
from app.models.pricing_rule import PricingRule
from app.models.tenant import Tenant


def test_list_capacity_scoped_to_tenant(client, db, tenant):
    other_tenant = Tenant(name="Other Tenant")
    db.add(other_tenant)
    db.commit()
    db.refresh(other_tenant)

    db.add(
        Capacity(
            tenant_id=tenant.id,
            resource_name="Toddler Room",
            resource_type="classroom",
            total_capacity=12,
            used_capacity=10,
            available_capacity=2,
            effective_date=datetime.date.today(),
        )
    )
    db.add(
        Capacity(
            tenant_id=other_tenant.id,
            resource_name="Infant Room",
            resource_type="classroom",
            total_capacity=8,
            used_capacity=8,
            available_capacity=0,
            effective_date=datetime.date.today(),
        )
    )
    db.commit()

    r = client.get(f"/tenants/{tenant.id}/capacity")
    assert r.status_code == 200
    body = r.json()
    assert len(body) == 1
    assert body[0]["resource_name"] == "Toddler Room"


def test_get_capacity_not_found(client, tenant):
    r = client.get(f"/tenants/{tenant.id}/capacity/{uuid.uuid4()}")
    assert r.status_code == 404


def test_list_pricing_rules_scoped_to_tenant(client, db, tenant):
    db.add(
        PricingRule(
            tenant_id=tenant.id,
            name="Sibling Discount",
            rule_type="discount",
            percentage=10,
            requires_approval=False,
            effective_from=datetime.date.today(),
        )
    )
    db.commit()

    r = client.get(f"/tenants/{tenant.id}/pricing-rules")
    assert r.status_code == 200
    assert len(r.json()) == 1
    assert r.json()[0]["name"] == "Sibling Discount"


def test_list_audit_events_scoped_to_tenant(client, db, tenant, user):
    db.add(
        AuditEvent(
            tenant_id=tenant.id,
            user_id=user.id,
            actor_role=user.role,
            action="lead_viewed",
            resource_type="lead",
            resource_id=uuid.uuid4(),
            result=AuditResult.SUCCESS,
        )
    )
    db.commit()

    r = client.get(f"/tenants/{tenant.id}/audit-events")
    assert r.status_code == 200
    assert len(r.json()) == 1
    assert r.json()[0]["action"] == "lead_viewed"
