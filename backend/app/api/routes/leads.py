import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.models.lead import Lead
from app.models.tenant import Tenant
from app.schemas.lead import LeadCreate, LeadRead, LeadUpdate

router = APIRouter(prefix="/tenants/{tenant_id}/leads", tags=["leads"])


@router.post("", response_model=LeadRead, status_code=201)
def create_lead(
    tenant_id: uuid.UUID, payload: LeadCreate, db: Session = Depends(get_db)
) -> Lead:
    tenant = db.get(Tenant, tenant_id)
    if tenant is None:
        raise HTTPException(status_code=404, detail="Tenant not found")

    lead = Lead(tenant_id=tenant_id, **payload.model_dump())
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(
    tenant_id: uuid.UUID, lead_id: uuid.UUID, db: Session = Depends(get_db)
) -> Lead:
    lead = db.query(Lead).filter_by(id=lead_id, tenant_id=tenant_id).first()
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.patch("/{lead_id}", response_model=LeadRead)
def update_lead(
    tenant_id: uuid.UUID,
    lead_id: uuid.UUID,
    payload: LeadUpdate,
    db: Session = Depends(get_db),
) -> Lead:
    lead = db.query(Lead).filter_by(id=lead_id, tenant_id=tenant_id).first()
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)
    return lead
