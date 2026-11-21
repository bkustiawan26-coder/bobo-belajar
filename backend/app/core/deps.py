import uuid
from dataclasses import dataclass

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.security import decode_token
from app.models import GuardianChildLink, ParentProfile, StudentProfile, User

bearer = HTTPBearer(auto_error=False)


@dataclass
class ParentCtx:
    user: User
    parent: ParentProfile | None
    roles: list[str]


@dataclass
class StudentCtx:
    student: StudentProfile
    guardian_user_id: uuid.UUID


def _claims(creds: HTTPAuthorizationCredentials | None) -> dict:
    if creds is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Sesi tidak ditemukan")
    try:
        return decode_token(creds.credentials)
    except jwt.PyJWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Sesi tidak valid atau kedaluwarsa")


def current_user(creds=Depends(bearer), db: Session = Depends(get_db)) -> ParentCtx:
    c = _claims(creds)
    if c.get("typ") != "access":
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Akses khusus orang tua atau admin")
    user = db.get(User, uuid.UUID(c["sub"]))
    if user is None or not user.is_active or user.deleted_at is not None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Akun tidak aktif")
    parent = db.scalar(select(ParentProfile).where(ParentProfile.user_id == user.id))
    return ParentCtx(user=user, parent=parent, roles=[r.role for r in user.roles])


def current_parent(ctx: ParentCtx = Depends(current_user)) -> ParentCtx:
    if ctx.parent is None or "parent" not in ctx.roles:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Akses khusus orang tua")
    return ctx


def require_roles(*allowed: str):
    def dep(ctx: ParentCtx = Depends(current_user)) -> ParentCtx:
        if not set(allowed) & set(ctx.roles):
            raise HTTPException(status.HTTP_403_FORBIDDEN, "Peran tidak diizinkan")
        return ctx
    return dep


def current_student(creds=Depends(bearer), db: Session = Depends(get_db)) -> StudentCtx:
    c = _claims(creds)
    if c.get("typ") != "student":
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Akses khusus mode anak")
    student = db.get(StudentProfile, uuid.UUID(c["sub"]))
    guardian = uuid.UUID(c["guardian"])
    if student is None or student.deleted_at is not None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Profil anak tidak ditemukan")
    linked = db.scalar(
        select(GuardianChildLink.id)
        .join(ParentProfile, ParentProfile.id == GuardianChildLink.parent_id)
        .where(GuardianChildLink.student_id == student.id, ParentProfile.user_id == guardian)
    )
    if linked is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Profil anak tidak lagi terhubung")
    return StudentCtx(student=student, guardian_user_id=guardian)


def owned_child(db: Session, parent: ParentProfile, child_id: uuid.UUID) -> StudentProfile:
    child = db.scalar(
        select(StudentProfile)
        .join(GuardianChildLink, GuardianChildLink.student_id == StudentProfile.id)
        .where(GuardianChildLink.parent_id == parent.id, StudentProfile.id == child_id, StudentProfile.deleted_at.is_(None))
    )
    if child is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Profil anak tidak ditemukan")
    return child
