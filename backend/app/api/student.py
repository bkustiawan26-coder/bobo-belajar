import random
import uuid
from typing import Literal
from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.db import get_db, utcnow
from app.core.deps import StudentCtx, current_student
from app.models import (
    Assessment, AssessmentAnswer, AssessmentQuestion, AssessmentResult, AssessmentSession, AssessmentTemplate, Chapter, ExerciseAttempt,
    Grade, Lesson, LessonProgress, ParentProfile, Question, StudentProfile, Subject, SyncJob, Topic,
)
from app.services import learning, support
from app.services.ai import service as ai
from app.services.grading import answer_text, grade, response_text

router = APIRouter(prefix="/student", tags=["student"])


def _parent(db: Session, ctx: StudentCtx) -> ParentProfile:
    p = db.scalar(select(ParentProfile).where(ParentProfile.user_id == ctx.guardian_user_id))
    if p is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Akun orang tua tidak ditemukan")
    return p


def _topic_grade(db: Session, topic_id: int) -> tuple[Topic, int, Subject] | None:
    row = db.execute(
        select(Topic, Grade.number, Subject).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id).where(Topic.id == topic_id)
    ).first()
    return (row[0], row[1], row[2]) if row else None


def question_payload(q: Question, topic_title: str | None = None, order: list[int] | None = None, with_key: bool = False, student: StudentProfile | None = None) -> dict:
    if order is None and student is not None:
        order = support.keep_options(q, student)
    opts = {o.position: o for o in q.options}
    seq = order if order else sorted(opts)
    d = {
        "id": q.id, "type": q.type, "body": q.body, "difficulty": q.difficulty, "topic_id": q.topic_id, "topic": topic_title,
        "options": [{"index": i, "label": opts[i].label, "side": opts[i].side} for i in seq if i in opts],
    }
    if with_key:
        d["answer"] = q.answer
        d["answer_text"] = answer_text(q)
        d["explanation"] = q.explanation.explanation if q.explanation else ""
        d["mistake_hint"] = q.explanation.mistake_hint if q.explanation else None
        d["scaffold"] = q.scaffold
    return d


def lesson_payload(l: Lesson, prog: LessonProgress | None) -> dict:
    return {
        "id": l.id, "topic_id": l.topic_id, "title": l.title, "minutes": l.minutes, "version": l.version, "reviewed": l.status == "published",
        "blocks": [{"position": b.position, "kind": b.kind, "text": b.text, "points": b.points, "visual": b.visual, "figure": b.figure} for b in l.blocks],
        "step": prog.step if prog else 0, "completed": bool(prog and prog.completed_at), "downloaded": bool(prog and prog.downloaded),
    }


@router.get("/me")
def me(ctx: StudentCtx = Depends(current_student)):
    s = ctx.student
    return {"id": str(s.id), "nickname": s.nickname, "grade": s.grade_number, "level": learning.level(s.grade_number), "phase": learning.phase(s.grade_number), "band": learning.band(s.grade_number), "settings": support.clean_settings(s.settings)}


