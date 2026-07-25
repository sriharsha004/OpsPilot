import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.models.enums import EntityStatus

if TYPE_CHECKING:
    from app.models.audit_event import AuditEvent
    from app.models.capacity import Capacity
    from app.models.franchisor import Franchisor
    from app.models.lead import Lead
    from app.models.pricing_rule import PricingRule
    from app.models.task import Task
    from app.models.user import User
    from app.models.user_tenant_access import UserTenantAccess


class Tenant(Base):
    __tablename__ = "tenants"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    franchisor_id: Mapped[uuid.UUID | None] = mapped_column(
        UUID(as_uuid=True), ForeignKey("franchisors.id"), nullable=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[EntityStatus] = mapped_column(
        Enum(EntityStatus, name="tenant_status"),
        nullable=False,
        default=EntityStatus.ACTIVE,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    franchisor: Mapped["Franchisor | None"] = relationship(back_populates="tenants")
    home_users: Mapped[list["User"]] = relationship(back_populates="home_tenant")
    leads: Mapped[list["Lead"]] = relationship(back_populates="tenant")
    access_grants: Mapped[list["UserTenantAccess"]] = relationship(back_populates="tenant")
    capacity_records: Mapped[list["Capacity"]] = relationship(back_populates="tenant")
    pricing_rules: Mapped[list["PricingRule"]] = relationship(back_populates="tenant")
    tasks: Mapped[list["Task"]] = relationship(back_populates="tenant")
    audit_events: Mapped[list["AuditEvent"]] = relationship(back_populates="tenant")
