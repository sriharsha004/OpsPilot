from app.models.audit_event import AuditEvent
from app.repositories.base import TenantScopedRepository


class AuditEventRepository(TenantScopedRepository[AuditEvent]):
    model = AuditEvent
