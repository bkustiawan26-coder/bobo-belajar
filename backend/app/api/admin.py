from datetime import timedelta
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.db import get_db, utcnow
from app.core.deps import ParentCtx, require_roles
from app.models import (
    AIPromptVersion, AIUsageLog, Assessment, AssessmentAnswer, AssessmentQuestion, AssessmentResult, AssessmentSession, AssessmentTemplate, AuditLog,
    Chapter, ContentReview, ContentVersion, CurriculumSource, CurriculumVersion, EducationLevel, Grade, LearningObjective, Lesson, LessonBlock,
    Question, QuestionExplanation, QuestionOption, QuestionReview, QuestionSource, QuestionVersion, StudentProfile, Subject, Topic,
)
from app.models.questions import QUESTION_TYPES
from app.services import learning
from app.services.ai import retrieval
from app.services.audit import audit
from app.services.grading import validate_answer_shape

router = APIRouter(prefix="/admin", tags=["admin"])
staff = require_roles("admin", "editor", "reviewer")
editor = require_roles("admin", "editor")
reviewer = require_roles("admin", "reviewer")
admin_only = require_roles("admin")


def _get(db: Session, model, oid):
    obj = db.get(model, oid)
    if obj is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"{model.__tablename__} tidak ditemukan")
    return obj


def _row(obj, *fields) -> dict:
    return {f: getattr(obj, f) for f in fields}


