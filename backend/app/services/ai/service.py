import hashlib
import threading
import time
import uuid

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models import (
    AIConversation, AIMessage, Lesson, LessonBlock, AIPromptVersion, AISafetyEvent, AIUsageLog, AssessmentResult, Assessment, ParentProfile, StudentProfile,
)
from app.services import learning
from app.services.ai import retrieval, safety
from app.services.ai.providers import GenRequest, GroundedProvider, build_provider
from app.services.entitlements import parent_assistant_limit, tutor_limit

TUTOR_PROMPT = (
    "Kamu adalah Tutor BOBO untuk siswa {level} kelas {grade} di Indonesia. Jawab dalam Bahasa Indonesia yang {style}. "
    "Gunakan hanya MATERI RUJUKAN yang diberikan. Jika materi tidak memuat jawabannya, katakan bahwa materi itu belum tersedia dan sarankan bertanya ke guru atau orang tua. "
    "Utamakan pemahaman: jangan langsung memberi jawaban akhir soal PR atau ujian, berikan petunjuk langkah demi langkah dan ajak siswa mencoba. "
    "Jangan meminta, menyebut, atau menyimpan data pribadi. Jangan membahas topik dewasa, kekerasan, atau hal berbahaya. "
    "Jangan mengaku sebagai manusia. Maksimal {max_sentences} kalimat."
)

PARENT_PROMPT = (
    "Kamu adalah asisten BOBO untuk orang tua siswa {level} kelas {grade} di Indonesia. Jawab dalam Bahasa Indonesia yang sopan, jelas, dan praktis. "
    "Gunakan DATA BELAJAR anak dan MATERI RUJUKAN yang diberikan. Sebutkan dasar datanya. Jika data tidak cukup, katakan dengan jelas. "
    "Jangan pernah mendiagnosis gangguan belajar, kondisi psikologis, atau medis, dan jangan memberi label negatif pada anak. "
    "Berikan saran kegiatan di rumah yang konkret dan singkat. Maksimal 8 kalimat."
)

STYLE_HINT = {
    "story": "Jelaskan lewat cerita pendek dari kehidupan sehari-hari anak Indonesia.",
    "visual": "Jelaskan dengan gambaran visual yang mudah dibayangkan; aplikasi akan menampilkan alat peraga di bawah jawabanmu.",
    "steps": "Jelaskan dalam langkah bernomor yang pendek, satu ide per langkah.",
}


def visual_for(db: Session, topic_id: int | None, topic_title: str | None) -> str | None:
    if topic_id is not None:
        v = db.scalar(select(LessonBlock.visual).join(Lesson, Lesson.id == LessonBlock.lesson_id).where(Lesson.topic_id == topic_id, Lesson.status == "published", LessonBlock.visual.is_not(None)))
        if v:
            return v
    t = (topic_title or "").lower()
    if "pecahan" in t:
        return "frac"
    if "pythagoras" in t or "segitiga" in t or "jarak" in t:
        return "tri"
    if "jumlah" in t or "kurang" in t or "cerita" in t:
        return "tens"
    return None


STYLE = {1: "sangat sederhana, kalimat pendek, dengan contoh benda sehari-hari", 2: "sederhana dengan contoh konkret", 3: "jelas dengan penalaran langkah demi langkah", 4: "runtut dan logis seperti untuk siswa SMP"}
MAX_SENT = {1: 3, 2: 4, 3: 5, 4: 6}

_cache: dict[str, tuple[float, str, list]] = {}
_cache_lock = threading.Lock()
CACHE_TTL = 3600


def _cache_get(key: str):
    with _cache_lock:
        v = _cache.get(key)
        if v and time.time() - v[0] < CACHE_TTL:
            return v[1], v[2]
        if v:
            _cache.pop(key, None)
    return None


def _cache_put(key: str, text: str, sources: list) -> None:
    with _cache_lock:
        if len(_cache) > 2000:
            _cache.clear()
        _cache[key] = (time.time(), text, sources)


