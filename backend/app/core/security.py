import uuid
from datetime import timedelta
from typing import Any

import bcrypt
import jwt

from app.core.config import get_settings
from app.core.db import utcnow


def hash_secret(value: str) -> str:
    return bcrypt.hashpw(value.encode(), bcrypt.gensalt(rounds=12)).decode()


def verify_secret(value: str, hashed: str | None) -> bool:
    if not hashed:
        return False
    try:
        return bcrypt.checkpw(value.encode(), hashed.encode())
    except ValueError:
        return False


def _encode(claims: dict[str, Any], ttl: timedelta) -> str:
    s = get_settings()
    now = utcnow()
    payload = {**claims, "iss": s.jwt_issuer, "iat": int(now.timestamp()), "exp": int((now + ttl).timestamp()), "jti": uuid.uuid4().hex}
    return jwt.encode(payload, s.jwt_secret, algorithm="HS256")


def parent_access_token(user_id: uuid.UUID, roles: list[str]) -> str:
    return _encode({"sub": str(user_id), "typ": "access", "roles": roles}, timedelta(minutes=get_settings().access_ttl_minutes))


def parent_refresh_token(user_id: uuid.UUID) -> str:
    return _encode({"sub": str(user_id), "typ": "refresh"}, timedelta(days=get_settings().refresh_ttl_days))


def student_token(student_id: uuid.UUID, parent_user_id: uuid.UUID) -> str:
    return _encode({"sub": str(student_id), "typ": "student", "roles": ["student"], "guardian": str(parent_user_id)}, timedelta(days=get_settings().student_ttl_days))


def decode_token(token: str) -> dict[str, Any]:
    s = get_settings()
    return jwt.decode(token, s.jwt_secret, algorithms=["HS256"], issuer=s.jwt_issuer, options={"require": ["exp", "sub", "typ"]})
