import hashlib
from collections import defaultdict
from datetime import timedelta

from sqlalchemy import delete, func, select
from sqlalchemy.orm import Session

from app.core.db import utcnow
from app.models import (
    Assessment, AssessmentResult, Chapter, ExerciseAttempt, Grade, Lesson, Question, ReviewItem, StudentProfile, Subject, Topic, TopicPrerequisite,
)
from app.services import learning

REVIEW_INTERVALS = [1, 3, 7]
SETTING_KEYS = {"short_sessions", "larger_text", "fewer_options", "read_aloud", "hide_mulok"}


def clean_settings(raw: dict | None) -> dict:
    raw = raw or {}
    return {k: bool(raw.get(k, False)) for k in SETTING_KEYS}


def schedule_review(db: Session, student_id, question: Question, correct: bool, mode: str) -> None:
    item = db.scalar(select(ReviewItem).where(ReviewItem.student_id == student_id, ReviewItem.question_id == question.id))
    now = utcnow()
    if mode == "review":
        if item is None:
            return
        if correct:
            item.step += 1
            item.last_correct = True
            if item.step >= len(REVIEW_INTERVALS):
                db.delete(item)
            else:
                item.due_at = now + timedelta(days=REVIEW_INTERVALS[item.step])
        else:
            item.step, item.last_correct, item.due_at = 0, False, now + timedelta(days=REVIEW_INTERVALS[0])
        return
    if correct:
        return
    if item is None:
        db.add(ReviewItem(student_id=student_id, question_id=question.id, topic_id=question.topic_id, step=0, due_at=now + timedelta(days=REVIEW_INTERVALS[0]), last_correct=False))
    else:
        item.step, item.last_correct, item.due_at = 0, False, now + timedelta(days=REVIEW_INTERVALS[0])


def due_reviews(db: Session, student_id, limit: int = 5) -> list[ReviewItem]:
    return list(db.scalars(select(ReviewItem).where(ReviewItem.student_id == student_id, ReviewItem.due_at <= utcnow()).order_by(ReviewItem.due_at).limit(limit)))


def due_count(db: Session, student_id) -> int:
    return db.scalar(select(func.count()).select_from(ReviewItem).where(ReviewItem.student_id == student_id, ReviewItem.due_at <= utcnow())) or 0


def prerequisite_map(db: Session) -> dict[int, list[int]]:
    m: dict[int, list[int]] = defaultdict(list)
    for t, p in db.execute(select(TopicPrerequisite.topic_id, TopicPrerequisite.prerequisite_topic_id)).all():
        m[t].append(p)
    return m


def allowed_topic_ids(db: Session, student: StudentProfile) -> set[int]:
    base = {t.id for t in learning.grade_topics(db, student.grade_number)}
    pm = prerequisite_map(db)
    allowed, frontier = set(base), list(base)
    for _ in range(3):
        nxt = []
        for t in frontier:
            for p in pm.get(t, []):
                if p not in allowed:
                    allowed.add(p)
                    nxt.append(p)
        frontier = nxt
    return allowed


def topic_info(db: Session, topic_ids: list[int]) -> dict[int, dict]:
    if not topic_ids:
        return {}
    rows = db.execute(
        select(Topic.id, Topic.title, Grade.number, Subject.name).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id).where(Topic.id.in_(topic_ids))
    ).all()
    return {r[0]: {"topic_id": r[0], "topic": r[1], "grade": r[2], "subject": r[3]} for r in rows}


def topic_attempt_stats(db: Session, student_id, topic_ids: list[int]) -> dict[int, list[bool]]:
    out: dict[int, list[bool]] = defaultdict(list)
    if not topic_ids:
        return out
    for tid, ok in db.execute(select(ExerciseAttempt.topic_id, ExerciseAttempt.is_correct).where(ExerciseAttempt.student_id == student_id, ExerciseAttempt.topic_id.in_(topic_ids)).order_by(ExerciseAttempt.answered_at, ExerciseAttempt.id)).all():
        out[tid].append(bool(ok))
    return out


def struggling(m: dict) -> bool:
    return m["state"] == "developing" and m["evidence_count"] >= 6 and m["recent_total"] > 0 and m["recent_correct"] / m["recent_total"] < 0.5


