from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.db import utcnow
from app.models import (
    AIModel, AIPromptVersion, AIProvider, Assessment, AssessmentQuestion, AssessmentTemplate, Chapter, CurriculumSource, CurriculumVersion,
    EducationLevel, Grade, Lesson, TopicPrerequisite, LessonBlock, Question, QuestionExplanation, QuestionOption, QuestionSource, Subject, SubscriptionEntitlement, Topic,
)
from app.seed.sample_content import EXTRA_SUBJECTS, PREREQUISITES, SAMPLE, SCAFFOLDS, SUBJECTS
from app.services.ai import retrieval
from app.services.ai.service import PARENT_PROMPT, TUTOR_PROMPT
from app.services.learning import band

TEMPLATES = [
    ("ASLM", "Asesmen Sumatif Lingkup Materi", "Asesmen di akhir satu lingkup materi atau bab."),
    ("ASAS", "Asesmen Sumatif Akhir Semester (ASAS)", "Asesmen di akhir semester."),
    ("ASAT", "Asesmen Sumatif Akhir Tahun (ASAT)", "Asesmen di akhir tahun ajaran."),
    ("TRYOUT", "Try Out", "Simulasi ujian dengan waktu terbatas."),
    ("PRACTICE", "Latihan Ujian", "Latihan dengan format ujian."),
    ("CUSTOM", "Asesmen Kustom", "Asesmen yang dikonfigurasi admin."),
]

ENTITLEMENTS = [
    ("free", "tutor_daily_limit", "10"), ("premium", "tutor_daily_limit", "40"),
    ("free", "parent_assistant_daily_limit", "10"), ("premium", "parent_assistant_daily_limit", "40"),
    ("free", "history_days", "30"), ("premium", "history_days", "365"),
]


def seed_base(db: Session) -> CurriculumVersion:
    if db.scalar(select(EducationLevel.id)) is None:
        sd, smp = EducationLevel(code="SD", name="Sekolah Dasar"), EducationLevel(code="SMP", name="Sekolah Menengah Pertama")
        db.add_all([sd, smp])
        db.flush()
        for n in range(1, 10):
            db.add(Grade(education_level_id=sd.id if n <= 6 else smp.id, number=n, phase={1: "A", 2: "B", 3: "C", 4: "D"}[band(n)]))
        db.flush()
    v = db.scalar(select(CurriculumVersion).where(CurriculumVersion.is_active.is_(True)))
    if v is None:
        v = CurriculumVersion(name="Kurikulum Merdeka", version="konfigurasi-awal", academic_year="2026/2027", is_active=True, status="active")
        db.add(v)
        db.flush()
        db.add(CurriculumSource(curriculum_version_id=v.id, title="Dokumen Capaian Pembelajaran resmi (belum diisi)", verification_status="unverified",
                                notes="Isi judul, instansi penerbit, nomor dokumen atau URL resmi, tanggal terbit, dan tanggal pengambilan melalui CMS, lalu verifikasi oleh peninjau."))
    for code, label, desc in TEMPLATES:
        if db.scalar(select(AssessmentTemplate.id).where(AssessmentTemplate.code == code)) is None:
            db.add(AssessmentTemplate(code=code, label=label, description=desc))
    for plan, key, value in ENTITLEMENTS:
        if db.scalar(select(SubscriptionEntitlement.id).where(SubscriptionEntitlement.plan == plan, SubscriptionEntitlement.key == key)) is None:
            db.add(SubscriptionEntitlement(plan=plan, key=key, value=value))
    for purpose, tpl in (("tutor", TUTOR_PROMPT), ("parent", PARENT_PROMPT)):
        if db.scalar(select(AIPromptVersion.id).where(AIPromptVersion.purpose == purpose)) is None:
            db.add(AIPromptVersion(purpose=purpose, version=1, template=tpl, is_active=True))
    for code, kind in (("grounded", "grounded"), ("anthropic", "anthropic"), ("openai_compat", "openai_compat")):
        if db.scalar(select(AIProvider.id).where(AIProvider.code == code)) is None:
            p = AIProvider(code=code, kind=kind, enabled=code == "grounded")
            db.add(p)
            db.flush()
            if code == "grounded":
                db.add(AIModel(provider_id=p.id, name="grounded-v1", is_default=True))
    db.flush()
    for g in db.scalars(select(Grade)):
        for i, (code, name, short) in enumerate(SUBJECTS[band(g.number)]):
            if db.scalar(select(Subject.id).where(Subject.curriculum_version_id == v.id, Subject.grade_id == g.id, Subject.code == code)) is None:
                db.add(Subject(curriculum_version_id=v.id, grade_id=g.id, code=code, name=name, short_label=short, sort_order=i))
    db.flush()
    for g in db.scalars(select(Grade).order_by(Grade.number)):
        base = len(SUBJECTS[band(g.number)])
        for i, (code, name, short) in enumerate(EXTRA_SUBJECTS):
            if db.scalar(select(Subject.id).where(Subject.curriculum_version_id == v.id, Subject.grade_id == g.id, Subject.code == code)) is None:
                db.add(Subject(curriculum_version_id=v.id, grade_id=g.id, code=code, name=name, short_label=short, sort_order=base + i))
    db.flush()
    return v


