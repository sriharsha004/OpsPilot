from app.models.capacity import Capacity
from app.repositories.base import TenantScopedRepository


class CapacityRepository(TenantScopedRepository[Capacity]):
    model = Capacity
