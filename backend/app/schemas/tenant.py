import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.enums import EntityStatus


class TenantCreate(BaseModel):
    name: str
    franchisor_id: uuid.UUID | None = None


class TenantUpdate(BaseModel):
    name: str | None = None
    status: EntityStatus | None = None


class TenantRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    franchisor_id: uuid.UUID | None
    name: str
    status: EntityStatus
    created_at: datetime
    updated_at: datetime
