import uuid

from app.models.task import Task
from app.repositories.base import TenantScopedRepository


class TaskRepository(TenantScopedRepository[Task]):
    model = Task

    def get_for_lead(
        self, tenant_id: uuid.UUID, lead_id: uuid.UUID, task_id: uuid.UUID
    ) -> Task | None:
        return (
            self.db.query(Task)
            .filter_by(id=task_id, tenant_id=tenant_id, lead_id=lead_id)
            .first()
        )

    def list_for_lead(self, tenant_id: uuid.UUID, lead_id: uuid.UUID) -> list[Task]:
        return self.db.query(Task).filter_by(tenant_id=tenant_id, lead_id=lead_id).all()
