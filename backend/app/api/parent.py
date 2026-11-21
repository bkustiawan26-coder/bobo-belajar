import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field, field_validator
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.db import get_db, utcnow
from app.core.deps import ParentCtx, current_parent, owned_child
from app.core.security import hash_secret, verify_secret
from app.models import (
    AIMessage, AIConversation, AISafetyEvent, AIUsageLog, Assessment, AssessmentResult, ExerciseAttempt, GuardianChildLink, GuardianConsent,
    LearningRecommendation, LearningSession, LessonProgress, PrivacyRequest, StudentProfile, User,
)
from app.services import learning, support
from app.services.ai import service as ai
from app.services.audit import audit
from app.services.entitlements import tutor_limit

router = APIRouter(prefix="/parent", tags=["parent"])

MAX_CHILDREN = 6


class ChildIn(BaseModel):
    nickname: str = Field(min_length=2, max_length=20)
    grade: int = Field(ge=1, le=9)

    @field_validator("nickname")
    @classmethod
    def clean(cls, v: str) -> str:
        v = " ".join(v.split())
        if any(ch.isdigit() for ch in v):
            raise ValueError("Nama panggilan tidak boleh berisi angka")
        return v


class SettingsIn(BaseModel):
    short_sessions: bool = False
    larger_text: bool = False
    fewer_options: bool = False
    read_aloud: bool = False


class ChildPatch(BaseModel):
    nickname: str | None = Field(default=None, min_length=2, max_length=20)
    grade: int | None = Field(default=None, ge=1, le=9)
    tutor_daily_limit: int | None = Field(default=None, ge=0, le=100)
    settings: SettingsIn | None = None


class PinIn(BaseModel):
    pin: str = Field(pattern=r"^\d{4,6}$")
    password: str


def _child_out(db: Session, parent, c: StudentProfile) -> dict:
    a, b = learning.today_bounds()
    used = db.scalar(select(func.count()).select_from(AIUsageLog).where(AIUsageLog.student_id == c.id, AIUsageLog.purpose == "tutor", AIUsageLog.created_at >= a, AIUsageLog.created_at < b)) or 0
    safety = db.scalar(select(func.count()).select_from(AISafetyEvent).where(AISafetyEvent.student_id == c.id, AISafetyEvent.purpose == "tutor", AISafetyEvent.action == "refuse")) or 0
    return {"id": str(c.id), "nickname": c.nickname, "grade": c.grade_number, "level": learning.level(c.grade_number), "phase": learning.phase(c.grade_number), "band": learning.band(c.grade_number),
            "tutor_today": used, "tutor_limit": tutor_limit(db, parent, c), "safety_refusals": safety, "consent_active": True, "settings": support.clean_settings(c.settings)}


