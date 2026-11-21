from typing import Any

from sqlalchemy.orm import Session

from app.models import AuditLog


def audit(db: Session, action: str, actor_user_id=None, actor_role: str | None = None, entity_type: str | None = None, entity_id: Any = None, meta: dict | None = None) -> None:
    db.add(AuditLog(actor_user_id=actor_user_id, actor_role=actor_role, action=action, entity_type=entity_type, entity_id=None if entity_id is None else str(entity_id), meta=meta))
