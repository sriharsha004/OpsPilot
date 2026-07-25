import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.repositories.capacity import CapacityRepository
from app.schemas.capacity import CapacityRead

router = APIRouter(prefix="/tenants/{tenant_id}/capacity", tags=["capacity"])


@router.get("", response_model=list[CapacityRead])
def list_capacity(tenant_id: uuid.UUID, db: Session = Depends(get_db)) -> object:
    return CapacityRepository(db).list(tenant_id)


@router.get("/{capacity_id}", response_model=CapacityRead)
def get_capacity(
    tenant_id: uuid.UUID, capacity_id: uuid.UUID, db: Session = Depends(get_db)
) -> object:
    record = CapacityRepository(db).get(tenant_id, capacity_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Capacity record not found")
    return record