@router.get("/catalog")
def catalog(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    v = learning.active_version(db)
    out = {"grade": s.grade_number, "phase": learning.phase(s.grade_number), "curriculum": f"{v.name} {v.version}" if v else None, "subjects": []}
    if v is None:
        return out
    subjects = list(db.scalars(select(Subject).join(Grade, Grade.id == Subject.grade_id).where(Subject.curriculum_version_id == v.id, Grade.number == s.grade_number, Subject.is_enabled.is_(True)).order_by(Subject.sort_order, Subject.id)))
    progress = {p.lesson_id: p for p in db.scalars(select(LessonProgress).where(LessonProgress.student_id == s.id))}
    for sub in subjects:
        chapters = list(db.scalars(select(Chapter).where(Chapter.subject_id == sub.id).order_by(Chapter.number)))
        ch_out, ready, n_topics = [], False, 0
        for ch in chapters:
            topics = list(db.scalars(select(Topic).where(Topic.chapter_id == ch.id).order_by(Topic.sort_order, Topic.id)))
            t_out = []
            for t in topics:
                lesson = db.scalar(select(Lesson).where(Lesson.topic_id == t.id, Lesson.status == "published").order_by(Lesson.id))
                nq = db.scalar(select(func.count()).select_from(Question).where(Question.topic_id == t.id, Question.status == "published", Question.usage.in_(["practice", "both"]))) or 0
                if lesson or nq:
                    ready = True
                p = progress.get(lesson.id) if lesson else None
                t_out.append({"id": t.id, "title": t.title, "question_count": nq, "lesson": {"id": lesson.id, "title": lesson.title, "minutes": lesson.minutes, "block_count": len(lesson.blocks), "step": p.step if p else 0, "completed": bool(p and p.completed_at), "downloaded": bool(p and p.downloaded)} if lesson else None})
            n_topics += len(t_out)
            ch_out.append({"id": ch.id, "number": ch.number, "title": ch.title, "topics": t_out})
        out["subjects"].append({"id": sub.id, "name": sub.name, "short_label": sub.short_label, "ready": ready, "topic_count": n_topics, "chapters": ch_out if ready else []})
    return out


def _lesson_for_student(db: Session, s: StudentProfile, lesson_id: int) -> Lesson:
    l = db.get(Lesson, lesson_id)
    if l is None or l.status != "published":
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Materi tidak ditemukan")
    if l.topic_id not in support.allowed_topic_ids(db, s):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Materi tidak ditemukan")
    return l


@router.get("/lessons/{lesson_id}")
def get_lesson(lesson_id: int, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    l = _lesson_for_student(db, ctx.student, lesson_id)
    p = db.scalar(select(LessonProgress).where(LessonProgress.student_id == ctx.student.id, LessonProgress.lesson_id == l.id))
    return lesson_payload(l, p)


class ProgressIn(BaseModel):
    step: int = Field(ge=0, le=200)
    completed: bool = False
    downloaded: bool | None = None


@router.post("/lessons/{lesson_id}/progress")
def lesson_progress(lesson_id: int, body: ProgressIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    l = _lesson_for_student(db, ctx.student, lesson_id)
    return _apply_progress(db, ctx.student, l, body.step, body.completed, body.downloaded, utcnow())


def _apply_progress(db: Session, s: StudentProfile, l: Lesson, step: int, completed: bool, downloaded: bool | None, when: datetime) -> dict:
    p = db.scalar(select(LessonProgress).where(LessonProgress.student_id == s.id, LessonProgress.lesson_id == l.id))
    if p is None:
        p = LessonProgress(student_id=s.id, lesson_id=l.id, step=0)
        db.add(p)
    p.step = min(step, max(0, len(l.blocks) - 1))
    if downloaded is not None:
        p.downloaded = downloaded
    first = completed and p.completed_at is None
    if completed and p.completed_at is None:
        p.completed_at = when
    if first:
        learning.log_activity(db, s.id, "lesson", f"Menyelesaikan materi {l.title}", l.topic_id, when)
    db.commit()
    return {"lesson_id": l.id, "step": p.step, "completed": p.completed_at is not None, "downloaded": p.downloaded}


def _grade_questions(db: Session, s: StudentProfile, usage: tuple[str, ...], allowed: set[int] | None = None):
    allowed = allowed if allowed is not None else support.allowed_topic_ids(db, s)
    return (
        select(Question, Topic.title).join(Topic, Topic.id == Question.topic_id)
        .where(Question.topic_id.in_(allowed or {-1}), Question.status == "published", Question.usage.in_(usage), Question.type != "essay")
    )


def _own_grade_ids(db: Session, s: StudentProfile) -> set[int]:
    return {t.id for t in learning.grade_topics(db, s.grade_number)}


@router.get("/practice")
def practice(topic_id: int | None = None, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    allowed = support.allowed_topic_ids(db, ctx.student) if topic_id is not None else _own_grade_ids(db, ctx.student)
    q = _grade_questions(db, ctx.student, ("practice", "both"), allowed)
    if topic_id is not None:
        q = q.where(Question.topic_id == topic_id)
    rows = db.execute(q.order_by(Topic.sort_order, Question.id)).all()
    return {"questions": [question_payload(r[0], r[1], student=ctx.student) for r in rows]}


@router.get("/practice/similar")
def similar(question_id: int, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    base = db.get(Question, question_id)
    if base is None or base.topic_id not in support.allowed_topic_ids(db, ctx.student):
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Soal tidak ditemukan")
    rank = {"mudah": 0, "sedang": 1, "menantang": 2}
    rows = db.execute(_grade_questions(db, ctx.student, ("practice", "both")).where(Question.topic_id == base.topic_id, Question.id != base.id)).all()
    solved = set(db.scalars(select(ExerciseAttempt.question_id).where(ExerciseAttempt.student_id == ctx.student.id, ExerciseAttempt.is_correct.is_(True))))
    cands = sorted(rows, key=lambda r: (rank.get(r[0].difficulty, 1) > rank.get(base.difficulty, 1), r[0].id in solved, rank.get(r[0].difficulty, 1), r[0].id))
    if not cands:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Belum ada soal serupa")
    return question_payload(cands[0][0], cands[0][1], student=ctx.student)


@router.get("/review")
def review(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    items = support.due_reviews(db, ctx.student.id, limit=5)
    qs = {q.id: q for q in db.scalars(select(Question).where(Question.id.in_([i.question_id for i in items]), Question.status == "published"))}
    titles = dict(db.execute(select(Topic.id, Topic.title).where(Topic.id.in_([q.topic_id for q in qs.values()]))).all())
    return {"due": support.due_count(db, ctx.student.id), "questions": [question_payload(qs[i.question_id], titles.get(qs[i.question_id].topic_id), student=ctx.student) for i in items if i.question_id in qs]}


@router.get("/foundation")
def foundation(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    return {"topics": support.foundation_suggestions(db, ctx.student)}


@router.get("/growth")
def growth(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    return support.growth(db, ctx.student)


class AttemptIn(BaseModel):
    client_uuid: uuid.UUID
    question_id: int
    response: dict | None
    answered_at: datetime | None = None
    mode: Literal["practice", "review", "foundation"] = "practice"


def _record_attempt(db: Session, s: StudentProfile, a: AttemptIn, offline: bool) -> tuple[dict, str]:
    existing = db.scalar(select(ExerciseAttempt).where(ExerciseAttempt.client_uuid == a.client_uuid))
    if existing is not None:
        if existing.student_id != s.id:
            return {"client_uuid": str(a.client_uuid), "error": "duplikat tidak valid"}, "rejected"
        q = db.get(Question, existing.question_id)
        return _attempt_result(db, q, existing.is_correct, a.client_uuid), "duplicate"
    row = db.execute(_grade_questions(db, s, ("practice", "both")).where(Question.id == a.question_id)).first()
    if row is None:
        return {"client_uuid": str(a.client_uuid), "error": "soal tidak tersedia"}, "rejected"
    q = row[0]
    now = utcnow()
    when = a.answered_at or now
    if when.tzinfo is None:
        when = when.replace(tzinfo=timezone.utc)
    if when > now + timedelta(minutes=5) or when < now - timedelta(days=30):
        return {"client_uuid": str(a.client_uuid), "error": "waktu jawaban tidak valid"}, "rejected"
    ok = bool(grade(q, a.response))
    source = {"practice": "latihan", "review": "review", "foundation": "pondasi"}[a.mode]
    db.add(ExerciseAttempt(client_uuid=a.client_uuid, student_id=s.id, question_id=q.id, topic_id=q.topic_id, response=a.response, is_correct=ok, source=source, answered_at=when, synced_offline=offline))
    support.schedule_review(db, s.id, q, ok, a.mode)
    db.flush()
    return _attempt_result(db, q, ok, a.client_uuid), "accepted"


def _attempt_result(db: Session, q: Question, ok: bool, cu: uuid.UUID) -> dict:
    lesson = db.scalar(select(Lesson.id).where(Lesson.topic_id == q.topic_id, Lesson.status == "published"))
    topic = db.get(Topic, q.topic_id)
    return {
        "client_uuid": str(cu), "question_id": q.id, "correct": ok, "correct_answer": answer_text(q), "answer_key": q.answer,
        "explanation": q.explanation.explanation if q.explanation else "", "mistake_hint": None if ok else (q.explanation.mistake_hint if q.explanation else None),
        "topic_id": q.topic_id, "topic": topic.title if topic else None, "related_lesson_id": lesson, "scaffold": None if ok else q.scaffold,
    }


@router.post("/practice/attempts")
def attempt(body: AttemptIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    res, st = _record_attempt(db, ctx.student, body, False)
    if st == "rejected":
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, res.get("error"))
    if st == "accepted":
        learning.refresh_mastery(db, ctx.student, {res["topic_id"]})
    db.commit()
    return res


class SyncProgress(BaseModel):
    lesson_id: int
    step: int = Field(ge=0, le=200)
    completed: bool = False
    at: datetime | None = None


class SyncIn(BaseModel):
    batch_uuid: uuid.UUID
    attempts: list[AttemptIn] = Field(default_factory=list, max_length=500)
    lesson_progress: list[SyncProgress] = Field(default_factory=list, max_length=200)


@router.post("/sync")
def sync(body: SyncIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    job = db.scalar(select(SyncJob).where(SyncJob.batch_uuid == body.batch_uuid))
    results, topics = [], set()
    counts = {"accepted": 0, "duplicate": 0, "rejected": 0}
    for a in body.attempts:
        r, st = _record_attempt(db, s, a, True)
        counts[st] += 1
        r["status"] = st
        results.append(r)
        if st == "accepted":
            topics.add(r["topic_id"])
    if counts["accepted"]:
        learning.log_activity(db, s.id, "practice", f"Menyinkronkan {counts['accepted']} jawaban latihan offline")
    for p in body.lesson_progress:
        try:
            l = _lesson_for_student(db, s, p.lesson_id)
        except HTTPException:
            continue
        _apply_progress(db, s, l, p.step, p.completed, None, p.at or utcnow())
    learning.refresh_mastery(db, s, topics)
    if job is None:
        db.add(SyncJob(student_id=s.id, batch_uuid=body.batch_uuid, received=len(body.attempts), accepted=counts["accepted"], duplicates=counts["duplicate"], rejected=counts["rejected"]))
    db.commit()
    return {"batch_uuid": str(body.batch_uuid), "summary": counts, "results": results}


@router.get("/offline-pack")
def offline_pack(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    v = learning.active_version(db)
    lessons = []
    if v is not None:
        ls = db.scalars(
            select(Lesson).join(Topic, Topic.id == Lesson.topic_id).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id)
            .where(Grade.number == s.grade_number, Subject.curriculum_version_id == v.id, Lesson.status == "published")
        ).all()
        for l in ls:
            p = db.scalar(select(LessonProgress).where(LessonProgress.student_id == s.id, LessonProgress.lesson_id == l.id))
            if p is None:
                p = LessonProgress(student_id=s.id, lesson_id=l.id, step=0)
                db.add(p)
            p.downloaded = True
            lessons.append(lesson_payload(l, p))
    rows = db.execute(_grade_questions(db, s, ("practice", "both"), _own_grade_ids(db, s))).all()
    db.commit()
    return {"generated_at": utcnow().isoformat(), "grade": s.grade_number, "lessons": lessons, "questions": [question_payload(r[0], r[1], with_key=True, student=s) for r in rows], "note": "Paket latihan offline. Asesmen formal tidak tersedia offline."}


@router.get("/home")
def home(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    parent = _parent(db, ctx)
    quota = ai.tutor_quota(db, s, parent)
    m = learning.mastery_for(db, s)
    cont = None
    v = learning.active_version(db)
    if v is not None:
        rows = db.execute(
            select(Lesson, LessonProgress).join(Topic, Topic.id == Lesson.topic_id).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id)
            .outerjoin(LessonProgress, (LessonProgress.lesson_id == Lesson.id) & (LessonProgress.student_id == s.id))
            .where(Grade.number == s.grade_number, Subject.curriculum_version_id == v.id, Lesson.status == "published")
            .order_by(Subject.sort_order, Chapter.number, Topic.sort_order)
        ).all()
        pick = next(((l, p) for l, p in rows if p is not None and p.completed_at is None), None) or next(((l, p) for l, p in rows if p is None), None) or (rows[0] if rows else None)
        if pick:
            l, p = pick
            sub = db.execute(select(Subject.name).join(Chapter, Chapter.subject_id == Subject.id).join(Topic, Topic.chapter_id == Chapter.id).where(Topic.id == l.topic_id)).scalar()
            cont = {"lesson_id": l.id, "title": l.title, "subject": sub, "step": p.step if p else 0, "block_count": len(l.blocks), "completed": bool(p and p.completed_at)}
    return {"targets": learning.today_targets(db, s, quota["used"]), "continue_lesson": cont, "developing_topics": [{"topic_id": x["topic_id"], "topic": x["topic"]} for x in m if x["state"] == "developing"], "tutor_quota": quota,
            "review_due": support.due_count(db, s.id), "foundation": support.foundation_suggestions(db, s), "settings": support.clean_settings(s.settings)}


@router.get("/progress")
def progress(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    return {"mastery": [{k: v for k, v in x.items() if k not in ("home_activity", "common_mistake")} for x in learning.mastery_for(db, ctx.student)]}


class TutorIn(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    conversation_id: uuid.UUID | None = None
    topic_id: int | None = None
    style: Literal["story", "visual", "steps"] | None = None


@router.post("/tutor/messages")
def tutor(body: TutorIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    return ai.tutor_reply(db, ctx.student, _parent(db, ctx), body.text.strip(), body.conversation_id, body.topic_id, body.style)


@router.get("/tutor/quota")
def tutor_quota(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    return ai.tutor_quota(db, ctx.student, _parent(db, ctx))


def _assessment_for(db: Session, s: StudentProfile, aid: int) -> Assessment:
    a = db.get(Assessment, aid)
    if a is None or a.status != "published" or a.grade_number != s.grade_number:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Asesmen tidak ditemukan")
    return a


def _finalize_expired(db: Session, s: StudentProfile) -> None:
    grace = timedelta(seconds=get_settings().assessment_grace_seconds)
    now = utcnow()
    for sess in db.scalars(select(AssessmentSession).where(AssessmentSession.student_id == s.id, AssessmentSession.status == "active")):
        if sess.deadline_at + grace < now:
            finalize(db, s, sess, auto=True)


@router.get("/assessments")
def assessments(ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    _finalize_expired(db, s)
    db.commit()
    rows = db.execute(select(Assessment, AssessmentTemplate.label).join(AssessmentTemplate, AssessmentTemplate.id == Assessment.template_id).where(Assessment.grade_number == s.grade_number, Assessment.status == "published").order_by(Assessment.id)).all()
    out = []
    for a, label in rows:
        n = db.scalar(select(func.count()).select_from(AssessmentQuestion).where(AssessmentQuestion.assessment_id == a.id)) or 0
        last = db.scalar(select(AssessmentResult).where(AssessmentResult.student_id == s.id, AssessmentResult.assessment_id == a.id).order_by(AssessmentResult.created_at.desc()))
        active = db.scalar(select(AssessmentSession.id).where(AssessmentSession.student_id == s.id, AssessmentSession.assessment_id == a.id, AssessmentSession.status == "active"))
        out.append({"id": a.id, "type": label, "title": a.title, "duration_minutes": a.duration_minutes, "question_count": n, "active_session_id": str(active) if active else None,
                    "last_result": {"score": round(last.score), "date": learning.relative_label(last.created_at), "final": last.is_final} if last else None})
    templates = db.scalars(select(AssessmentTemplate).order_by(AssessmentTemplate.id)).all()
    available = {r[1] for r in rows}
    return {"assessments": out, "upcoming": [t.label for t in templates if t.label not in available]}


def _session_payload(db: Session, sess: AssessmentSession, a: Assessment) -> dict:
    qs = {q.id: q for q in db.scalars(select(Question).where(Question.id.in_(sess.question_order)))}
    titles = dict(db.execute(select(Topic.id, Topic.title).where(Topic.id.in_([q.topic_id for q in qs.values()]))).all())
    saved = {x.question_id: x.response for x in db.scalars(select(AssessmentAnswer).where(AssessmentAnswer.session_id == sess.id))}
    return {
        "session_id": str(sess.id), "assessment_id": a.id, "title": a.title, "status": sess.status, "started_at": sess.started_at.isoformat(), "deadline_at": sess.deadline_at.isoformat(), "server_now": utcnow().isoformat(),
        "questions": [question_payload(qs[qid], titles.get(qs[qid].topic_id), sess.option_orders.get(str(qid))) for qid in sess.question_order if qid in qs],
        "answers": {str(k): v for k, v in saved.items()},
    }


@router.post("/assessments/{aid}/start")
def start(aid: int, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    a = _assessment_for(db, s, aid)
    _finalize_expired(db, s)
    sess = db.scalar(select(AssessmentSession).where(AssessmentSession.student_id == s.id, AssessmentSession.assessment_id == a.id, AssessmentSession.status == "active"))
    if sess is None:
        links = list(db.scalars(select(AssessmentQuestion).where(AssessmentQuestion.assessment_id == a.id).order_by(AssessmentQuestion.position)))
        if not links:
            raise HTTPException(status.HTTP_409_CONFLICT, "Asesmen belum memiliki soal")
        order = [l.question_id for l in links]
        if a.shuffle_questions:
            random.shuffle(order)
        opt_orders = {}
        for q in db.scalars(select(Question).where(Question.id.in_(order))):
            if q.status != "published":
                raise HTTPException(status.HTTP_409_CONFLICT, "Asesmen berisi soal yang belum terbit")
            pos = [o.position for o in q.options]
            if a.shuffle_options and q.type in ("mc", "multi"):
                random.shuffle(pos)
            opt_orders[str(q.id)] = pos
        now = utcnow()
        sess = AssessmentSession(assessment_id=a.id, student_id=s.id, started_at=now, deadline_at=now + timedelta(minutes=a.duration_minutes), question_order=order, option_orders=opt_orders)
        db.add(sess)
        db.flush()
    db.commit()
    return _session_payload(db, sess, a)


def _own_session(db: Session, s: StudentProfile, sid: uuid.UUID) -> AssessmentSession:
    sess = db.get(AssessmentSession, sid)
    if sess is None or sess.student_id != s.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sesi asesmen tidak ditemukan")
    return sess


class AnswerIn(BaseModel):
    question_id: int
    response: dict | None


@router.put("/assessment-sessions/{sid}/answers")
def save_answer(sid: uuid.UUID, body: AnswerIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    sess = _own_session(db, ctx.student, sid)
    if sess.status != "active":
        raise HTTPException(status.HTTP_409_CONFLICT, "Asesmen sudah dikumpulkan")
    if utcnow() > sess.deadline_at + timedelta(seconds=get_settings().assessment_grace_seconds):
        raise HTTPException(status.HTTP_409_CONFLICT, "Waktu asesmen sudah habis")
    if body.question_id not in sess.question_order:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_CONTENT, "Soal bukan bagian dari asesmen ini")
    _upsert_answer(db, sess, body.question_id, body.response)
    db.commit()
    return {"saved": True, "question_id": body.question_id, "server_now": utcnow().isoformat()}


def _upsert_answer(db: Session, sess: AssessmentSession, qid: int, response: dict | None) -> None:
    row = db.scalar(select(AssessmentAnswer).where(AssessmentAnswer.session_id == sess.id, AssessmentAnswer.question_id == qid))
    if row is None:
        db.add(AssessmentAnswer(session_id=sess.id, question_id=qid, response=response))
    else:
        row.response = response


class SubmitIn(BaseModel):
    idempotency_key: str = Field(min_length=8, max_length=80)
    answers: list[AnswerIn] = Field(default_factory=list, max_length=200)


def finalize(db: Session, s: StudentProfile, sess: AssessmentSession, auto: bool, key: str | None = None) -> AssessmentResult:
    a = db.get(Assessment, sess.assessment_id)
    points = {l.question_id: l.points for l in db.scalars(select(AssessmentQuestion).where(AssessmentQuestion.assessment_id == a.id))}
    answers = {x.question_id: x for x in db.scalars(select(AssessmentAnswer).where(AssessmentAnswer.session_id == sess.id))}
    qs = {q.id: q for q in db.scalars(select(Question).where(Question.id.in_(sess.question_order)))}
    total_pts = sum(points.get(q, 1.0) for q in sess.question_order)
    got_pts, correct, pending, weak, topics = 0.0, 0, 0, [], set()
    now = utcnow()
    for qid in sess.question_order:
        q = qs[qid]
        ans = answers.get(qid)
        if ans is None:
            ans = AssessmentAnswer(session_id=sess.id, question_id=qid, response=None)
            db.add(ans)
        ok = grade(q, ans.response)
        if ok is None:
            ans.needs_review, ans.is_correct, ans.points_awarded = True, None, None
            pending += 1
            continue
        ans.is_correct = ok
        ans.points_awarded = points.get(qid, 1.0) if ok else 0.0
        got_pts += ans.points_awarded
        correct += int(ok)
        topics.add(q.topic_id)
        if not ok and q.topic_id not in weak:
            weak.append(q.topic_id)
        db.add(ExerciseAttempt(client_uuid=uuid.uuid5(sess.id, str(qid)), student_id=s.id, question_id=qid, topic_id=q.topic_id, response=ans.response, is_correct=ok, source="asesmen", answered_at=now))
    score = round(got_pts / total_pts * 100, 1) if total_pts else 0.0
    sess.status, sess.submitted_at, sess.auto_submitted, sess.submit_key = "submitted", now, auto, key
    res = AssessmentResult(session_id=sess.id, student_id=s.id, assessment_id=a.id, score=score, correct_count=correct, total_count=len(sess.question_order), pending_review_count=pending, weak_topic_ids=weak,
                           passed=None if a.passing_score is None else score >= a.passing_score, is_final=pending == 0)
    db.add(res)
    db.flush()
    learning.log_activity(db, s.id, "assessment", f"Asesmen {a.short_title}: nilai {round(score)}" + (" (menunggu penilaian esai)" if pending else ""))
    learning.refresh_mastery(db, s, topics)
    return res


def _result_payload(db: Session, sess: AssessmentSession) -> dict:
    res = db.scalar(select(AssessmentResult).where(AssessmentResult.session_id == sess.id))
    qs = {q.id: q for q in db.scalars(select(Question).where(Question.id.in_(sess.question_order)))}
    answers = {x.question_id: x for x in db.scalars(select(AssessmentAnswer).where(AssessmentAnswer.session_id == sess.id))}
    titles = dict(db.execute(select(Topic.id, Topic.title).where(Topic.id.in_([q.topic_id for q in qs.values()]))).all())
    review = []
    for i, qid in enumerate(sess.question_order):
        q, ans = qs[qid], answers.get(qid)
        review.append({"n": i + 1, "question_id": qid, "question": q.body, "your_answer": response_text(q, ans.response if ans else None), "correct_answer": answer_text(q), "correct": ans.is_correct if ans else False,
                       "needs_review": bool(ans and ans.needs_review), "explanation": q.explanation.explanation if q.explanation else "", "topic": titles.get(q.topic_id)})
    return {"session_id": str(sess.id), "score": round(res.score), "correct": res.correct_count, "total": res.total_count, "pending_review": res.pending_review_count, "final": res.is_final, "auto_submitted": sess.auto_submitted,
            "weak_topics": [{"id": t, "title": titles.get(t)} for t in res.weak_topic_ids], "submitted_at": sess.submitted_at.isoformat(), "verified_by_server": True, "review": review}


@router.post("/assessment-sessions/{sid}/submit")
def submit(sid: uuid.UUID, body: SubmitIn, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    s = ctx.student
    sess = db.scalar(select(AssessmentSession).where(AssessmentSession.id == sid).with_for_update())
    if sess is None or sess.student_id != s.id:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Sesi asesmen tidak ditemukan")
    if sess.status == "submitted":
        return _result_payload(db, sess)
    late = utcnow() > sess.deadline_at + timedelta(seconds=get_settings().assessment_grace_seconds)
    if not late:
        for x in body.answers:
            if x.question_id in sess.question_order:
                _upsert_answer(db, sess, x.question_id, x.response)
        db.flush()
    finalize(db, s, sess, auto=late, key=body.idempotency_key)
    db.commit()
    return _result_payload(db, sess)


@router.get("/assessment-sessions/{sid}/result")
def result(sid: uuid.UUID, ctx: StudentCtx = Depends(current_student), db: Session = Depends(get_db)):
    sess = _own_session(db, ctx.student, sid)
    if sess.status != "submitted":
        raise HTTPException(status.HTTP_409_CONFLICT, "Asesmen belum dikumpulkan")
    return _result_payload(db, sess)
