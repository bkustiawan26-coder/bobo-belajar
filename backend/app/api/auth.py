import uuid
from datetime import timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.db import get_db, utcnow
from app.core.deps import ParentCtx, current_parent, owned_child
from app.core.ratelimit import client_key, limiter
from app.core.security import decode_token, hash_secret, parent_access_token, parent_refresh_token, student_token, verify_secret
from app.models import GuardianConsent, ParentProfile, User, UserRole
from app.services.audit import audit

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)
    display_name: str = Field(min_length=2, max_length=60)
    accept_privacy_policy: bool
    accept_child_data_processing: bool


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class RefreshIn(BaseModel):
    refresh_token: str
    pin: str | None = None


class ChildSessionIn(BaseModel):
    child_id: uuid.UUID


class TokenOut(BaseModel):
    access_token: str
    refresh_token: str
    roles: list[str]
    has_pin: bool
    display_name: str


def _tokens(user: User, parent: ParentProfile | None) -> TokenOut:
    roles = [r.role for r in user.roles]
    return TokenOut(access_token=parent_access_token(user.id, roles), refresh_token=parent_refresh_token(user.id), roles=roles, has_pin=bool(parent and parent.pin_hash), display_name=user.display_name)


@router.post("/register", response_model=TokenOut, status_code=201)
def register(body: RegisterIn, request: Request, db: Session = Depends(get_db)):
    limiter.check(client_key(request, "register"), 5, 60)
    if not (body.accept_privacy_policy and body.accept_child_data_processing):
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Persetujuan kebijakan privasi dan pemrosesan data anak wajib diberikan")
    email = body.email.lower()
    if db.scalar(select(User.id).where(User.email == email)):
        raise HTTPException(status.HTTP_409_CONFLICT, "Email sudah terdaftar")
    user = User(email=email, password_hash=hash_secret(body.password), display_name=body.display_name.strip())
    user.roles.append(UserRole(role="parent"))
    db.add(user)
    db.flush()
    parent = ParentProfile(user_id=user.id)
    db.add(parent)
    db.flush()
    v, now = get_settings().privacy_policy_version, utcnow()
    db.add_all([
        GuardianConsent(parent_id=parent.id, consent_type="privacy_policy", policy_version=v, granted=True, granted_at=now),
        GuardianConsent(parent_id=parent.id, consent_type="child_data_processing", policy_version=v, granted=True, granted_at=now),
        GuardianConsent(parent_id=parent.id, consent_type="ai_training", policy_version=v, granted=False),
    ])
    audit(db, "parent.register", user.id, "parent", "user", user.id)
    db.commit()
    return _tokens(user, parent)


@router.post("/login", response_model=TokenOut)
def login(body: LoginIn, request: Request, db: Session = Depends(get_db)):
    limiter.check(client_key(request, "login"), get_settings().login_rate_per_minute, 60)
    user = db.scalar(select(User).where(User.email == body.email.lower()))
    if user is None or not user.is_active or user.deleted_at is not None or not verify_secret(body.password, user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Email atau kata sandi salah")
    parent = db.scalar(select(ParentProfile).where(ParentProfile.user_id == user.id))
    audit(db, "auth.login", user.id, ",".join(r.role for r in user.roles))
    db.commit()
    return _tokens(user, parent)


def check_pin(db: Session, parent: ParentProfile, pin: str | None) -> None:
    s = get_settings()
    now = utcnow()
    if parent.pin_locked_until and parent.pin_locked_until > now:
        raise HTTPException(status.HTTP_423_LOCKED, "PIN terkunci sementara karena terlalu banyak percobaan")
    if not pin or not verify_secret(pin, parent.pin_hash):
        parent.pin_failed_attempts += 1
        if parent.pin_failed_attempts >= s.pin_max_attempts:
            parent.pin_locked_until = now + timedelta(minutes=s.pin_lock_minutes)
            parent.pin_failed_attempts = 0
        db.commit()
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "PIN salah")
    parent.pin_failed_attempts = 0
    parent.pin_locked_until = None


@router.post("/refresh", response_model=TokenOut)
def refresh(body: RefreshIn, request: Request, db: Session = Depends(get_db)):
    limiter.check(client_key(request, "refresh"), 30, 60)
    try:
        c = decode_token(body.refresh_token)
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Sesi kedaluwarsa, silakan masuk lagi")
    if c.get("typ") != "refresh":
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token tidak valid")
    user = db.get(User, uuid.UUID(c["sub"]))
    if user is None or not user.is_active or user.deleted_at is not None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Akun tidak aktif")
    parent = db.scalar(select(ParentProfile).where(ParentProfile.user_id == user.id))
    if parent is not None and parent.pin_hash:
        check_pin(db, parent, body.pin)
    db.commit()
    return _tokens(user, parent)


@router.post("/child-session")
def child_session(body: ChildSessionIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    child = owned_child(db, ctx.parent, body.child_id)
    consent = db.scalar(select(GuardianConsent).where(GuardianConsent.parent_id == ctx.parent.id, GuardianConsent.consent_type == "child_data_processing", GuardianConsent.granted.is_(True), GuardianConsent.revoked_at.is_(None)))
    if consent is None:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Persetujuan pemrosesan data anak belum aktif")
    audit(db, "child.session", ctx.user.id, "parent", "student", child.id)
    db.commit()
    return {"student_token": student_token(child.id, ctx.user.id), "child_id": str(child.id), "nickname": child.nickname, "grade": child.grade_number}
