import uuid

from sqlalchemy.orm import Session

from app.database.base import Base


class TenantScopedRepository[ModelT: Base]:
    """CRUD helpers that always scope reads/writes to a single tenant.

    Every query goes through tenant_id - there is no method here that can
    return or touch a row belonging to a different tenant.
    """

    model: type[ModelT]

    def __init__(self, db: Session) -> None:
        self.db = db

    def get(self, tenant_id: uuid.UUID, id: uuid.UUID) -> ModelT | None:
        return (
            self.db.query(self.model)
            .filter_by(id=id, tenant_id=tenant_id)
            .first()
        )

    def list(self, tenant_id: uuid.UUID) -> list[ModelT]:
        return self.db.query(self.model).filter_by(tenant_id=tenant_id).all()

    def create(self, **fields: object) -> ModelT:
        obj = self.model(**fields)
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, obj: ModelT, **updates: object) -> ModelT:
        for key, value in updates.items():
            setattr(obj, key, value)
        self.db.commit()
        self.db.refresh(obj)
        return obj
