import os

import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

TEST_DATABASE_URL = os.environ["TEST_DATABASE_URL"]

test_engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

from app.api.dependencies.database import get_db  # noqa: E402
from app.database.base import Base  # noqa: E402
from app.main import app  # noqa: E402
from app.models import Franchisor, Lead, Tenant, User, UserTenantAccess  # noqa: E402, F401
from app.models.enums import UserRole  # noqa: E402


@pytest.fixture(scope="session", autouse=True)
def _create_test_schema():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(autouse=True)
def _clean_tables():
    """Truncate every table before each test so tests never see each other's data."""
    with test_engine.begin() as connection:
        for table in reversed(Base.metadata.sorted_tables):
            connection.execute(table.delete())
    yield


def _override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = _override_get_db


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db():
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture
def tenant(db):
    t = Tenant(name="Leander Campus")
    db.add(t)
    db.commit()
    db.refresh(t)
    return t


@pytest.fixture
def user(db, tenant):
    u = User(
        name="Jane Admin",
        email="jane.admin@example.com",
        role=UserRole.TENANT_ADMIN,
        home_tenant_id=tenant.id,
    )
    db.add(u)
    db.commit()
    db.refresh(u)
    return u