def foundation_suggestions(db: Session, student: StudentProfile) -> list[dict]:
    mastery = learning.mastery_for(db, student)
    pm = prerequisite_map(db)
    candidates = [(x, p) for x in mastery if struggling(x) for p in pm.get(x["topic_id"], [])]
    if not candidates:
        return []
    pids = list({p for _, p in candidates})
    info = topic_info(db, pids)
    stats = topic_attempt_stats(db, student.id, pids)
    out, seen = [], set()
    for x, p in candidates:
        if p in seen or p not in info:
            continue
        seq = stats.get(p, [])
        recent = seq[-5:]
        if len(seq) >= 3 and sum(recent) / len(recent) >= 0.8:
            continue
        seen.add(p)
        lesson = db.scalar(select(Lesson.id).where(Lesson.topic_id == p, Lesson.status == "published"))
        nq = db.scalar(select(func.count()).select_from(Question).where(Question.topic_id == p, Question.status == "published", Question.usage.in_(["practice", "both"]))) or 0
        out.append({**info[p], "for_topic": x["topic"], "for_topic_id": x["topic_id"], "lesson_id": lesson, "question_count": nq,
                    "reason": f"{x['recent_correct']} dari {x['recent_total']} jawaban terakhir di {x['topic']} benar. {info[p]['topic']} adalah dasarnya."})
    return out


def keep_options(q: Question, student: StudentProfile) -> list[int] | None:
    if not clean_settings(student.settings).get("fewer_options") or q.type != "mc" or len(q.options) < 4:
        return None
    correct = (q.answer or {}).get("index")
    wrong = [o.position for o in q.options if o.position != correct]
    if not wrong:
        return None
    h = int(hashlib.sha256(f"{student.id}:{q.id}".encode()).hexdigest(), 16)
    drop = wrong[h % len(wrong)]
    return [o.position for o in q.options if o.position != drop]


def growth(db: Session, student: StudentProfile) -> dict:
    rows = db.execute(select(ExerciseAttempt.topic_id, ExerciseAttempt.is_correct, ExerciseAttempt.answered_at, ExerciseAttempt.source).where(ExerciseAttempt.student_id == student.id).order_by(ExerciseAttempt.answered_at, ExerciseAttempt.id)).all()
    by_topic: dict[int, list[bool]] = defaultdict(list)
    days, weekly = set(), defaultdict(int)
    now = utcnow()
    reviews_ok = 0
    retry_success = 0
    last_wrong_topic: dict[int, bool] = {}
    for tid, ok, at, src in rows:
        by_topic[tid].append(bool(ok))
        local = at.astimezone(learning.WIB).date()
        days.add(local)
        wk = (now - at).days // 7
        if wk < 4:
            weekly[wk] += 1
        if src == "review" and ok:
            reviews_ok += 1
        if ok and last_wrong_topic.get(tid):
            retry_success += 1
        last_wrong_topic[tid] = not ok
    info = topic_info(db, list(by_topic))
    topics = []
    for tid, seq in by_topic.items():
        if len(seq) < 6 or tid not in info:
            continue
        first, last = seq[:5], seq[-5:]
        topics.append({"topic": info[tid]["topic"], "before_pct": round(sum(first) * 100 / len(first)), "now_pct": round(sum(last) * 100 / len(last)), "answers": len(seq)})
    streak, d = 0, now.astimezone(learning.WIB).date()
    while d in days:
        streak += 1
        d = d - timedelta(days=1)
    total = len(rows)
    badges = [
        {"key": "first", "title": "Langkah pertama", "desc": "Menjawab soal pertama", "earned": total >= 1},
        {"key": "tries", "title": "Rajin mencoba", "desc": "Menjawab 20 soal", "earned": total >= 20},
        {"key": "persist", "title": "Pantang menyerah", "desc": "Benar setelah sebelumnya salah di topik yang sama, 3 kali", "earned": retry_success >= 3},
        {"key": "review", "title": "Ingat terus", "desc": "Berhasil di 3 soal Ulang sebentar", "earned": reviews_ok >= 3},
        {"key": "streak", "title": "Rutin 3 hari", "desc": "Belajar 3 hari berturut-turut", "earned": streak >= 3},
    ]
    return {"weekly_answers": [weekly.get(i, 0) for i in (3, 2, 1, 0)], "streak_days": streak, "topics": topics, "badges": badges, "total_answers": total}


def signals(db: Session, student: StudentProfile) -> list[dict]:
    mastery = learning.mastery_for(db, student)
    out = []
    for x in mastery:
        if x["state"] != "developing" or x["evidence_count"] < 8:
            continue
        rows = db.execute(select(ExerciseAttempt.is_correct, ExerciseAttempt.answered_at).where(ExerciseAttempt.student_id == student.id, ExerciseAttempt.topic_id == x["topic_id"]).order_by(ExerciseAttempt.answered_at, ExerciseAttempt.id)).all()
        seq = [bool(r[0]) for r in rows]
        days = {r[1].astimezone(learning.WIB).date() for r in rows[-10:]}
        last, prev = seq[-5:], seq[-10:-5]
        if len(days) < 3 or not prev or sum(last) / len(last) > sum(prev) / len(prev):
            continue
        out.append({"topic_id": x["topic_id"], "topic": x["topic"], "days": len(days),
                    "message": f"Dalam {len(days)} hari belajar terakhir, hasil {student.nickname} di {x['topic']} belum naik ({sum(prev)} dari {len(prev)} lalu {sum(last)} dari {len(last)} benar).",
                    "plan": weekly_plan(db, student, x)})
    return out