@router.get("/me")
def me(ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    return {"display_name": ctx.user.display_name, "email": ctx.user.email, "plan": ctx.parent.plan, "has_pin": bool(ctx.parent.pin_hash)}


@router.put("/pin")
def set_pin(body: PinIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    if not verify_secret(body.password, ctx.user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Kata sandi salah")
    ctx.parent.pin_hash = hash_secret(body.pin)
    ctx.parent.pin_failed_attempts = 0
    ctx.parent.pin_locked_until = None
    audit(db, "parent.pin_set", ctx.user.id, "parent")
    db.commit()
    return {"has_pin": True}


@router.get("/children")
def children(ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    rows = db.scalars(select(StudentProfile).join(GuardianChildLink, GuardianChildLink.student_id == StudentProfile.id).where(GuardianChildLink.parent_id == ctx.parent.id, StudentProfile.deleted_at.is_(None)).order_by(StudentProfile.created_at))
    return {"children": [_child_out(db, ctx.parent, c) for c in rows]}


@router.post("/children", status_code=201)
def add_child(body: ChildIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    n = db.scalar(select(func.count()).select_from(GuardianChildLink).join(StudentProfile, StudentProfile.id == GuardianChildLink.student_id).where(GuardianChildLink.parent_id == ctx.parent.id, StudentProfile.deleted_at.is_(None))) or 0
    if n >= MAX_CHILDREN:
        raise HTTPException(status.HTTP_409_CONFLICT, f"Maksimal {MAX_CHILDREN} profil anak per akun")
    c = StudentProfile(nickname=body.nickname, grade_number=body.grade)
    db.add(c)
    db.flush()
    db.add(GuardianChildLink(parent_id=ctx.parent.id, student_id=c.id))
    db.add(GuardianConsent(parent_id=ctx.parent.id, student_id=c.id, consent_type="child_profile", policy_version="2026-11", granted=True, granted_at=utcnow()))
    learning.log_activity(db, c.id, "profile", "Profil dibuat oleh orang tua")
    audit(db, "child.create", ctx.user.id, "parent", "student", c.id)
    db.commit()
    return _child_out(db, ctx.parent, c)


@router.patch("/children/{child_id}")
def patch_child(child_id: uuid.UUID, body: ChildPatch, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    if body.nickname is not None:
        c.nickname = ChildIn(nickname=body.nickname, grade=c.grade_number).nickname
    if body.grade is not None:
        c.grade_number = body.grade
    if body.tutor_daily_limit is not None:
        c.tutor_daily_limit_override = body.tutor_daily_limit
    if body.settings is not None:
        c.settings = support.clean_settings(body.settings.model_dump())
    audit(db, "child.update", ctx.user.id, "parent", "student", c.id, body.model_dump(exclude_none=True))
    db.commit()
    return _child_out(db, ctx.parent, c)


@router.delete("/children/{child_id}")
def delete_child(child_id: uuid.UUID, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    _erase_child(db, c)
    db.add(PrivacyRequest(parent_id=ctx.parent.id, student_id=c.id, kind="delete_child", status="completed", completed_at=utcnow(), done=True))
    audit(db, "child.delete", ctx.user.id, "parent", "student", c.id)
    db.commit()
    return {"deleted": True}


def _erase_child(db: Session, c: StudentProfile) -> None:
    from app.models import ReviewItem
    for model in (ExerciseAttempt, LessonProgress, LearningSession, LearningRecommendation, AssessmentResult, ReviewItem):
        db.query(model).filter(model.student_id == c.id).delete(synchronize_session=False)
    conv_ids = list(db.scalars(select(AIConversation.id).where(AIConversation.student_id == c.id)))
    if conv_ids:
        db.query(AIMessage).filter(AIMessage.conversation_id.in_(conv_ids)).delete(synchronize_session=False)
        db.query(AIConversation).filter(AIConversation.id.in_(conv_ids)).delete(synchronize_session=False)
    c.nickname = "Dihapus"
    c.deleted_at = utcnow()


@router.get("/children/{child_id}/dashboard")
def dashboard(child_id: uuid.UUID, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    m = learning.mastery_for(db, c)
    total = db.scalar(select(func.count()).select_from(ExerciseAttempt).where(ExerciseAttempt.student_id == c.id)) or 0
    ok = db.scalar(select(func.count()).select_from(ExerciseAttempt).where(ExerciseAttempt.student_id == c.id, ExerciseAttempt.is_correct.is_(True))) or 0
    lessons_done = db.scalar(select(func.count()).select_from(LessonProgress).where(LessonProgress.student_id == c.id, LessonProgress.completed_at.is_not(None))) or 0
    exams = db.execute(select(AssessmentResult, Assessment.title).join(Assessment, Assessment.id == AssessmentResult.assessment_id).where(AssessmentResult.student_id == c.id).order_by(AssessmentResult.created_at.desc()).limit(10)).all()
    titles = {x["topic_id"]: x["topic"] for x in m}
    log = list(db.scalars(select(LearningSession).where(LearningSession.student_id == c.id).order_by(LearningSession.occurred_at.desc(), LearningSession.id.desc()).limit(8)))
    recs = learning.active_recommendations(db, c)
    top = next((r for r in recs if r.kind != "maintain"), None)
    last = exams[0][0] if exams else None
    return {
        "child": _child_out(db, ctx.parent, c),
        "last_active": learning.relative_label(log[0].occurred_at) if log else None,
        "kpis": {
            "lessons_completed": lessons_done, "answers_total": total, "answers_correct": ok, "accuracy_pct": round(ok * 100 / total) if total else None,
            "last_assessment": {"score": round(last.score), "date": learning.relative_label(last.created_at), "final": last.is_final} if last else None,
        },
        "mastery": [{k: v for k, v in x.items() if k not in ("home_activity", "common_mistake")} for x in m],
        "top_recommendation": _rec_out(top) if top else None,
        "assessments": [{"title": t, "score": round(r.score), "date": learning.relative_label(r.created_at), "final": r.is_final, "pending_review": r.pending_review_count, "weak_topics": [titles.get(x) for x in r.weak_topic_ids if titles.get(x)]} for r, t in exams],
        "activity": [{"text": a.summary, "when": learning.relative_label(a.occurred_at)} for a in log],
        "signals": support.signals(db, c),
        "review_due": support.due_count(db, c.id),
    }


@router.get("/children/{child_id}/summary")
def summary(child_id: uuid.UUID, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    audit(db, "child.summary_shared", ctx.user.id, "parent", "student", c.id)
    db.commit()
    return {"text": support.teacher_summary(db, c)}


@router.get("/children/{child_id}/growth")
def child_growth(child_id: uuid.UUID, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    return support.growth(db, owned_child(db, ctx.parent, child_id))


def _rec_out(r: LearningRecommendation) -> dict:
    return {"id": r.id, "kind": r.kind, "kind_label": learning.KIND_LABEL.get(r.kind, r.kind), "title": r.title, "evidence": r.evidence, "activity": r.activity, "duration": r.duration_label, "done": r.done_at is not None}


@router.get("/children/{child_id}/recommendations")
def recommendations(child_id: uuid.UUID, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    return {"recommendations": [_rec_out(r) for r in learning.active_recommendations(db, c)]}


class DoneIn(BaseModel):
    done: bool = True


@router.post("/children/{child_id}/recommendations/{rec_id}/done")
def rec_done(child_id: uuid.UUID, rec_id: int, body: DoneIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, child_id)
    r = db.get(LearningRecommendation, rec_id)
    if r is None or r.student_id != c.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Rekomendasi tidak ditemukan")
    r.done_at = utcnow() if body.done else None
    db.commit()
    return _rec_out(r)


class AskIn(BaseModel):
    child_id: uuid.UUID
    text: str = Field(min_length=1, max_length=600)
    conversation_id: uuid.UUID | None = None


@router.post("/assistant/messages")
def assistant(body: AskIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    c = owned_child(db, ctx.parent, body.child_id)
    return ai.parent_reply(db, ctx.parent, c, body.text.strip(), body.conversation_id)


@router.get("/consents")
def consents(ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    rows = db.scalars(select(GuardianConsent).where(GuardianConsent.parent_id == ctx.parent.id).order_by(GuardianConsent.id))
    return {"consents": [{"id": r.id, "type": r.consent_type, "child_id": str(r.student_id) if r.student_id else None, "granted": r.granted and r.revoked_at is None, "policy_version": r.policy_version} for r in rows]}


class ConsentIn(BaseModel):
    consent_type: str = Field(pattern=r"^(ai_training|marketing_email)$")
    granted: bool


@router.post("/consents")
def set_consent(body: ConsentIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    now = utcnow()
    for r in db.scalars(select(GuardianConsent).where(GuardianConsent.parent_id == ctx.parent.id, GuardianConsent.consent_type == body.consent_type, GuardianConsent.revoked_at.is_(None))):
        r.revoked_at = now
    db.add(GuardianConsent(parent_id=ctx.parent.id, consent_type=body.consent_type, policy_version="2026-11", granted=body.granted, granted_at=now if body.granted else None))
    audit(db, "consent.update", ctx.user.id, "parent", meta=body.model_dump())
    db.commit()
    return {"consent_type": body.consent_type, "granted": body.granted}


@router.get("/export")
def export(ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    kids = db.scalars(select(StudentProfile).join(GuardianChildLink, GuardianChildLink.student_id == StudentProfile.id).where(GuardianChildLink.parent_id == ctx.parent.id, StudentProfile.deleted_at.is_(None))).all()
    data = {"account": {"display_name": ctx.user.display_name, "email": ctx.user.email, "plan": ctx.parent.plan}, "children": []}
    for c in kids:
        data["children"].append({
            "nickname": c.nickname, "grade": c.grade_number,
            "attempts": [{"question_id": a.question_id, "correct": a.is_correct, "source": a.source, "answered_at": a.answered_at.isoformat()} for a in db.scalars(select(ExerciseAttempt).where(ExerciseAttempt.student_id == c.id))],
            "assessments": [{"assessment_id": r.assessment_id, "score": r.score, "at": r.created_at.isoformat()} for r in db.scalars(select(AssessmentResult).where(AssessmentResult.student_id == c.id))],
            "activity": [{"text": s.summary, "at": s.occurred_at.isoformat()} for s in db.scalars(select(LearningSession).where(LearningSession.student_id == c.id))],
        })
    db.add(PrivacyRequest(parent_id=ctx.parent.id, kind="export", status="completed", completed_at=utcnow(), done=True))
    audit(db, "privacy.export", ctx.user.id, "parent")
    db.commit()
    return data


class DeleteAccountIn(BaseModel):
    password: str
    confirm: str = Field(pattern=r"^HAPUS$")


@router.post("/delete-account")
def delete_account(body: DeleteAccountIn, ctx: ParentCtx = Depends(current_parent), db: Session = Depends(get_db)):
    if not verify_secret(body.password, ctx.user.password_hash):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Kata sandi salah")
    kids = db.scalars(select(StudentProfile).join(GuardianChildLink, GuardianChildLink.student_id == StudentProfile.id).where(GuardianChildLink.parent_id == ctx.parent.id)).all()
    for c in kids:
        _erase_child(db, c)
    u: User = ctx.user
    u.email = f"deleted-{u.id}@invalid"
    u.display_name = "Dihapus"
    u.password_hash = None
    u.is_active = False
    u.deleted_at = utcnow()
    ctx.parent.pin_hash = None
    db.add(PrivacyRequest(parent_id=ctx.parent.id, kind="delete_account", status="completed", completed_at=utcnow(), done=True))
    audit(db, "privacy.delete_account", u.id, "parent")
    db.commit()
    return {"deleted": True}
