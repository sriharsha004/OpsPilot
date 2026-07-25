from fastapi import FastAPI

from app.api.errors import register_exception_handlers
from app.api.routes.leads import router as leads_router
from app.api.routes.tenants import router as tenants_router

app = FastAPI(title="OpsPilot API")

register_exception_handlers(app)

app.include_router(tenants_router)
app.include_router(leads_router)
