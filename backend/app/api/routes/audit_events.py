import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.repositories.audit_event import AuditEventRepository
from app.schemas.audit_event import AuditEventRead

router = APIRouter(prefix="/tenants/{tenant_id}/audit-events", tags=["audit-events"])


@router.get("", response_model=list[AuditEventRead])
def list_audit_events(tenant_id: uuid.UUID, db: Session = Depends(get_db)) -> object:
    return AuditEventRepository(db).list(tenant_id)
