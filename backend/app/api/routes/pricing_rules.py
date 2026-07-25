import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.repositories.pricing_rule import PricingRuleRepository
from app.schemas.pricing_rule import PricingRuleRead

router = APIRouter(prefix="/tenants/{tenant_id}/pricing-rules", tags=["pricing-rules"])


@router.get("", response_model=list[PricingRuleRead])
def list_pricing_rules(tenant_id: uuid.UUID, db: Session = Depends(get_db)) -> object:
    return PricingRuleRepository(db).list(tenant_id)


@router.get("/{rule_id}", response_model=PricingRuleRead)
def get_pricing_rule(
    tenant_id: uuid.UUID, rule_id: uuid.UUID, db: Session = Depends(get_db)
) -> object:
    rule = PricingRuleRepository(db).get(tenant_id, rule_id)
    if rule is None:
        raise HTTPException(status_code=404, detail="Pricing rule not found")
    return rule
