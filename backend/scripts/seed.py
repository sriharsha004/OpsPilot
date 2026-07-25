"""Seed two sample tenants under one franchisor, with capacity, pricing,
leads, and a task each - so the API has something realistic to hit locally.

Usage (from backend/):
    python -m scripts.seed
"""

import datetime

from app.database.session import SessionLocal
from app.models.capacity import Capacity
from app.models.enums import LeadSource
from app.models.franchisor import Franchisor
from app.models.lead import Lead
from app.models.pricing_rule import PricingRule
from app.models.task import Task
from app.models.tenant import Tenant

FRANCHISOR_NAME = "Building Kidz Preschools"


def seed() -> None:
    db = SessionLocal()
    try:
        existing = db.query(Franchisor).filter_by(name=FRANCHISOR_NAME).first()
        if existing is not None:
            print(f"'{FRANCHISOR_NAME}' already seeded - skipping.")
            return

        franchisor = Franchisor(name=FRANCHISOR_NAME)
        db.add(franchisor)
        db.commit()
        db.refresh(franchisor)

        for tenant_name, room_name, room_seats in [
            ("Building Kidz - North Austin", "Toddler Room", 12),
            ("Building Kidz - South Austin", "Infant Room", 8),
        ]:
            tenant = Tenant(name=tenant_name, franchisor_id=franchisor.id)
            db.add(tenant)
            db.commit()
            db.refresh(tenant)

            db.add(
                Capacity(
                    tenant_id=tenant.id,
                    resource_name=room_name,
                    resource_type="classroom",
                    total_capacity=room_seats,
                    used_capacity=room_seats - 2,
                    available_capacity=2,
                    effective_date=datetime.date.today(),
                )
            )
            db.add(
                PricingRule(
                    tenant_id=tenant.id,
                    name="Sibling Discount",
                    description="10% off tuition for a second enrolled sibling",
                    rule_type="discount",
                    percentage=10,
                    requires_approval=False,
                    effective_from=datetime.date.today(),
                )
            )

            lead = Lead(
                tenant_id=tenant.id,
                name="Sample Parent",
                email="parent@example.com",
                source=LeadSource.WEBSITE_FORM,
            )
            db.add(lead)
            db.commit()
            db.refresh(lead)

            db.add(
                Task(
                    tenant_id=tenant.id,
                    lead_id=lead.id,
                    title="Call the lead within 24 hours",
                )
            )
            db.commit()

            print(f"Seeded tenant '{tenant_name}' with capacity, pricing rule, lead, and task.")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