def clear_cache() -> None:
    with _cache_lock:
        _cache.clear()


def _prompt(db: Session, purpose: str, fallback: str) -> tuple[str, int | None]:
    row = db.scalar(select(AIPromptVersion).where(AIPromptVersion.purpose == purpose, AIPromptVersion.is_active.is_(True)).order_by(AIPromptVersion.version.desc()))
    return (row.template, row.version) if row else (fallback, None)


def _used_today(db: Session, purpose: str, student_id=None, parent_id=None) -> int:
    a, b = learning.today_bounds()
    q = select(func.count()).select_from(AIUsageLog).where(AIUsageLog.purpose == purpose, AIUsageLog.created_at >= a, AIUsageLog.created_at < b)
    if student_id is not None:
        q = q.where(AIUsageLog.student_id == student_id)
    if parent_id is not None:
        q = q.where(AIUsageLog.parent_id == parent_id)
    return db.scalar(q) or 0


def _spent_today(db: Session) -> float:
    a, b = learning.today_bounds()
    return float(db.scalar(select(func.coalesce(func.sum(AIUsageLog.cost_usd), 0.0)).where(AIUsageLog.created_at >= a, AIUsageLog.created_at < b)) or 0.0)


def _conversation(db: Session, conv_id: uuid.UUID | None, purpose: str, student: StudentProfile, parent: ParentProfile | None) -> AIConversation:
    if conv_id:
        c = db.get(AIConversation, conv_id)
        if c and c.student_id == student.id and c.purpose == purpose and (parent is None or c.parent_id == parent.id):
            return c
    c = AIConversation(purpose=purpose, student_id=student.id, parent_id=parent.id if parent else None)
    db.add(c)
    db.flush()
    return c


def _run_provider(db: Session, req: GenRequest):
    s = get_settings()
    kind, model = s.ai_provider, s.ai_model
    if kind != "grounded" and _spent_today(db) >= s.ai_global_daily_cost_limit_usd:
        kind, model = "grounded", "grounded-v1"
    t0 = time.monotonic()
    outcome = "ok"
    try:
        res = build_provider(kind, model).generate(req)
        if not res.text.strip():
            raise RuntimeError("empty response")
    except Exception:
        res = GroundedProvider().generate(req)
        outcome = "fallback"
    latency = int((time.monotonic() - t0) * 1000)
    cost = (res.input_tokens * s.ai_price_input_per_mtok + res.output_tokens * s.ai_price_output_per_mtok) / 1_000_000 if res.provider != "grounded" else 0.0
    return res, outcome, latency, cost


