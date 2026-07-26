from app.models.lead import Lead
from app.repositories.base import TenantScopedRepository


class LeadRepository(TenantScopedRepository[Lead]):
    model = Lead
