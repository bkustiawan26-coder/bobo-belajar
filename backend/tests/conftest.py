import os
import secrets
import uuid

os.environ.setdefault("BOBO_JWT_SECRET", secrets.token_hex(32))
os.environ.setdefault("BOBO_DATABASE_URL", "postgresql+psycopg://bobo:bobo@localhost:5432/bobo_test")
os.environ.setdefault("BOBO_ENV", "test")

import pytest
from alembic import command
from alembic.config import Config
from fastapi.testclient import TestClient
from sqlalchemy import text

from app.core.db import get_engine, session_factory
from app.core.ratelimit import limiter
from app.main import app
from app.seed.seed import run
from app.services.ai.service import clear_cache

ROOT = os.path.dirname(os.path.dirname(__file__))


@pytest.fixture(scope="session", autouse=True)
def schema():
    eng = get_engine()
    with eng.begin() as c:
        c.execute(text("DROP SCHEMA public CASCADE; CREATE SCHEMA public;"))
    cfg = Config(os.path.join(ROOT, "alembic.ini"))
    cfg.set_main_option("script_location", os.path.join(ROOT, "alembic"))
    command.upgrade(cfg, "head")
    yield


@pytest.fixture(autouse=True)
def clean(schema):
    eng = get_engine()
    with eng.begin() as c:
        tables = [r[0] for r in c.execute(text("select tablename from pg_tables where schemaname='public' and tablename <> 'alembic_version'"))]
        c.execute(text("TRUNCATE " + ", ".join(f'"{t}"' for t in tables) + " RESTART IDENTITY CASCADE"))
    db = session_factory()()
    run(db, sample=True, publish_sample=True)
    db.close()
    limiter.reset()
    clear_cache()
    yield


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db():
    s = session_factory()()
    yield s
    s.close()


def register(client, email=None, pin="2468"):
    email = email or f"ortu-{uuid.uuid4().hex[:8]}@contoh.id"
    r = client.post("/v1/auth/register", json={"email": email, "password": "rahasia-kuat-1", "display_name": "Ibu Sari", "accept_privacy_policy": True, "accept_child_data_processing": True})
    assert r.status_code == 201, r.text
    tok = r.json()
    h = {"Authorization": f"Bearer {tok['access_token']}"}
    if pin:
        assert client.put("/v1/parent/pin", json={"pin": pin, "password": "rahasia-kuat-1"}, headers=h).status_code == 200
    return tok, h


def add_child(client, h, nickname="Nadia", grade=5):
    r = client.post("/v1/parent/children", json={"nickname": nickname, "grade": grade}, headers=h)
    assert r.status_code == 201, r.text
    cid = r.json()["id"]
    s = client.post("/v1/auth/child-session", json={"child_id": cid}, headers=h)
    assert s.status_code == 200, s.text
    return cid, {"Authorization": f"Bearer {s.json()['student_token']}"}


def staff(db, role="admin", email=None):
    from app.core.security import hash_secret, parent_access_token
    from app.models import User, UserRole
    u = User(email=email or f"{role}-{uuid.uuid4().hex[:6]}@bobo.id", display_name=role.title(), password_hash=hash_secret("admin-rahasia-123"))
    u.roles.append(UserRole(role=role))
    db.add(u)
    db.commit()
    return {"Authorization": f"Bearer {parent_access_token(u.id, [role])}"}
