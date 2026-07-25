import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import AuditAccessType, AuditResult, UserRole


class AuditEventRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    tenant_id: uuid.UUID
    user_id: uuid.UUID | None
    actor_role: UserRole | None
    franchisor_id: uuid.UUID | None
    agent_run_id: uuid.UUID | None
    action: str
    access_type: AuditAccessType | None
    resource_type: str
    resource_id: uuid.UUID
    request_data: dict[str, object] | None
    reason: str | None
    result: AuditResult
    timestamp: datetime