def weekly_plan(db: Session, student: StudentProfile, m: dict) -> list[dict]:
    pm = prerequisite_map(db)
    pre = topic_info(db, pm.get(m["topic_id"], []))
    pre_name = next(iter(pre.values()))["topic"] if pre else None
    act = m.get("home_activity") or f"Ajak anak menjelaskan {m['topic']} dengan kata-katanya sendiri."
    short = "10 menit" if learning.band(student.grade_number) <= 2 else "15 menit"
    return [
        {"day": "Hari 1", "task": f"Baca ulang materi {m['topic']} bersama, berhenti di setiap contoh. ({short})"},
        {"day": "Hari 2", "task": act},
        {"day": "Hari 3", "task": f"Latihan 3 soal {m['topic']}. Saat salah, buka Langkah kecil bersama."},
        {"day": "Hari 4", "task": "Istirahat dari topik ini. Kerjakan Ulang sebentar saja jika ada."},
        {"day": "Hari 5", "task": f"Perkuat dasar: latihan topik {pre_name}." if pre_name else f"Pakai Alat peraga atau minta Tutor menjelaskan {m['topic']} dengan cara lain."},
        {"day": "Hari 6", "task": f"Latihan 3 soal {m['topic']} lagi, biarkan anak mengerjakan sendiri dulu."},
        {"day": "Hari 7", "task": "Lihat Kemajuanku bersama dan puji usahanya, bukan nilainya."},
    ]


def teacher_summary(db: Session, student: StudentProfile) -> str:
    mastery = learning.mastery_for(db, student)
    since = utcnow() - timedelta(days=30)
    n = db.scalar(select(func.count()).select_from(ExerciseAttempt).where(ExerciseAttempt.student_id == student.id, ExerciseAttempt.answered_at >= since)) or 0
    ok = db.scalar(select(func.count()).select_from(ExerciseAttempt).where(ExerciseAttempt.student_id == student.id, ExerciseAttempt.answered_at >= since, ExerciseAttempt.is_correct.is_(True))) or 0
    exams = db.execute(select(AssessmentResult, Assessment.title).join(Assessment, Assessment.id == AssessmentResult.assessment_id).where(AssessmentResult.student_id == student.id).order_by(AssessmentResult.created_at.desc()).limit(3)).all()
    lines = [
        f"Ringkasan belajar {student.nickname} (Kelas {student.grade_number}) dari aplikasi BOBO BELAJAR",
        f"Periode: 30 hari terakhir, dibuat {utcnow().astimezone(learning.WIB).strftime('%d-%m-%Y')}",
        "",
        f"Soal dikerjakan: {n} ({ok} benar)" if n else "Soal dikerjakan: belum ada dalam 30 hari terakhir",
        "",
        "Status per topik (berdasarkan 5 jawaban terakhir, minimal 3 jawaban):",
    ]
    for x in mastery:
        lines.append(f"- {x['topic']}: {x['label']} ({x['evidence']})")
    if exams:
        lines += ["", "Asesmen terakhir:"]
        for r, t in exams:
            lines.append(f"- {t}: nilai {round(r.score)}{'' if r.is_final else ' (menunggu penilaian esai)'}")
    sig = signals(db, student)
    if sig:
        lines += ["", "Perlu perhatian:"] + [f"- {s['message']}" for s in sig]
    lines += ["", "Catatan: ringkasan ini dibuat otomatis dari aktivitas di aplikasi, bukan penilaian resmi sekolah dan bukan diagnosis."]
    return "\n".join(lines)


def purge_old_conversations(db: Session, days: int = 30) -> int:
    from app.models import AIConversation, AIMessage
    cutoff = utcnow() - timedelta(days=days)
    n = db.execute(delete(AIMessage).where(AIMessage.created_at < cutoff)).rowcount or 0
    empty = select(AIConversation.id).where(~select(AIMessage.id).where(AIMessage.conversation_id == AIConversation.id).exists(), AIConversation.created_at < cutoff)
    db.execute(delete(AIConversation).where(AIConversation.id.in_(empty)))
    db.commit()
    return n
