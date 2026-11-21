from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.db import utcnow
from app.models import (
    Assessment, AssessmentQuestion, AssessmentTemplate, Chapter, Grade, Lesson, Question, Subject, Topic, TopicPrerequisite,
)
from app.services import learning

BUNDLE_FORMAT = 1


def _content_ok(status: str, is_sample: bool, include_sample: bool) -> bool:
    return status == "published" or (include_sample and is_sample)


def build_bundle(db: Session, include_sample: bool = False) -> dict:
    v = learning.active_version(db)
    out = {
        "format": BUNDLE_FORMAT, "generated_at": utcnow().isoformat(), "curriculum": f"{v.name} {v.version}" if v else None,
        "includes_sample": include_sample, "subjects": [], "chapters": [], "topics": [], "prerequisites": [], "lessons": [], "questions": [],
        "assessment_templates": [t.label for t in db.scalars(select(AssessmentTemplate).order_by(AssessmentTemplate.id))], "assessments": [],
    }
    if v is None:
        return out
    subjects = db.execute(
        select(Subject, Grade.number).join(Grade, Grade.id == Subject.grade_id)
        .where(Subject.curriculum_version_id == v.id, Subject.is_enabled.is_(True)).order_by(Grade.number, Subject.sort_order, Subject.id)
    ).all()
    subject_ids = [s.id for s, _ in subjects]
    for s, g in subjects:
        out["subjects"].append({"id": s.id, "grade": g, "name": s.name, "short_label": s.short_label, "sort_order": s.sort_order})
    chapters = list(db.scalars(select(Chapter).where(Chapter.subject_id.in_(subject_ids or [-1])).order_by(Chapter.subject_id, Chapter.number)))
    for c in chapters:
        out["chapters"].append({"id": c.id, "subject_id": c.subject_id, "number": c.number, "title": c.title})
    topics = list(db.scalars(select(Topic).where(Topic.chapter_id.in_([c.id for c in chapters] or [-1])).order_by(Topic.chapter_id, Topic.sort_order, Topic.id)))
    topic_ids = {t.id for t in topics}
    for t in topics:
        out["topics"].append({"id": t.id, "chapter_id": t.chapter_id, "title": t.title, "sort_order": t.sort_order, "home_activity": t.home_activity, "common_mistake": t.common_mistake})
    for a, b in db.execute(select(TopicPrerequisite.topic_id, TopicPrerequisite.prerequisite_topic_id)).all():
        if a in topic_ids and b in topic_ids:
            out["prerequisites"].append([a, b])
    for l in db.scalars(select(Lesson).where(Lesson.topic_id.in_(topic_ids or {-1})).order_by(Lesson.topic_id, Lesson.id)):
        if not _content_ok(l.status, l.is_sample, include_sample):
            continue
        out["lessons"].append({
            "id": l.id, "topic_id": l.topic_id, "title": l.title, "minutes": l.minutes, "version": l.version, "sample": l.is_sample,
            "blocks": [{"kind": b.kind, "text": b.text, "points": b.points, "visual": b.visual} for b in l.blocks],
        })
    kept_questions: set[int] = set()
    for q in db.scalars(select(Question).where(Question.topic_id.in_(topic_ids or {-1})).order_by(Question.topic_id, Question.id)):
        if q.type == "essay" or not _content_ok(q.status, q.is_sample, include_sample):
            continue
        kept_questions.add(q.id)
        out["questions"].append({
            "id": q.id, "topic_id": q.topic_id, "type": q.type, "body": q.body, "difficulty": q.difficulty, "usage": q.usage, "sample": q.is_sample,
            "options": [{"index": o.position, "label": o.label, "side": o.side} for o in sorted(q.options, key=lambda o: o.position)],
            "answer": q.answer, "explanation": q.explanation.explanation if q.explanation else "", "mistake_hint": q.explanation.mistake_hint if q.explanation else None,
            "scaffold": q.scaffold,
        })
    labels = {t.id: t.label for t in db.scalars(select(AssessmentTemplate))}
    for a in db.scalars(select(Assessment).where(Assessment.subject_id.in_(subject_ids or [-1])).order_by(Assessment.id)):
        if not _content_ok(a.status, a.is_sample, include_sample):
            continue
        links = [x for x in db.scalars(select(AssessmentQuestion).where(AssessmentQuestion.assessment_id == a.id).order_by(AssessmentQuestion.position)) if x.question_id in kept_questions]
        if not links:
            continue
        out["assessments"].append({
            "id": a.id, "template": labels.get(a.template_id, "Asesmen"), "title": a.title, "short_title": a.short_title, "grade": a.grade_number,
            "duration_minutes": a.duration_minutes, "shuffle_questions": a.shuffle_questions, "shuffle_options": a.shuffle_options, "passing_score": a.passing_score,
            "sample": a.is_sample, "questions": [{"id": x.question_id, "points": x.points} for x in links],
        })
    return out
