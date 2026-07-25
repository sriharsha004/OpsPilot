import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import LeadSource, LeadStatus


class LeadCreate(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    source: LeadSource


class LeadUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    status: LeadStatus | None = None


class LeadRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    tenant_id: uuid.UUID
    name: str
    email: str | None
    phone: str | None
    source: LeadSource
    status: LeadStatus
    created_at: datetime
    updated_at: datetime