def tutor_reply(db: Session, student: StudentProfile, parent: ParentProfile, text: str, conv_id: uuid.UUID | None, topic_id: int | None, style: str | None = None) -> dict:
    s = get_settings()
    limit = tutor_limit(db, parent, student)
    used = _used_today(db, "tutor", student_id=student.id)
    if used >= limit:
        raise HTTPException(status.HTTP_429_TOO_MANY_REQUESTS, "Kuota Tutor hari ini sudah habis")
    conv = _conversation(db, conv_id, "tutor", student, None)
    db.add(AIMessage(conversation_id=conv.id, role="user", content=text))
    verdict = safety.check_child_input(text)
    b = learning.band(student.grade_number)
    topics = learning.topics_with_evidence_or_content(db, student.grade_number)
    scope = ", ".join(t.title for t in topics[:3]) or "materi kelasmu"
    sources: list[str] = []
    visual = None
    provider, model, outcome, latency, cost, tin, tout, cached, pv = "safety", "rules", "refused", 0, 0.0, 0, 0, False, None
    if verdict.action != "allow":
        db.add(AISafetyEvent(student_id=student.id, purpose="tutor", category=verdict.category, stage="input", action=verdict.action))
        reply, flagged = verdict.reply, True
        outcome = "guided" if verdict.action == "guide" else "refused"
        learning.log_activity(db, student.id, "tutor", "Tutor menolak permintaan yang tidak aman" if outcome == "refused" else "Tutor memandu langkah, bukan memberi jawaban langsung")
    else:
        key = hashlib.sha256(f"tutor|{student.grade_number}|{topic_id}|{style}|{s.ai_provider}|{s.ai_model}|{' '.join(text.lower().split())}".encode()).hexdigest()
        hit = _cache_get(key)
        passages = retrieval.search(db, text, student.grade_number, topic_id)
        if hit:
            reply, sources = hit
            provider, model, outcome, cached = s.ai_provider, s.ai_model, "ok", True
        else:
            tpl, pv = _prompt(db, "tutor", TUTOR_PROMPT)
            system = tpl.format(level=learning.level(student.grade_number), grade=student.grade_number, style=STYLE[b], max_sentences=MAX_SENT[b])
            if style:
                system += " " + STYLE_HINT[style]
            req = GenRequest("tutor", system, text, passages, student.grade_number, s.ai_max_output_tokens, {"scope": scope, "style": style})
            res, outcome, latency, cost = _run_provider(db, req)
            provider, model, tin, tout = res.provider, res.model, res.input_tokens, res.output_tokens
            reply, flagged = safety.clean_output(res.text, 900 if b <= 2 else 1400)
            if flagged:
                db.add(AISafetyEvent(student_id=student.id, purpose="tutor", category="output_filtered", stage="output", action="sanitized"))
            sources = list(dict.fromkeys(f"{'Materi' if p.source_type == 'lesson' else 'Bank soal'}: {p.topic or p.title}" for p in passages[:2]))
            if passages:
                _cache_put(key, reply, sources)
        topic_name = passages[0].topic if passages and passages[0].topic else None
        if passages:
            visual = visual_for(db, passages[0].topic_id, topic_name)
        learning.log_activity(db, student.id, "tutor", f"Bertanya ke Tutor ({topic_name or 'umum'})", passages[0].topic_id if passages else None)
        flagged = False
    db.add(AIMessage(conversation_id=conv.id, role="assistant", content=reply, sources=sources, flagged=verdict.action != "allow"))
    db.add(AIUsageLog(purpose="tutor", student_id=student.id, parent_id=parent.id, provider=provider, model=model, prompt_version=pv, input_tokens=tin, output_tokens=tout, cost_usd=cost, latency_ms=latency, outcome=outcome, cached=cached))
    db.commit()
    return {"conversation_id": str(conv.id), "reply": reply, "sources": sources, "refused": verdict.action == "refuse", "category": verdict.category, "quota_limit": limit, "quota_left": max(0, limit - used - 1),
            "visual": visual if style == "visual" else None, "visual_available": visual is not None, "can_restyle": bool(sources)}


def parent_context(db: Session, child: StudentProfile) -> dict:
    m = learning.mastery_for(db, child)
    recs = learning.active_recommendations(db, child)
    last = db.execute(
        select(AssessmentResult, Assessment.short_title).join(Assessment, Assessment.id == AssessmentResult.assessment_id)
        .where(AssessmentResult.student_id == child.id).order_by(AssessmentResult.created_at.desc()).limit(1)
    ).first()
    attempts = sum(x["evidence_count"] for x in m)
    exams = db.scalar(select(func.count()).select_from(AssessmentResult).where(AssessmentResult.student_id == child.id)) or 0
    weak_titles = []
    if last:
        tmap = {x["topic_id"]: x["topic"] for x in m}
        weak_titles = [tmap.get(t, "") for t in last[0].weak_topic_ids if tmap.get(t)]
    basis = f"Berdasarkan {attempts} jawaban" + (f" dan {exams} asesmen" if exams else "") + f" {child.nickname}"
    return {"mastery": m, "recs": recs, "last": last, "weak": weak_titles, "basis": basis}


