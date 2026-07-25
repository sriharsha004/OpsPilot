import uuid
from datetime import date

from pydantic import BaseModel, ConfigDict


class PricingRuleRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    tenant_id: uuid.UUID
    name: str
    description: str | None
    rule_type: str
    amount: float | None
    percentage: float | None
    conditions: dict[str, object] | None
    requires_approval: bool
    effective_from: date
    effective_until: date | None
