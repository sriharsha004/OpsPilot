import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.repositories.lead import LeadRepository
from app.repositories.tenant import TenantRepository
from app.schemas.lead import LeadCreate, LeadRead, LeadUpdate

router = APIRouter(prefix="/tenants/{tenant_id}/leads", tags=["leads"])


@router.post("", response_model=LeadRead, status_code=201)
def create_lead(
    tenant_id: uuid.UUID, payload: LeadCreate, db: Session = Depends(get_db)
) -> object:
    tenant = TenantRepository(db).get(tenant_id)
    if tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")

    return LeadRepository(db).create(tenant_id=tenant_id, **payload.model_dump())


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(
    tenant_id: uuid.UUID, lead_id: uuid.UUID, db: Session = Depends(get_db)
) -> object:
    lead = LeadRepository(db).get(tenant_id, lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.patch("/{lead_id}", response_model=LeadRead)
def update_lead(
    tenant_id: uuid.UUID,
    lead_id: uuid.UUID,
    payload: LeadUpdate,
    db: Session = Depends(get_db),
) -> object:
    repo = LeadRepository(db)
    lead = repo.get(tenant_id, lead_id)
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    updates = payload.model_dump(exclude_unset=True)
    return repo.update(lead, **updates)