def grounded_parent_answer(text: str, child: StudentProfile, ctx: dict) -> str:
    t = text.lower()
    m, name, b = ctx["mastery"], child.nickname, learning.band(child.grade_number)
    if any(k in t for k in ("rutin", "jadwal", "kebiasaan", "berapa lama", "waktu belajar", "sehat")):
        return {
            1: "Untuk anak kelas 1–2, sesi singkat 10–15 menit biasanya lebih efektif daripada satu sesi panjang. Pilih jam yang sama setiap hari, temani di awal, dan tutup dengan pujian atas usahanya.",
            2: "Untuk anak kelas 3–4, coba 15–25 menit per sesi dengan jeda singkat. Biarkan anak memilih urutan mata pelajaran agar merasa punya kendali.",
            3: "Untuk anak kelas 5–6, 20–30 menit per sesi dengan jeda 5 menit biasanya cukup. Ajak anak mencentang target hariannya sendiri di aplikasi.",
            4: "Untuk siswa SMP, 30–45 menit per sesi dengan jeda 5–10 menit. Libatkan anak menyusun jadwalnya sendiri dan jauhkan ponsel dari notifikasi lain saat belajar.",
        }[b] + "\n\nIni panduan umum. Sesuaikan dengan kondisi dan kegiatan anak."
    if not m:
        return f"Belum ada materi atau data belajar untuk Kelas {child.grade_number}, jadi saya belum bisa menganalisis perkembangan {name}."
    dev = [x for x in m if x["state"] == "developing"]
    ins = [x for x in m if x["state"] == "insufficient"]
    none = [x for x in m if x["state"] == "not_started"]
    if any(k in t for k in ("kesulitan", "kenapa", "mengapa", "susah", "sulit")):
        if not dev:
            if ins:
                return f"Saat ini belum terlihat topik yang sulit. Untuk {ins[0]['topic']}, {name} baru menjawab {ins[0]['evidence_count']} soal, jadi belum cukup untuk menyimpulkan apa pun. Ajak {name} mengerjakan beberapa soal lagi agar gambarannya lebih jelas."
            return f"Dari data yang ada, belum terlihat topik yang sulit untuk {name}."
        x = dev[0]
        mistake = f" Kesalahan yang umum di topik ini adalah {x['common_mistake']}." if x["common_mistake"] else ""
        act = x["home_activity"] or "Buka materinya bersama dan minta anak menjelaskan kembali."
        return f"Di {x['topic']}, {name} menjawab benar {x['recent_correct']} dari {x['recent_total']} soal terakhir, jadi topik ini masih berkembang.{mistake} Ini wajar saat anak baru mempelajarinya dan tidak menggambarkan kemampuan {name} secara umum.\n\nYang bisa dicoba di rumah: {act}"
    if any(k in t for k in ("jelaskan", "menjelaskan", "cara", "ajarkan", "mengajar")):
        x = (dev or ins or m)[0]
        act = x["home_activity"] or "Buka materi topik ini bersama anak."
        return f"Cara menjelaskan {x['topic']} di rumah:\n\n{act}\n\nMinta {name} menjelaskan kembali dengan kata-katanya sendiri. Jika ia bisa \"mengajari\" Anda, itu tanda pemahamannya mulai kuat."
    if any(k in t for k in ("selanjutnya", "berikutnya", "belajar apa")):
        lines = []
        if dev:
            lines.append(f"Perkuat {', '.join(x['topic'] for x in dev)}, karena hasilnya masih naik-turun.")
        if ins:
            lines.append(f"Tambah 3–5 soal di {', '.join(x['topic'] for x in ins)} agar BOBO bisa menilai.")
        if none:
            lines.append(f"Setelah itu, mulai topik {none[0]['topic']}.")
        if not lines:
            lines.append("Semua topik yang tersedia sudah baik. Lanjutkan ke bab berikutnya setelah materinya tersedia.")
        return f"Saran urutan untuk {name}:\n" + "\n".join(f"{i + 1}. {l}" for i, l in enumerate(lines))
    if any(k in t for k in ("ujian", "asesmen", "persiapan", "tes", "try out", "menyiapkan")):
        last = ctx["last"]
        weak = ctx["weak"] or [x["topic"] for x in dev]
        head = f"Fokuskan persiapan ke {' dan '.join(weak)}" + (f", topik yang belum tepat di asesmen terakhir (nilai {round(last[0].score)})" if last and ctx["weak"] else "") + "." if weak else "Belum ada topik lemah yang tercatat."
        return f"{head} Ajak {name} mengerjakan 5 soal latihan per topik selama 2–3 hari, lalu coba asesmen di menu Ujian. Hindari belajar maraton semalam sebelum ujian."
    return f"Saya bisa membantu soal perkembangan belajar {name}, cara menjelaskan materi di rumah, persiapan asesmen, dan rutinitas belajar. Coba pilih salah satu pertanyaan yang tersedia."


