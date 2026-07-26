import uuid

from sqlalchemy.orm import Session

from app.models.tenant import Tenant


class TenantRepository:
    """Not tenant-scoped like the others - a Tenant IS the tenant, there's
    no tenant_id column on this table to filter by."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get(self, id: uuid.UUID) -> Tenant | None:
        return self.db.get(Tenant, id)

    def create(self, **fields: object) -> Tenant:
        tenant = Tenant(**fields)
        self.db.add(tenant)
        self.db.commit()
        self.db.refresh(tenant)
        return tenant

    def update(self, tenant: Tenant, **updates: object) -> Tenant:
        for key, value in updates.items():
            setattr(tenant, key, value)
        self.db.commit()
        self.db.refresh(tenant)
        return tenant
