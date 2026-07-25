import uuid
from datetime import UTC, datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.models.enums import TaskStatus
from app.models.lead import Lead
from app.repositories.task import TaskRepository
from app.schemas.task import TaskCreate, TaskRead, TaskUpdate

router = APIRouter(prefix="/tenants/{tenant_id}/leads/{lead_id}/tasks", tags=["tasks"])


@router.post("", response_model=TaskRead, status_code=201)
def create_task(
    tenant_id: uuid.UUID,
    lead_id: uuid.UUID,
    payload: TaskCreate,
    db: Session = Depends(get_db),
) -> object:
    lead = db.query(Lead).filter_by(id=lead_id, tenant_id=tenant_id).first()
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")

    repo = TaskRepository(db)
    return repo.create(tenant_id=tenant_id, lead_id=lead_id, **payload.model_dump())


@router.get("", response_model=list[TaskRead])
def list_tasks(tenant_id: uuid.UUID, lead_id: uuid.UUID, db: Session = Depends(get_db)) -> object:
    repo = TaskRepository(db)
    return repo.list_for_lead(tenant_id, lead_id)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    tenant_id: uuid.UUID, lead_id: uuid.UUID, task_id: uuid.UUID, db: Session = Depends(get_db)
) -> object:
    repo = TaskRepository(db)
    task = repo.get_for_lead(tenant_id, lead_id, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/{task_id}", response_model=TaskRead)
def update_task(
    tenant_id: uuid.UUID,
    lead_id: uuid.UUID,
    task_id: uuid.UUID,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
) -> object:
    repo = TaskRepository(db)
    task = repo.get_for_lead(tenant_id, lead_id, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    updates = payload.model_dump(exclude_unset=True)
    if updates.get("status") == TaskStatus.DONE:
        updates["completed_at"] = datetime.now(UTC)

    return repo.update(task, **updates)
