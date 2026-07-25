import uuid
from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class CapacityRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    tenant_id: uuid.UUID
    resource_name: str
    resource_type: str
    total_capacity: int
    used_capacity: int
    available_capacity: int
    effective_date: date
    updated_at: datetime
