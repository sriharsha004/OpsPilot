from app.models.pricing_rule import PricingRule
from app.repositories.base import TenantScopedRepository


class PricingRuleRepository(TenantScopedRepository[PricingRule]):
    model = PricingRule
