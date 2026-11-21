import uuid
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.db import utcnow
from app.models import (
    Chapter, CurriculumVersion, ExerciseAttempt, Grade, LearningRecommendation, LearningSession, Lesson, LessonProgress,
    MasteryRecord, Question, StudentProfile, Subject, Topic,
)

MIN_EVIDENCE = 3
WINDOW = 5
GOOD_RATIO = 0.8

STATE_LABELS = {
    "not_started": "Belum mulai",
    "insufficient": "Bukti belum cukup",
    "developing": "Berkembang",
    "demonstrated": "Menunjukkan pemahaman",
}

WIB = timezone(timedelta(hours=7))


def band(grade: int) -> int:
    return 1 if grade <= 2 else 2 if grade <= 4 else 3 if grade <= 6 else 4


def phase(grade: int) -> str:
    return {1: "Fase A", 2: "Fase B", 3: "Fase C", 4: "Fase D"}[band(grade)]


def level(grade: int) -> str:
    return "SD" if grade <= 6 else "SMP"


def active_version(db: Session) -> CurriculumVersion | None:
    return db.scalar(select(CurriculumVersion).where(CurriculumVersion.is_active.is_(True)).order_by(CurriculumVersion.id.desc()))


def grade_topics(db: Session, grade_number: int) -> list[Topic]:
    v = active_version(db)
    if v is None:
        return []
    return list(db.scalars(
        select(Topic).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id)
        .where(Subject.curriculum_version_id == v.id, Grade.number == grade_number, Subject.is_enabled.is_(True))
        .order_by(Subject.sort_order, Chapter.number, Topic.sort_order, Topic.id)
    ))


def topics_with_evidence_or_content(db: Session, grade_number: int) -> list[Topic]:
    topics = grade_topics(db, grade_number)
    if not topics:
        return []
    ids = [t.id for t in topics]
    with_q = set(db.scalars(select(Question.topic_id).where(Question.topic_id.in_(ids), Question.status == "published")))
    with_l = set(db.scalars(select(Lesson.topic_id).where(Lesson.topic_id.in_(ids), Lesson.status == "published")))
    chapters_with_content = {t.chapter_id for t in topics if t.id in with_q or t.id in with_l}
    return [t for t in topics if t.chapter_id in chapters_with_content]


def mastery_for(db: Session, student: StudentProfile, topics: list[Topic] | None = None) -> list[dict]:
    topics = topics if topics is not None else topics_with_evidence_or_content(db, student.grade_number)
    if not topics:
        return []
    ids = [t.id for t in topics]
    rows = db.execute(
        select(ExerciseAttempt.topic_id, ExerciseAttempt.is_correct, ExerciseAttempt.answered_at)
        .where(ExerciseAttempt.student_id == student.id, ExerciseAttempt.topic_id.in_(ids))
        .order_by(ExerciseAttempt.answered_at, ExerciseAttempt.id)
    ).all()
    by_topic: dict[int, list[bool]] = defaultdict(list)
    for tid, ok, _ in rows:
        by_topic[tid].append(bool(ok))
    out = []
    for t in topics:
        seq = by_topic.get(t.id, [])
        recent = seq[-WINDOW:]
        rc = sum(recent)
        if not seq:
            st = "not_started"
        elif len(seq) < MIN_EVIDENCE:
            st = "insufficient"
        elif rc / len(recent) >= GOOD_RATIO:
            st = "demonstrated"
        else:
            st = "developing"
        evidence = "Belum ada jawaban" if not seq else f"{rc} dari {len(recent)} jawaban terakhir benar" + (f" · butuh minimal {MIN_EVIDENCE}" if st == "insufficient" else "")
        out.append({
            "topic_id": t.id, "topic": t.title, "state": st, "label": STATE_LABELS[st], "evidence_count": len(seq),
            "recent_correct": rc, "recent_total": len(recent), "recent": recent, "evidence": evidence,
            "home_activity": t.home_activity, "common_mistake": t.common_mistake,
        })
    return out


def refresh_mastery(db: Session, student: StudentProfile, topic_ids: set[int]) -> None:
    if not topic_ids:
        return
    topics = list(db.scalars(select(Topic).where(Topic.id.in_(topic_ids))))
    for m in mastery_for(db, student, topics):
        rec = db.scalar(select(MasteryRecord).where(MasteryRecord.student_id == student.id, MasteryRecord.topic_id == m["topic_id"]))
        if rec is None:
            rec = MasteryRecord(student_id=student.id, topic_id=m["topic_id"], state=m["state"], evidence_count=0, recent_correct=0, recent_total=0)
            db.add(rec)
        rec.state, rec.evidence_count, rec.recent_correct, rec.recent_total = m["state"], m["evidence_count"], m["recent_correct"], m["recent_total"]
    refresh_recommendations(db, student)