class VersionIn(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    version: str = Field(min_length=1, max_length=40)
    academic_year: str | None = None
    is_active: bool = False


@router.get("/curriculum/versions")
def versions(ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return [_row(v, "id", "name", "version", "academic_year", "is_active", "status") for v in db.scalars(select(CurriculumVersion).order_by(CurriculumVersion.id))]


@router.post("/curriculum/versions", status_code=201)
def create_version(body: VersionIn, ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    if body.is_active:
        for v in db.scalars(select(CurriculumVersion).where(CurriculumVersion.is_active.is_(True))):
            v.is_active = False
    v = CurriculumVersion(**body.model_dump(), status="active" if body.is_active else "draft")
    db.add(v)
    audit(db, "curriculum.version_create", ctx.user.id, "admin", "curriculum_version", None, body.model_dump())
    db.commit()
    return _row(v, "id", "name", "version", "academic_year", "is_active", "status")


@router.post("/curriculum/versions/{vid}/activate")
def activate_version(vid: int, ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    target = _get(db, CurriculumVersion, vid)
    for v in db.scalars(select(CurriculumVersion)):
        v.is_active = v.id == target.id
        if v.is_active:
            v.status = "active"
    audit(db, "curriculum.version_activate", ctx.user.id, "admin", "curriculum_version", vid)
    db.commit()
    return {"active_version_id": vid}


class SourceIn(BaseModel):
    title: str = Field(min_length=3, max_length=300)
    issuing_authority: str | None = None
    reference: str | None = None
    published_on: str | None = None
    retrieved_on: str | None = None
    verification_status: Literal["unverified", "verified", "rejected"] = "unverified"
    notes: str | None = None


def _source_out(s: CurriculumSource) -> dict:
    return {"id": s.id, "title": s.title, "issuing_authority": s.issuing_authority, "reference": s.reference, "published_on": s.published_on.isoformat() if s.published_on else None,
            "retrieved_on": s.retrieved_on.isoformat() if s.retrieved_on else None, "verification_status": s.verification_status, "notes": s.notes}


@router.get("/curriculum/versions/{vid}/sources")
def sources(vid: int, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return [_source_out(s) for s in db.scalars(select(CurriculumSource).where(CurriculumSource.curriculum_version_id == vid).order_by(CurriculumSource.id))]


def _date(v: str | None):
    from datetime import date
    return date.fromisoformat(v) if v else None


@router.post("/curriculum/versions/{vid}/sources", status_code=201)
def add_source(vid: int, body: SourceIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, CurriculumVersion, vid)
    if body.verification_status == "verified" and not body.reference:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Sumber terverifikasi wajib memiliki referensi dokumen atau URL")
    s = CurriculumSource(curriculum_version_id=vid, **{**body.model_dump(), "published_on": _date(body.published_on), "retrieved_on": _date(body.retrieved_on)})
    db.add(s)
    audit(db, "curriculum.source_add", ctx.user.id, "staff", "curriculum_source", None, {"title": body.title})
    db.commit()
    return _source_out(s)


@router.put("/curriculum/sources/{sid}")
def update_source(sid: int, body: SourceIn, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    s = _get(db, CurriculumSource, sid)
    if body.verification_status == "verified" and not body.reference:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Sumber terverifikasi wajib memiliki referensi dokumen atau URL")
    for k, v in body.model_dump().items():
        setattr(s, k, _date(v) if k in ("published_on", "retrieved_on") else v)
    audit(db, "curriculum.source_update", ctx.user.id, "reviewer", "curriculum_source", sid, {"verification_status": body.verification_status})
    db.commit()
    return _source_out(s)


@router.get("/grades")
def grades(ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    rows = db.execute(select(Grade, EducationLevel.code).join(EducationLevel, EducationLevel.id == Grade.education_level_id).order_by(Grade.number)).all()
    return [{"id": g.id, "number": g.number, "phase": g.phase, "level": code} for g, code in rows]


class SubjectIn(BaseModel):
    curriculum_version_id: int
    grade_number: int = Field(ge=1, le=9)
    code: str = Field(min_length=2, max_length=20)
    name: str = Field(min_length=2, max_length=80)
    short_label: str = Field(min_length=1, max_length=4)
    sort_order: int = 0
    is_enabled: bool = True


def _subject_out(db: Session, s: Subject) -> dict:
    g = db.get(Grade, s.grade_id)
    return {"id": s.id, "curriculum_version_id": s.curriculum_version_id, "grade_number": g.number, "code": s.code, "name": s.name, "short_label": s.short_label, "sort_order": s.sort_order, "is_enabled": s.is_enabled}


@router.get("/subjects")
def subjects(version_id: int | None = None, grade: int | None = None, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    q = select(Subject).join(Grade, Grade.id == Subject.grade_id)
    if version_id:
        q = q.where(Subject.curriculum_version_id == version_id)
    if grade:
        q = q.where(Grade.number == grade)
    return [_subject_out(db, s) for s in db.scalars(q.order_by(Grade.number, Subject.sort_order, Subject.id))]


def _grade_id(db: Session, number: int) -> int:
    g = db.scalar(select(Grade).where(Grade.number == number))
    if g is None:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Kelas belum dikonfigurasi")
    return g.id


@router.post("/subjects", status_code=201)
def create_subject(body: SubjectIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, CurriculumVersion, body.curriculum_version_id)
    s = Subject(curriculum_version_id=body.curriculum_version_id, grade_id=_grade_id(db, body.grade_number), code=body.code, name=body.name, short_label=body.short_label, sort_order=body.sort_order, is_enabled=body.is_enabled)
    db.add(s)
    db.commit()
    return _subject_out(db, s)


@router.put("/subjects/{sid}")
def update_subject(sid: int, body: SubjectIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    s = _get(db, Subject, sid)
    s.grade_id = _grade_id(db, body.grade_number)
    for k in ("code", "name", "short_label", "sort_order", "is_enabled"):
        setattr(s, k, getattr(body, k))
    db.commit()
    return _subject_out(db, s)


@router.get("/subjects/{sid}/tree")
def subject_tree(sid: int, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    s = _get(db, Subject, sid)
    out = {**_subject_out(db, s), "chapters": []}
    for ch in db.scalars(select(Chapter).where(Chapter.subject_id == sid).order_by(Chapter.number)):
        topics = []
        for t in db.scalars(select(Topic).where(Topic.chapter_id == ch.id).order_by(Topic.sort_order, Topic.id)):
            objs = [_row(o, "id", "code", "description", "status", "source_id") for o in db.scalars(select(LearningObjective).where(LearningObjective.topic_id == t.id))]
            nl = db.scalar(select(func.count()).select_from(Lesson).where(Lesson.topic_id == t.id)) or 0
            nq = db.scalar(select(func.count()).select_from(Question).where(Question.topic_id == t.id)) or 0
            topics.append({**_row(t, "id", "title", "sort_order", "home_activity", "common_mistake"), "objectives": objs, "lesson_count": nl, "question_count": nq})
        out["chapters"].append({**_row(ch, "id", "number", "title", "semester"), "topics": topics})
    return out


class ChapterIn(BaseModel):
    subject_id: int
    number: int = Field(ge=1, le=50)
    title: str = Field(min_length=2, max_length=160)
    semester: int | None = Field(default=None, ge=1, le=2)


@router.post("/chapters", status_code=201)
def create_chapter(body: ChapterIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, Subject, body.subject_id)
    c = Chapter(**body.model_dump())
    db.add(c)
    db.commit()
    return _row(c, "id", "subject_id", "number", "title", "semester")


@router.put("/chapters/{cid}")
def update_chapter(cid: int, body: ChapterIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    c = _get(db, Chapter, cid)
    for k, v in body.model_dump().items():
        setattr(c, k, v)
    db.commit()
    return _row(c, "id", "subject_id", "number", "title", "semester")


class TopicIn(BaseModel):
    chapter_id: int
    title: str = Field(min_length=2, max_length=160)
    sort_order: int = 0
    home_activity: str | None = Field(default=None, max_length=1000)
    common_mistake: str | None = Field(default=None, max_length=500)


@router.post("/topics", status_code=201)
def create_topic(body: TopicIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, Chapter, body.chapter_id)
    t = Topic(**body.model_dump())
    db.add(t)
    db.commit()
    return _row(t, "id", "chapter_id", "title", "sort_order", "home_activity", "common_mistake")


@router.get("/topics/{tid}")
def get_topic(tid: int, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    row = db.execute(select(Topic, Chapter.subject_id, Grade.number).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id).where(Topic.id == tid)).first()
    if row is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Topik tidak ditemukan")
    t, subject_id, grade = row
    return {"id": t.id, "title": t.title, "chapter_id": t.chapter_id, "subject_id": subject_id, "grade_number": grade}


@router.put("/topics/{tid}")
def update_topic(tid: int, body: TopicIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    t = _get(db, Topic, tid)
    for k, v in body.model_dump().items():
        setattr(t, k, v)
    db.commit()
    return _row(t, "id", "chapter_id", "title", "sort_order", "home_activity", "common_mistake")


class ObjectiveIn(BaseModel):
    topic_id: int
    code: str | None = None
    outcome: str | None = None
    description: str = Field(min_length=3)
    source_id: int | None = None


@router.post("/objectives", status_code=201)
def create_objective(body: ObjectiveIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, Topic, body.topic_id)
    st = "unverified"
    if body.source_id:
        src = _get(db, CurriculumSource, body.source_id)
        st = "verified" if src.verification_status == "verified" else "unverified"
    o = LearningObjective(**body.model_dump(), status=st)
    db.add(o)
    db.commit()
    return _row(o, "id", "topic_id", "code", "description", "status", "source_id")


def _topic_grade(db: Session, topic_id: int) -> tuple[int, str]:
    row = db.execute(select(Grade.number, Topic.title).join(Subject, Subject.grade_id == Grade.id).join(Chapter, Chapter.subject_id == Subject.id).join(Topic, Topic.chapter_id == Chapter.id).where(Topic.id == topic_id)).first()
    if row is None:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Topik tidak valid")
    return row[0], row[1]


class BlockIn(BaseModel):
    kind: str = Field(min_length=2, max_length=30)
    text: str | None = Field(default=None, max_length=5000)
    points: list[str] | None = None
    visual: str | None = Field(default=None, max_length=30)


class LessonIn(BaseModel):
    topic_id: int
    title: str = Field(min_length=2, max_length=160)
    minutes: int = Field(ge=1, le=120)
    blocks: list[BlockIn] = Field(min_length=1, max_length=40)


def _lesson_out(l: Lesson, db: Session | None = None) -> dict:
    d = {"id": l.id, "topic_id": l.topic_id, "title": l.title, "minutes": l.minutes, "status": l.status, "version": l.version, "is_sample": l.is_sample,
         "blocks": [{"kind": b.kind, "text": b.text, "points": b.points, "visual": b.visual} for b in l.blocks], "updated_at": l.updated_at.isoformat() if l.updated_at else None}
    if db is not None:
        d["reviews"] = [{"decision": r.decision, "notes": r.notes, "at": r.created_at.isoformat()} for r in db.scalars(select(ContentReview).where(ContentReview.entity_type == "lesson", ContentReview.entity_id == l.id).order_by(ContentReview.id.desc()))]
        d["topic"] = db.get(Topic, l.topic_id).title
    return d


@router.get("/lessons")
def list_lessons(status_filter: str | None = None, topic_id: int | None = None, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    q = select(Lesson)
    if status_filter:
        q = q.where(Lesson.status == status_filter)
    if topic_id:
        q = q.where(Lesson.topic_id == topic_id)
    return [_lesson_out(l, db) for l in db.scalars(q.order_by(Lesson.updated_at.desc()).limit(200))]


@router.get("/lessons/{lid}")
def get_lesson(lid: int, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return _lesson_out(_get(db, Lesson, lid), db)


def _set_blocks(l: Lesson, blocks: list[BlockIn]) -> None:
    l.blocks.clear()
    for i, b in enumerate(blocks):
        l.blocks.append(LessonBlock(position=i, kind=b.kind, text=b.text, points=b.points, visual=b.visual))


@router.post("/lessons", status_code=201)
def create_lesson(body: LessonIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _topic_grade(db, body.topic_id)
    l = Lesson(topic_id=body.topic_id, title=body.title, minutes=body.minutes, status="draft", author_id=ctx.user.id)
    _set_blocks(l, body.blocks)
    db.add(l)
    db.flush()
    audit(db, "lesson.create", ctx.user.id, "editor", "lesson", l.id)
    db.commit()
    return _lesson_out(l, db)


@router.put("/lessons/{lid}")
def update_lesson(lid: int, body: LessonIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    l = _get(db, Lesson, lid)
    _topic_grade(db, body.topic_id)
    was_published = l.status == "published"
    l.topic_id, l.title, l.minutes, l.status, l.is_sample = body.topic_id, body.title, body.minutes, "draft", False
    _set_blocks(l, body.blocks)
    if was_published:
        retrieval.unindex(db, "lesson", l.id)
    audit(db, "lesson.update", ctx.user.id, "editor", "lesson", l.id, {"unpublished": was_published})
    db.commit()
    return _lesson_out(l, db)


class ReviewIn(BaseModel):
    decision: Literal["approve", "reject"]
    notes: str | None = Field(default=None, max_length=2000)


def _transition(obj, allowed: tuple[str, ...], to: str) -> None:
    if obj.status not in allowed:
        raise HTTPException(status.HTTP_409_CONFLICT, f"Status {obj.status} tidak bisa diubah ke {to}")
    obj.status = to


@router.post("/lessons/{lid}/submit")
def submit_lesson(lid: int, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    l = _get(db, Lesson, lid)
    _transition(l, ("draft", "rejected"), "in_review")
    db.commit()
    return _lesson_out(l, db)


def _check_reviewer(ctx: ParentCtx, author_id) -> None:
    if author_id is not None and author_id == ctx.user.id and "admin" not in ctx.roles:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Peninjau tidak boleh menyetujui konten buatannya sendiri")


@router.post("/lessons/{lid}/review")
def review_lesson(lid: int, body: ReviewIn, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    l = _get(db, Lesson, lid)
    _check_reviewer(ctx, l.author_id)
    _transition(l, ("in_review",), "approved" if body.decision == "approve" else "rejected")
    db.add(ContentReview(entity_type="lesson", entity_id=l.id, reviewer_id=ctx.user.id, decision=body.decision, notes=body.notes))
    audit(db, "lesson.review", ctx.user.id, "reviewer", "lesson", l.id, body.model_dump())
    db.commit()
    return _lesson_out(l, db)


@router.post("/lessons/{lid}/publish")
def publish_lesson(lid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    l = _get(db, Lesson, lid)
    _transition(l, ("approved",), "published")
    l.version += 1
    l.published_at = utcnow()
    grade, _ = _topic_grade(db, l.topic_id)
    db.add(ContentVersion(entity_type="lesson", entity_id=l.id, version=l.version, snapshot=_lesson_out(l), published_by=ctx.user.id))
    retrieval.index_lesson(db, l, grade)
    audit(db, "lesson.publish", ctx.user.id, "reviewer", "lesson", l.id, {"version": l.version})
    db.commit()
    return _lesson_out(l, db)


@router.post("/lessons/{lid}/unpublish")
def unpublish_lesson(lid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    l = _get(db, Lesson, lid)
    _transition(l, ("published",), "draft")
    retrieval.unindex(db, "lesson", l.id)
    audit(db, "lesson.unpublish", ctx.user.id, "reviewer", "lesson", l.id)
    db.commit()
    return _lesson_out(l, db)


class OptionIn(BaseModel):
    label: str = Field(min_length=1, max_length=500)
    side: Literal["a", "b"] = "a"


class QuestionIn(BaseModel):
    topic_id: int
    learning_objective_id: int | None = None
    type: str
    body: str = Field(min_length=2, max_length=3000)
    difficulty: Literal["mudah", "sedang", "menantang"] = "mudah"
    options: list[OptionIn] = Field(default_factory=list, max_length=12)
    answer: dict | None = None
    rubric: str | None = None
    usage: Literal["practice", "assessment", "both"] = "both"
    explanation: str = Field(min_length=3, max_length=3000)
    mistake_hint: str | None = Field(default=None, max_length=1000)
    source: str = Field(min_length=2, max_length=300)
    source_reference: str | None = None


def _question_out(q: Question, db: Session | None = None) -> dict:
    d = {"id": q.id, "topic_id": q.topic_id, "learning_objective_id": q.learning_objective_id, "type": q.type, "body": q.body, "difficulty": q.difficulty,
         "options": [{"label": o.label, "side": o.side} for o in q.options], "answer": q.answer, "rubric": q.rubric, "usage": q.usage, "status": q.status, "version": q.version, "is_sample": q.is_sample,
         "explanation": q.explanation.explanation if q.explanation else "", "mistake_hint": q.explanation.mistake_hint if q.explanation else None,
         "source": q.sources[0].source if q.sources else "", "source_reference": q.sources[0].reference if q.sources else None}
    if db is not None:
        d["reviews"] = [{"decision": r.decision, "notes": r.notes, "at": r.created_at.isoformat()} for r in db.scalars(select(QuestionReview).where(QuestionReview.question_id == q.id).order_by(QuestionReview.id.desc()))]
        d["topic"] = db.get(Topic, q.topic_id).title
    return d


def _apply_question(q: Question, body: QuestionIn) -> None:
    if body.type not in QUESTION_TYPES:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Tipe soal tidak dikenal")
    opts = body.options
    if body.type == "tf" and not opts:
        opts = [OptionIn(label="Benar"), OptionIn(label="Salah")]
    if body.type in ("mc", "multi") and len(opts) < 2:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Minimal dua pilihan jawaban")
    if body.type == "essay" and not body.rubric:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Soal esai wajib memiliki rubrik penilaian")
    err = validate_answer_shape(body.type, body.answer, len(opts))
    if err:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, err)
    q.topic_id, q.learning_objective_id, q.type, q.body, q.difficulty, q.answer, q.rubric, q.usage = body.topic_id, body.learning_objective_id, body.type, body.body, body.difficulty, body.answer, body.rubric, body.usage
    q.options.clear()
    for i, o in enumerate(opts):
        q.options.append(QuestionOption(position=i, label=o.label, side=o.side))
    if q.explanation is None:
        q.explanation = QuestionExplanation(explanation=body.explanation, mistake_hint=body.mistake_hint)
    else:
        q.explanation.explanation, q.explanation.mistake_hint = body.explanation, body.mistake_hint
    q.sources.clear()
    q.sources.append(QuestionSource(source=body.source, reference=body.source_reference))


@router.get("/questions")
def list_questions(status_filter: str | None = None, topic_id: int | None = None, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    q = select(Question)
    if status_filter:
        q = q.where(Question.status == status_filter)
    if topic_id:
        q = q.where(Question.topic_id == topic_id)
    return [_question_out(x, db) for x in db.scalars(q.order_by(Question.updated_at.desc()).limit(300))]


@router.get("/questions/{qid}")
def get_question(qid: int, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return _question_out(_get(db, Question, qid), db)


@router.post("/questions", status_code=201)
def create_question(body: QuestionIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _topic_grade(db, body.topic_id)
    q = Question(status="draft", author_id=ctx.user.id, topic_id=body.topic_id, type=body.type, body=body.body)
    _apply_question(q, body)
    db.add(q)
    db.flush()
    audit(db, "question.create", ctx.user.id, "editor", "question", q.id)
    db.commit()
    return _question_out(q, db)


@router.put("/questions/{qid}")
def update_question(qid: int, body: QuestionIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    q = _get(db, Question, qid)
    _topic_grade(db, body.topic_id)
    in_use = db.scalar(select(func.count()).select_from(AssessmentQuestion).join(Assessment, Assessment.id == AssessmentQuestion.assessment_id).where(AssessmentQuestion.question_id == q.id, Assessment.status == "published")) or 0
    if in_use:
        raise HTTPException(status.HTTP_409_CONFLICT, "Soal dipakai di asesmen yang sudah terbit. Tarik asesmen dulu.")
    was = q.status == "published"
    _apply_question(q, body)
    q.status, q.is_sample = "draft", False
    if was:
        retrieval.unindex(db, "question", q.id)
    audit(db, "question.update", ctx.user.id, "editor", "question", q.id, {"unpublished": was})
    db.commit()
    return _question_out(q, db)


@router.post("/questions/{qid}/submit")
def submit_question(qid: int, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    q = _get(db, Question, qid)
    _transition(q, ("draft", "rejected"), "in_review")
    db.commit()
    return _question_out(q, db)


@router.post("/questions/{qid}/review")
def review_question(qid: int, body: ReviewIn, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    q = _get(db, Question, qid)
    _check_reviewer(ctx, q.author_id)
    _transition(q, ("in_review",), "approved" if body.decision == "approve" else "rejected")
    db.add(QuestionReview(question_id=q.id, reviewer_id=ctx.user.id, decision=body.decision, notes=body.notes))
    audit(db, "question.review", ctx.user.id, "reviewer", "question", q.id, body.model_dump())
    db.commit()
    return _question_out(q, db)


@router.post("/questions/{qid}/publish")
def publish_question(qid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    q = _get(db, Question, qid)
    _transition(q, ("approved",), "published")
    q.version += 1
    q.published_at = utcnow()
    grade, title = _topic_grade(db, q.topic_id)
    db.add(QuestionVersion(question_id=q.id, version=q.version, snapshot=_question_out(q)))
    retrieval.index_question(db, q, grade, title)
    audit(db, "question.publish", ctx.user.id, "reviewer", "question", q.id, {"version": q.version})
    db.commit()
    return _question_out(q, db)


@router.post("/questions/{qid}/unpublish")
def unpublish_question(qid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    q = _get(db, Question, qid)
    in_use = db.scalar(select(func.count()).select_from(AssessmentQuestion).join(Assessment, Assessment.id == AssessmentQuestion.assessment_id).where(AssessmentQuestion.question_id == q.id, Assessment.status == "published")) or 0
    if in_use:
        raise HTTPException(status.HTTP_409_CONFLICT, "Soal dipakai di asesmen yang sudah terbit")
    _transition(q, ("published",), "draft")
    retrieval.unindex(db, "question", q.id)
    db.commit()
    return _question_out(q, db)


@router.get("/assessment-templates")
def templates(ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return [_row(t, "id", "code", "label", "description") for t in db.scalars(select(AssessmentTemplate).order_by(AssessmentTemplate.id))]


class TemplateIn(BaseModel):
    code: str = Field(min_length=2, max_length=30)
    label: str = Field(min_length=2, max_length=120)
    description: str | None = None


@router.post("/assessment-templates", status_code=201)
def create_template(body: TemplateIn, ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    t = AssessmentTemplate(**body.model_dump())
    db.add(t)
    db.commit()
    return _row(t, "id", "code", "label", "description")


class AssessmentIn(BaseModel):
    template_id: int
    title: str = Field(min_length=3, max_length=200)
    short_title: str = Field(min_length=2, max_length=80)
    subject_id: int
    grade_number: int = Field(ge=1, le=9)
    semester: int | None = Field(default=None, ge=1, le=2)
    duration_minutes: int = Field(ge=1, le=240)
    shuffle_questions: bool = True
    shuffle_options: bool = True
    passing_score: float | None = Field(default=None, ge=0, le=100)
    show_result: Literal["immediate", "after_review"] = "immediate"
    difficulty_distribution: dict | None = None
    question_ids: list[int] = Field(min_length=1, max_length=100)


def _assessment_out(db: Session, a: Assessment) -> dict:
    links = list(db.scalars(select(AssessmentQuestion).where(AssessmentQuestion.assessment_id == a.id).order_by(AssessmentQuestion.position)))
    return {**_row(a, "id", "template_id", "title", "short_title", "subject_id", "grade_number", "semester", "duration_minutes", "shuffle_questions", "shuffle_options", "passing_score", "show_result", "difficulty_distribution", "status", "is_sample"),
            "question_ids": [l.question_id for l in links]}


def _apply_assessment(db: Session, a: Assessment, body: AssessmentIn) -> None:
    _get(db, AssessmentTemplate, body.template_id)
    sub = _get(db, Subject, body.subject_id)
    if db.get(Grade, sub.grade_id).number != body.grade_number:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Kelas asesmen harus sama dengan kelas mata pelajaran")
    for k, v in body.model_dump(exclude={"question_ids"}).items():
        setattr(a, k, v)
    db.flush()
    db.query(AssessmentQuestion).filter(AssessmentQuestion.assessment_id == a.id).delete()
    for i, qid in enumerate(dict.fromkeys(body.question_ids)):
        q = _get(db, Question, qid)
        if q.usage == "practice":
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, f"Soal {qid} hanya untuk latihan")
        db.add(AssessmentQuestion(assessment_id=a.id, question_id=qid, position=i))


@router.get("/assessments")
def list_assessments(ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    return [_assessment_out(db, a) for a in db.scalars(select(Assessment).order_by(Assessment.id.desc()))]


@router.post("/assessments", status_code=201)
def create_assessment(body: AssessmentIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    a = Assessment(status="draft", template_id=body.template_id, title=body.title, short_title=body.short_title, subject_id=body.subject_id, grade_number=body.grade_number, duration_minutes=body.duration_minutes)
    db.add(a)
    db.flush()
    _apply_assessment(db, a, body)
    db.commit()
    return _assessment_out(db, a)


@router.put("/assessments/{aid}")
def update_assessment(aid: int, body: AssessmentIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    a = _get(db, Assessment, aid)
    if a.status == "published":
        raise HTTPException(status.HTTP_409_CONFLICT, "Tarik asesmen dulu sebelum mengubah")
    _apply_assessment(db, a, body)
    db.commit()
    return _assessment_out(db, a)


@router.post("/assessments/{aid}/publish")
def publish_assessment(aid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    a = _get(db, Assessment, aid)
    unpublished = db.scalar(select(func.count()).select_from(AssessmentQuestion).join(Question, Question.id == AssessmentQuestion.question_id).where(AssessmentQuestion.assessment_id == a.id, Question.status != "published")) or 0
    if unpublished:
        raise HTTPException(status.HTTP_409_CONFLICT, f"{unpublished} soal belum terbit. Semua soal asesmen harus sudah ditinjau dan terbit.")
    _transition(a, ("draft",), "published")
    audit(db, "assessment.publish", ctx.user.id, "reviewer", "assessment", a.id)
    db.commit()
    return _assessment_out(db, a)


@router.post("/assessments/{aid}/unpublish")
def unpublish_assessment(aid: int, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    a = _get(db, Assessment, aid)
    _transition(a, ("published",), "draft")
    db.commit()
    return _assessment_out(db, a)


@router.get("/essay-reviews")
def essay_reviews(ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    rows = db.execute(select(AssessmentAnswer, Question).join(Question, Question.id == AssessmentAnswer.question_id).where(AssessmentAnswer.needs_review.is_(True), AssessmentAnswer.reviewed_by.is_(None)).limit(100)).all()
    return [{"answer_id": a.id, "question": q.body, "rubric": q.rubric, "response": (a.response or {}).get("text"), "ai_suggested_points": a.ai_suggested_points, "ai_suggestion_reason": a.ai_suggestion_reason} for a, q in rows]


class ScoreIn(BaseModel):
    correct: bool


@router.post("/assessment-answers/{ans_id}/score")
def score_essay(ans_id: int, body: ScoreIn, ctx: ParentCtx = Depends(reviewer), db: Session = Depends(get_db)):
    ans = _get(db, AssessmentAnswer, ans_id)
    if not ans.needs_review:
        raise HTTPException(status.HTTP_409_CONFLICT, "Jawaban ini tidak memerlukan penilaian manual")
    sess = db.get(AssessmentSession, ans.session_id)
    pts = db.scalar(select(AssessmentQuestion.points).where(AssessmentQuestion.assessment_id == sess.assessment_id, AssessmentQuestion.question_id == ans.question_id)) or 1.0
    ans.is_correct, ans.points_awarded, ans.reviewed_by, ans.needs_review = body.correct, pts if body.correct else 0.0, ctx.user.id, False
    db.flush()
    res = db.scalar(select(AssessmentResult).where(AssessmentResult.session_id == sess.id))
    all_ans = list(db.scalars(select(AssessmentAnswer).where(AssessmentAnswer.session_id == sess.id)))
    total = sum(db.scalar(select(AssessmentQuestion.points).where(AssessmentQuestion.assessment_id == sess.assessment_id, AssessmentQuestion.question_id == x.question_id)) or 1.0 for x in all_ans)
    got = sum(x.points_awarded or 0.0 for x in all_ans)
    res.score = round(got / total * 100, 1) if total else 0.0
    res.correct_count = sum(1 for x in all_ans if x.is_correct)
    res.pending_review_count = sum(1 for x in all_ans if x.needs_review)
    res.is_final = res.pending_review_count == 0
    audit(db, "assessment.essay_scored", ctx.user.id, "reviewer", "assessment_answer", ans.id, body.model_dump())
    db.commit()
    return {"score": res.score, "final": res.is_final}


@router.get("/export")
def export(grade: int | None = None, ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    q = select(Subject).join(Grade, Grade.id == Subject.grade_id)
    if grade:
        q = q.where(Grade.number == grade)
    out = []
    for s in db.scalars(q):
        tree = subject_tree(s.id, ctx, db)
        for ch in tree["chapters"]:
            for t in ch["topics"]:
                t["lessons"] = [_lesson_out(l) for l in db.scalars(select(Lesson).where(Lesson.topic_id == t["id"]))]
                t["questions"] = [_question_out(x) for x in db.scalars(select(Question).where(Question.topic_id == t["id"]))]
        out.append(tree)
    return {"format": "bobo-content-v1", "exported_at": utcnow().isoformat(), "subjects": out}


class ImportIn(BaseModel):
    format: Literal["bobo-content-v1"]
    curriculum_version_id: int
    subjects: list[dict] = Field(max_length=50)


@router.post("/import")
def import_content(body: ImportIn, ctx: ParentCtx = Depends(editor), db: Session = Depends(get_db)):
    _get(db, CurriculumVersion, body.curriculum_version_id)
    counts = {"subjects": 0, "chapters": 0, "topics": 0, "lessons": 0, "questions": 0, "errors": []}
    for sd in body.subjects:
        try:
            s = Subject(curriculum_version_id=body.curriculum_version_id, grade_id=_grade_id(db, int(sd["grade_number"])), code=sd["code"], name=sd["name"], short_label=sd.get("short_label", sd["name"][:2]), sort_order=sd.get("sort_order", 0))
            db.add(s)
            db.flush()
            counts["subjects"] += 1
            for cd in sd.get("chapters", []):
                c = Chapter(subject_id=s.id, number=cd["number"], title=cd["title"], semester=cd.get("semester"))
                db.add(c)
                db.flush()
                counts["chapters"] += 1
                for td in cd.get("topics", []):
                    t = Topic(chapter_id=c.id, title=td["title"], sort_order=td.get("sort_order", 0), home_activity=td.get("home_activity"), common_mistake=td.get("common_mistake"))
                    db.add(t)
                    db.flush()
                    counts["topics"] += 1
                    for ld in td.get("lessons", []):
                        l = Lesson(topic_id=t.id, title=ld["title"], minutes=ld.get("minutes", 5), status="draft", author_id=ctx.user.id)
                        _set_blocks(l, [BlockIn(**b) for b in ld["blocks"]])
                        db.add(l)
                        counts["lessons"] += 1
                    for qd in td.get("questions", []):
                        qin = QuestionIn(**{**qd, "topic_id": t.id, "learning_objective_id": None})
                        q = Question(status="draft", author_id=ctx.user.id, topic_id=t.id, type=qin.type, body=qin.body)
                        _apply_question(q, qin)
                        db.add(q)
                        counts["questions"] += 1
        except (KeyError, ValueError, HTTPException) as e:
            db.rollback()
            detail = e.detail if isinstance(e, HTTPException) else str(e)
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, f"Impor gagal pada mata pelajaran {sd.get('name', '?')}: {detail}")
    audit(db, "content.import", ctx.user.id, "editor", meta={k: v for k, v in counts.items() if k != "errors"})
    db.commit()
    return {**counts, "note": "Semua konten hasil impor berstatus draft dan wajib ditinjau sebelum terbit."}


@router.get("/ai/usage")
def ai_usage(days: int = 7, ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    since = utcnow() - timedelta(days=max(1, min(days, 90)))
    day = func.date_trunc("day", AIUsageLog.created_at)
    rows = db.execute(
        select(day, AIUsageLog.purpose, func.count(), func.sum(AIUsageLog.cost_usd), func.sum(AIUsageLog.input_tokens), func.sum(AIUsageLog.output_tokens))
        .where(AIUsageLog.created_at >= since).group_by(day, AIUsageLog.purpose).order_by(day)
    ).all()
    active = db.scalar(select(func.count(func.distinct(AIUsageLog.student_id))).where(AIUsageLog.created_at >= since, AIUsageLog.purpose == "tutor")) or 0
    total_cost = float(db.scalar(select(func.coalesce(func.sum(AIUsageLog.cost_usd), 0.0)).where(AIUsageLog.created_at >= since)) or 0.0)
    outcomes = dict(db.execute(select(AIUsageLog.outcome, func.count()).where(AIUsageLog.created_at >= since).group_by(AIUsageLog.outcome)).all())
    return {"days": days, "rows": [{"day": r[0].date().isoformat(), "purpose": r[1], "requests": r[2], "cost_usd": round(float(r[3] or 0), 4), "input_tokens": int(r[4] or 0), "output_tokens": int(r[5] or 0)} for r in rows],
            "active_students": active, "total_cost_usd": round(total_cost, 4), "cost_per_active_student_usd": round(total_cost / active, 4) if active else 0.0, "outcomes": outcomes}


class PromptIn(BaseModel):
    purpose: Literal["tutor", "parent"]
    template: str = Field(min_length=20, max_length=4000)
    activate: bool = True


@router.get("/ai/prompts")
def prompts(ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    return [_row(p, "id", "purpose", "version", "template", "is_active") for p in db.scalars(select(AIPromptVersion).order_by(AIPromptVersion.purpose, AIPromptVersion.version.desc()))]


@router.post("/ai/prompts", status_code=201)
def create_prompt(body: PromptIn, ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    for key in ("{grade}", "{level}"):
        if key not in body.template:
            raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, f"Template wajib memuat {key}")
    nxt = (db.scalar(select(func.max(AIPromptVersion.version)).where(AIPromptVersion.purpose == body.purpose)) or 0) + 1
    if body.activate:
        for p in db.scalars(select(AIPromptVersion).where(AIPromptVersion.purpose == body.purpose)):
            p.is_active = False
    p = AIPromptVersion(purpose=body.purpose, version=nxt, template=body.template, is_active=body.activate)
    db.add(p)
    audit(db, "ai.prompt_version", ctx.user.id, "admin", "ai_prompt", None, {"purpose": body.purpose, "version": nxt})
    db.commit()
    return _row(p, "id", "purpose", "version", "template", "is_active")


@router.get("/stats")
def stats(ctx: ParentCtx = Depends(staff), db: Session = Depends(get_db)):
    def count(model, *where):
        return db.scalar(select(func.count()).select_from(model).where(*where)) or 0
    return {
        "lessons": {s: count(Lesson, Lesson.status == s) for s in ("draft", "in_review", "approved", "rejected", "published")},
        "questions": {s: count(Question, Question.status == s) for s in ("draft", "in_review", "approved", "rejected", "published")},
        "assessments_published": count(Assessment, Assessment.status == "published"),
        "students": count(StudentProfile, StudentProfile.deleted_at.is_(None)),
        "unverified_sources": count(CurriculumSource, CurriculumSource.verification_status != "verified"),
        "sample_content_published": count(Lesson, Lesson.is_sample.is_(True), Lesson.status == "published") + count(Question, Question.is_sample.is_(True), Question.status == "published"),
    }


@router.get("/audit")
def audit_log(ctx: ParentCtx = Depends(admin_only), db: Session = Depends(get_db)):
    return [{"at": a.created_at.isoformat(), "action": a.action, "actor": str(a.actor_user_id) if a.actor_user_id else None, "entity": f"{a.entity_type}:{a.entity_id}" if a.entity_type else None, "meta": a.meta} for a in db.scalars(select(AuditLog).order_by(AuditLog.id.desc()).limit(200))]