def seed_sample(db: Session, v: CurriculumVersion, publish: bool) -> int:
    status_ = "published" if publish else "in_review"
    tpl = db.scalar(select(AssessmentTemplate).where(AssessmentTemplate.code == "ASLM"))
    created = 0
    for grade_no, data in SAMPLE.items():
        g = db.scalar(select(Grade).where(Grade.number == grade_no))
        sub = db.scalar(select(Subject).where(Subject.curriculum_version_id == v.id, Subject.grade_id == g.id, Subject.code == "MAT"))
        num, title = data["chapter"]
        if db.scalar(select(Chapter.id).where(Chapter.subject_id == sub.id, Chapter.number == num)) is not None:
            continue
        ch = Chapter(subject_id=sub.id, number=num, title=title, semester=1)
        db.add(ch)
        db.flush()
        topics = []
        for i, (t, act, mistake) in enumerate(data["topics"]):
            topic = Topic(chapter_id=ch.id, title=t, sort_order=i, home_activity=act, common_mistake=mistake)
            db.add(topic)
            topics.append(topic)
        db.flush()
        lt, minutes, blocks = data["lesson"]
        lesson = Lesson(topic_id=topics[0].id, title=lt, minutes=minutes, status=status_, version=1 if publish else 0, is_sample=True, published_at=utcnow() if publish else None)
        for i, (kind, text, points, visual) in enumerate(blocks):
            lesson.blocks.append(LessonBlock(position=i, kind=kind, text=text, points=points, visual=visual))
        db.add(lesson)
        db.flush()
        if publish:
            retrieval.index_lesson(db, lesson, grade_no)

        def mkq(qtype, body, opts, ans, exp, hint, tidx, diff, usage, scaffold=None):
            q = Question(topic_id=topics[tidx].id, type=qtype, body=body, difficulty=diff, answer=ans, usage=usage, scaffold=scaffold, status=status_, version=1 if publish else 0, is_sample=True, published_at=utcnow() if publish else None)
            for j, label in enumerate(opts):
                q.options.append(QuestionOption(position=j, label=label))
            q.explanation = QuestionExplanation(explanation=exp, mistake_hint=hint)
            q.sources.append(QuestionSource(source="Konten contoh BOBO (wajib ditinjau ulang tim kurikulum sebelum produksi)"))
            db.add(q)
            return q

        for qi, (qtype, body, opts, ans, exp, hint, tidx, diff) in enumerate(data["practice"]):
            q = mkq(qtype, body, opts, ans, exp, hint, tidx, diff, "practice", SCAFFOLDS.get(grade_no, [None] * 10)[qi])
            db.flush()
            if publish:
                retrieval.index_question(db, q, grade_no, topics[tidx].title)
                created += 1
        etitle, eshort, emin, eqs = data["exam"]
        exam = Assessment(template_id=tpl.id, title=etitle, short_title=eshort, subject_id=sub.id, grade_number=grade_no, semester=1, duration_minutes=emin, status="published" if publish else "draft", is_sample=True)
        db.add(exam)
        db.flush()
        for pos, (qtype, body, opts, ans, exp, tidx) in enumerate(eqs):
            q = mkq(qtype, body, opts, ans, exp, None, tidx, "sedang", "assessment")
            db.flush()
            db.add(AssessmentQuestion(assessment_id=exam.id, question_id=q.id, position=pos))
        created += 1
    return created


def seed_prerequisites(db: Session, v: CurriculumVersion) -> int:
    def find(grade, title):
        return db.scalar(select(Topic).join(Chapter, Chapter.id == Topic.chapter_id).join(Subject, Subject.id == Chapter.subject_id).join(Grade, Grade.id == Subject.grade_id)
                         .where(Grade.number == grade, Topic.title == title, Subject.curriculum_version_id == v.id))
    n = 0
    for g, t, pg, pt in PREREQUISITES:
        a, b = find(g, t), find(pg, pt)
        if a and b and db.scalar(select(TopicPrerequisite.id).where(TopicPrerequisite.topic_id == a.id, TopicPrerequisite.prerequisite_topic_id == b.id)) is None:
            db.add(TopicPrerequisite(topic_id=a.id, prerequisite_topic_id=b.id))
            n += 1
    return n


def run(db: Session, sample: bool, publish_sample: bool, full: bool = False) -> dict:
    v = seed_base(db)
    if full:
        from app.seed.full import seed_full
        counts = seed_full(db, v, publish_sample)
        db.commit()
        return {"curriculum_version_id": v.id, **counts}
    n = seed_sample(db, v, publish_sample) if sample else 0
    if sample:
        db.flush()
        seed_prerequisites(db, v)
    db.commit()
    return {"curriculum_version_id": v.id, "sample_items": n}