def refresh_recommendations(db: Session, student: StudentProfile) -> None:
    m = mastery_for(db, student)
    young = band(student.grade_number) <= 2
    dur = "10 menit" if young else "10–15 menit"
    wanted: dict[str, dict] = {}
    for x in m:
        act = x["home_activity"] or "Buka materi topik ini bersama anak dan minta ia menjelaskan kembali dengan kata-katanya sendiri."
        if x["state"] == "developing":
            wanted[f"dev:{x['topic_id']}"] = dict(kind="practice", topic_id=x["topic_id"], title=f"Latih lagi {x['topic']} di rumah", evidence=f"{x['recent_correct']} dari {x['recent_total']} jawaban terakhir benar di {x['topic']}.", activity=act, duration_label=dur)
        elif x["state"] == "insufficient":
            need = MIN_EVIDENCE - x["evidence_count"]
            wanted[f"ins:{x['topic_id']}"] = dict(kind="evidence", topic_id=x["topic_id"], title=f"Ajak {student.nickname} mengerjakan {need} soal {x['topic']} lagi", evidence=f"Baru {x['evidence_count']} jawaban, belum cukup untuk menilai.", activity="Buka menu Latihan bersama, pilih topik ini, lalu minta anak menjelaskan caranya dengan kata-katanya sendiri.", duration_label="5–10 menit")
        elif x["state"] == "demonstrated":
            wanted[f"good:{x['topic_id']}"] = dict(kind="maintain", topic_id=x["topic_id"], title=f"Apresiasi usaha {student.nickname} di {x['topic']}", evidence=f"{x['recent_correct']} dari {x['recent_total']} jawaban terakhir benar.", activity="Puji prosesnya (\"kamu teliti menghitungnya\"), bukan kecerdasannya. Sesekali ajak mengulang satu soal agar tetap ingat.", duration_label="2 menit")
    from app.services import support
    for f in support.foundation_suggestions(db, student):
        grade_note = f" dari Kelas {f['grade']}" if f["grade"] != student.grade_number else ""
        wanted[f"found:{f['topic_id']}"] = dict(kind="foundation", topic_id=f["topic_id"], title=f"Perkuat pondasi: {f['topic']}{grade_note}", evidence=f["reason"], activity=f"Sebelum lanjut {f['for_topic']}, ajak anak membuka jalur Pondasi di menu Home: baca materi {f['topic']} lalu kerjakan 3 soal. Dasar yang kuat membuat topik berikutnya lebih mudah.", duration_label=dur)
    nxt = next((x for x in m if x["state"] == "not_started"), None)
    if nxt:
        wanted[f"next:{nxt['topic_id']}"] = dict(kind="next", topic_id=nxt["topic_id"], title=f"Mulai topik {nxt['topic']}", evidence="Belum ada aktivitas di topik ini.", activity=nxt["home_activity"] or "Mulai dari materi topik ini di menu Belajar.", duration_label=dur)
    existing = {r.key: r for r in db.scalars(select(LearningRecommendation).where(LearningRecommendation.student_id == student.id))}
    for key, data in wanted.items():
        x = next((y for y in m if y["topic_id"] == data["topic_id"]), None)
        evidence_data = {"recent_correct": x["recent_correct"], "recent_total": x["recent_total"], "evidence_count": x["evidence_count"], "state": x["state"]} if x else {}
        r = existing.get(key)
        if r is None:
            db.add(LearningRecommendation(student_id=student.id, key=key, evidence_data=evidence_data, active=True, **data))
        else:
            for k, v in data.items():
                setattr(r, k, v)
            if r.evidence_data != evidence_data:
                r.done_at = None
            r.evidence_data = evidence_data
            r.active = True
    for key, r in existing.items():
        if key not in wanted:
            r.active = False


KIND_ORDER = {"practice": 0, "foundation": 1, "evidence": 2, "next": 3, "maintain": 4}
KIND_LABEL = {"practice": "Latih lagi", "foundation": "Perkuat pondasi", "evidence": "Kumpulkan bukti", "next": "Topik berikutnya", "maintain": "Pertahankan"}


def active_recommendations(db: Session, student: StudentProfile) -> list[LearningRecommendation]:
    rows = list(db.scalars(select(LearningRecommendation).where(LearningRecommendation.student_id == student.id, LearningRecommendation.active.is_(True))))
    return sorted(rows, key=lambda r: (KIND_ORDER.get(r.kind, 9), r.id))


def log_activity(db: Session, student_id: uuid.UUID, kind: str, summary: str, topic_id: int | None = None, when: datetime | None = None) -> None:
    db.add(LearningSession(student_id=student_id, kind=kind, summary=summary[:200], topic_id=topic_id, occurred_at=when or utcnow()))


def today_bounds() -> tuple[datetime, datetime]:
    now = utcnow().astimezone(WIB)
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    return start.astimezone(timezone.utc), (start + timedelta(days=1)).astimezone(timezone.utc)


def today_targets(db: Session, student: StudentProfile, tutor_today: int) -> list[dict]:
    a, b = today_bounds()
    goal = 3 if band(student.grade_number) <= 2 else 5
    n_att = db.scalar(select(func.count()).select_from(ExerciseAttempt).where(ExerciseAttempt.student_id == student.id, ExerciseAttempt.answered_at >= a, ExerciseAttempt.answered_at < b)) or 0
    n_les = db.scalar(select(func.count()).select_from(LessonProgress).where(LessonProgress.student_id == student.id, LessonProgress.completed_at >= a, LessonProgress.completed_at < b)) or 0
    return [
        {"key": "lesson", "label": "Selesaikan 1 materi", "done": n_les >= 1, "progress": f"{min(n_les, 1)}/1"},
        {"key": "practice", "label": f"Kerjakan {goal} soal", "done": n_att >= goal, "progress": f"{min(n_att, goal)}/{goal}"},
        {"key": "tutor", "label": "Tanya Tutor 1 kali", "done": tutor_today >= 1, "progress": f"{min(tutor_today, 1)}/1"},
    ]


def relative_label(when: datetime) -> str:
    local = when.astimezone(WIB)
    today = utcnow().astimezone(WIB).date()
    d = (today - local.date()).days
    if d <= 0:
        return "Hari ini"
    if d == 1:
        return "Kemarin"
    if d < 7:
        return f"{d} hari lalu"
    bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
    return f"{local.day} {bulan[local.month - 1]}"
