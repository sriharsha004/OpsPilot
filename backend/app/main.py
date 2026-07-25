from fastapi import FastAPI

from app.api.errors import register_exception_handlers
from app.api.routes.audit_events import router as audit_events_router
from app.api.routes.capacity import router as capacity_router
from app.api.routes.leads import router as leads_router
from app.api.routes.pricing_rules import router as pricing_rules_router
from app.api.routes.tasks import router as tasks_router
from app.api.routes.tenants import router as tenants_router

app = FastAPI(title="OpsPilot API")

register_exception_handlers(app)

app.include_router(tenants_router)
app.include_router(leads_router)
app.include_router(tasks_router)
app.include_router(capacity_router)
app.include_router(pricing_rules_router)
app.include_router(audit_events_router)