def parent_reply(db: Session, parent: ParentProfile, child: StudentProfile, text: str, conv_id: uuid.UUID | None) -> dict:
    s = get_settings()
    limit = parent_assistant_limit(db, parent)
    used = _used_today(db, "parent", parent_id=parent.id)
    if used >= limit:
        raise HTTPException(status.HTTP_429_TOO_MANY_REQUESTS, "Kuota Tanya BOBO hari ini sudah habis")
    conv = _conversation(db, conv_id, "parent", child, parent)
    db.add(AIMessage(conversation_id=conv.id, role="user", content=text))
    verdict = safety.check_parent_input(text, child.nickname)
    provider, model, outcome, latency, cost, tin, tout, pv = "safety", "rules", "redirected", 0, 0.0, 0, 0, None
    if verdict.action != "allow":
        db.add(AISafetyEvent(student_id=child.id, purpose="parent", category=verdict.category, stage="input", action=verdict.action))
        reply, basis = verdict.reply, "Panduan keamanan · bukan diagnosis"
    else:
        ctx = parent_context(db, child)
        basis = ctx["basis"]
        data_lines = [f"- {x['topic']}: {x['label']} ({x['evidence']})" for x in ctx["mastery"]]
        if ctx["last"]:
            data_lines.append(f"- Asesmen terakhir {ctx['last'][1]}: nilai {round(ctx['last'][0].score)}; perlu dilatih: {', '.join(ctx['weak']) or '-'}")
        tpl, pv = _prompt(db, "parent", PARENT_PROMPT)
        system = tpl.format(level=learning.level(child.grade_number), grade=child.grade_number) + "\n\nDATA BELAJAR " + child.nickname + ":\n" + ("\n".join(data_lines) or "- belum ada data")
        passages = retrieval.search(db, text, child.grade_number, None, limit=2)
        req = GenRequest("parent", system, text, passages, child.grade_number, s.ai_max_output_tokens, {"grounded_answer": grounded_parent_answer(text, child, ctx)})
        res, outcome, latency, cost = _run_provider(db, req)
        provider, model, tin, tout = res.provider, res.model, res.input_tokens, res.output_tokens
        reply, flagged = safety.clean_output(res.text, 1800)
    db.add(AIMessage(conversation_id=conv.id, role="assistant", content=reply, sources=[basis]))
    db.add(AIUsageLog(purpose="parent", student_id=child.id, parent_id=parent.id, provider=provider, model=model, prompt_version=pv, input_tokens=tin, output_tokens=tout, cost_usd=cost, latency_ms=latency, outcome=outcome))
    db.commit()
    return {"conversation_id": str(conv.id), "reply": reply, "basis": basis, "quota_limit": limit, "quota_left": max(0, limit - used - 1)}


def tutor_quota(db: Session, student: StudentProfile, parent: ParentProfile) -> dict:
    limit = tutor_limit(db, parent, student)
    used = _used_today(db, "tutor", student_id=student.id)
    return {"limit": limit, "used": used, "left": max(0, limit - used)}
