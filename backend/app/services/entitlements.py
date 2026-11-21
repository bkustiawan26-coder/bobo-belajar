from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models import ParentProfile, StudentProfile, SubscriptionEntitlement


def plan_value(db: Session, plan: str, key: str, default: int) -> int:
    row = db.scalar(select(SubscriptionEntitlement).where(SubscriptionEntitlement.plan == plan, SubscriptionEntitlement.key == key))
    if row is None:
        return default
    try:
        return int(row.value)
    except ValueError:
        return default


def tutor_limit(db: Session, parent: ParentProfile, student: StudentProfile) -> int:
    s = get_settings()
    base = plan_value(db, parent.plan, "tutor_daily_limit", s.premium_tutor_daily_limit if parent.plan == "premium" else s.free_tutor_daily_limit)
    if student.tutor_daily_limit_override is not None:
        return max(0, min(base, student.tutor_daily_limit_override))
    return base


def parent_assistant_limit(db: Session, parent: ParentProfile) -> int:
    s = get_settings()
    return plan_value(db, parent.plan, "parent_assistant_daily_limit", s.premium_parent_assistant_daily_limit if parent.plan == "premium" else s.free_parent_assistant_daily_limit)
