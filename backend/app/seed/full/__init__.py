import copy
import functools
import hashlib
import importlib
import random
from dataclasses import replace
from types import SimpleNamespace

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.db import utcnow
from app.models import (
    Assessment, AssessmentQuestion, AssessmentTemplate, Chapter, CurriculumVersion, Grade, Lesson, LessonBlock, Question, QuestionExplanation,
    QuestionOption, QuestionSource, Subject, Topic, TopicPrerequisite,
)
from app.seed.full import fig, latihan, mulok, sas
from app.seed.full.gen import generate
from app.seed.full.dsl import Q, S

GRADES = range(1, 10)
EXTRA_CODES = {"PAI", "SUN"}
SOURCE_NOTE = "Draf materi BOBO buatan AI, belum ditinjau guru/tim kurikulum"
DIFF = ["mudah", "mudah", "sedang", "menantang"]
VISUALS = {"frac", "tens", "tri"}


@functools.lru_cache(maxsize=None)
def load_grade(n: int):
    base = importlib.import_module(f"app.seed.full.g{n}")
    subjects = copy.deepcopy(base.SUBJECTS)
    prereq = list(base.PREREQ)
    try:
        ext = importlib.import_module(f"app.seed.full.x{n}")
    except ModuleNotFoundError:
        ext = None
    for s in subjects:
        sems = getattr(ext, "BASE_SEM", {}).get(s.code) if ext else None
        sems = sems or [1] + [2] * (len(s.chapters) - 1)
        for c, sem in zip(s.chapters, sems):
            c.semester = sem
        if ext and s.code in getattr(ext, "EXTEND", {}):
            chapters, exam = ext.EXTEND[s.code]
            offset = sum(len(c.topics) for c in s.chapters)
            s.chapters = s.chapters + copy.deepcopy(chapters)
            s.exam = s.exam + [replace(q, topic=q.topic + offset) for q in exam]
    if ext:
        subjects += copy.deepcopy(getattr(ext, "NEW", []))
        prereq += list(getattr(ext, "PREREQ", []))
    ag = _module(f"ag{n}")
    if ag is not None:
        subjects += copy.deepcopy(_mulok(n).subjects)
    ex = _module(f"ext{n}")
    offsets: dict[tuple[str, int], int] = {}
    if ex is not None:
        by_code = {s.code: s for s in subjects}
        for es in copy.deepcopy(_ext(n).subjects):
            target = by_code[es.code]
            sems = topic_semesters(target)
            for sem in (1, 2):
                offsets.setdefault((es.code, sem), sems.count(sem))
            for c in es.chapters:
                c.ext = True
                target.chapters.append(c)
    texts = []
    for name in (f"sas{n}", f"sasx{n}"):
        mod = _module(name)
        if mod is not None:
            texts.append(mod.BANK)
    if ag is not None:
        texts.append(ag.SAS)
    bank = sas.parse("\n".join(texts))
    if ex is not None and getattr(ex, "SAS", ""):
        for key, items in sas.parse(ex.SAS).items():
            bank.setdefault(key, []).extend((local + offsets[key], q) for local, q in items)
    for s in subjects:
        _apply_sas(s, bank)
        _fit_sas(s, n)
    lat = _module(f"lat{n}")
    practice = latihan.parse_bank("\n".join(x for x in (getattr(lat, "BANK", ""), getattr(ag, "BANK", ""), getattr(ex, "BANK", "")) if x))
    try:
        pics = figures(n)
    except fig.FigError:
        pics = {}
    for s in subjects:
        for c in s.chapters:
            for t in c.topics:
                pic = pics.get((s.code, t.title))
                auto = latihan.from_figure(pic, t.title) if pic else []
                gen = generate(n, t.title) if s.code == "MAT" else []
                t.qs = latihan.complete(t.qs, practice.get((s.code, t.title), []), auto, gen)
    return SimpleNamespace(GRADE=n, SUBJECTS=subjects, PREREQ=prereq)


def _module(name: str):
    try:
        return importlib.import_module(f"app.seed.full.{name}")
    except ModuleNotFoundError:
        return None


@functools.lru_cache(maxsize=None)
def _mulok(n: int) -> mulok.Parsed:
    ag = _module(f"ag{n}")
    return mulok.parse(ag.TOPICS) if ag is not None else mulok.Parsed()


@functools.lru_cache(maxsize=None)
def readings(n: int) -> dict:
    return {(code, title): fig.parse(spec) for code, title, spec in _mulok(n).reads + _ext(n).reads}


@functools.lru_cache(maxsize=None)
def _ext(n: int) -> mulok.Parsed:
    mod = _module(f"ext{n}")
    return mulok.parse(mod.TOPICS) if mod is not None else mulok.Parsed()


def _fit_sas(s: S, n: int) -> None:
    sems = topic_semesters(s)
    for sem in (1, 2):
        for typ, cap in zip(("mc", "fill", "essay"), sas.target(n)):
            while True:
                pos = [i for i, q in enumerate(s.exam) if 0 <= q.topic < len(sems) and sems[q.topic] == sem and q.type == typ]
                if len(pos) <= cap:
                    break
                load: dict[int, int] = {}
                for q in s.exam:
                    if 0 <= q.topic < len(sems) and sems[q.topic] == sem:
                        load[q.topic] = load.get(q.topic, 0) + 1
                victim = max(pos, key=lambda i: load[s.exam[i].topic])
                if load[s.exam[victim].topic] <= 1:
                    break
                del s.exam[victim]


@functools.lru_cache(maxsize=None)
def figures(n: int) -> dict:
    mod = _module(f"fig{n}")
    text = mod.BANK if mod is not None else ""
    extra = "\n".join(f"## {code}\n{title} :: {spec}" for code, title, spec in _mulok(n).figs + _ext(n).figs)
    return fig.parse_bank(text + "\n" + extra)


def _apply_sas(s: S, bank: dict) -> None:
    flat = [t for c in s.chapters for t in c.topics]
    sems = topic_semesters(s)
    for sem in (1, 2):
        items = bank.get((s.code, sem))
        if items is None:
            continue
        idx = [i for i, x in enumerate(sems) if x == sem]
        keep = []
        for q in s.exam:
            if 0 <= q.topic < len(sems) and sems[q.topic] == sem:
                t = flat[q.topic]
                if q.body not in {x.body for x in t.qs}:
                    t.qs.append(replace(q, topic=0))
            else:
                keep.append(q)
        items = sorted(items, key=lambda it: (sas.RANK[it[1].type], it[0]))
        s.exam = keep + [replace(q, topic=idx[local] if 0 <= local < len(idx) else -1) for local, q in items]


def topic_semesters(s: S) -> list[int]:
    return [c.semester for c in s.chapters for _ in c.topics]


def validate_question(q: Q, where: str) -> list[str]:
    errs = []
    if not q.body.strip() or not q.explanation.strip():
        errs.append(f"{where}: soal/pembahasan kosong")
    if q.type in ("mc", "tf"):
        idx = q.answer.get("index")
        if not isinstance(idx, int) or not 0 <= idx < len(q.options):
            errs.append(f"{where}: indeks jawaban di luar pilihan")
        if q.type == "mc" and len(q.options) < 3:
            errs.append(f"{where}: pilihan ganda kurang dari 3")
        if len(set(q.options)) != len(q.options):
            errs.append(f"{where}: pilihan kembar")
    elif q.type == "multi":
        ids = q.answer.get("indices") or []
        if not ids or any(not 0 <= i < len(q.options) for i in ids) or len(set(q.options)) != len(q.options):
            errs.append(f"{where}: jawaban multi tidak valid")
    elif q.type == "fill":
        if not q.answer.get("accepted"):
            errs.append(f"{where}: jawaban isian kosong")
    elif q.type == "essay":
        if not str(q.answer.get("model") or "").strip() or not q.answer.get("keys"):
            errs.append(f"{where}: uraian wajib punya contoh jawaban dan poin penting")
    else:
        errs.append(f"{where}: tipe {q.type} tidak didukung")
    if q.scaffold is not None and (not q.scaffold.get("steps") or len(q.scaffold["steps"]) > 8):
        errs.append(f"{where}: langkah kecil tidak valid")
    return errs


def validate_all(subject_codes: dict[int, list[str]]) -> list[str]:
    errs = []
    for n in GRADES:
        try:
            mod = load_grade(n)
        except ModuleNotFoundError:
            errs.append(f"Kelas {n}: belum ada")
            continue
        codes = [s.code for s in mod.SUBJECTS]
        if sorted(codes) != sorted(subject_codes[n]):
            errs.append(f"Kelas {n}: mapel {codes} tidak sama dengan {subject_codes[n]}")
        try:
            readings(n)
        except fig.FigError as e:
            errs.append(f"Kelas {n}: bacaan {e}")
        titles = set()
        for s in mod.SUBJECTS:
            flat = [t for c in s.chapters for t in c.topics]
            if len(flat) < 4:
                errs.append(f"Kelas {n} {s.code}: topik kurang dari 4")
            sems = topic_semesters(s)
            if sorted(set(c.semester for c in s.chapters)) != [1, 2]:
                errs.append(f"Kelas {n} {s.code}: harus ada bab Semester 1 dan Semester 2")
            practice = {q.body for t in flat for q in t.qs}
            for sem in (1, 2):
                qs = [q for q in s.exam if 0 <= q.topic < len(sems) and sems[q.topic] == sem]
                pg = [q for q in qs if q.type == "mc"]
                isian = [q for q in qs if q.type == "fill"]
                uraian = [q for q in qs if q.type == "essay"]
                want = sas.target(n)
                if (len(pg), len(isian), len(uraian)) != want or len(qs) != sum(want):
                    errs.append(f"Kelas {n} {s.code}: SAS Semester {sem} harus {want[0]} PG + {want[1]} isian + {want[2]} uraian, sekarang {len(pg)} PG + {len(isian)} isian + {len(uraian)} uraian dari {len(qs)} soal")
                covered = {q.topic for q in qs}
                missing = [i for i, x in enumerate(sems) if x == sem and i not in covered]
                if missing:
                    errs.append(f"Kelas {n} {s.code}: SAS Semester {sem} belum mencakup topik {[flat[i].title for i in missing]}")
                if any(len(q.options) != 4 for q in pg):
                    errs.append(f"Kelas {n} {s.code}: SAS Semester {sem} ada PG yang pilihannya bukan 4")
                bodies = [q.body for q in qs]
                if len(set(bodies)) != len(bodies):
                    errs.append(f"Kelas {n} {s.code}: SAS Semester {sem} ada soal kembar")
                for b in set(bodies) & practice:
                    errs.append(f"Kelas {n} {s.code}: SAS Semester {sem} sama dengan soal latihan: {b}")
            try:
                pics = figures(n)
            except fig.FigError as e:
                errs.append(f"Kelas {n}: {e}")
                pics = {}
            for t in flat:
                if len(t.qs) != latihan.TARGET:
                    errs.append(f"Kelas {n} {s.code} {t.title}: latihan {len(t.qs)} dari {latihan.TARGET} soal")
                pic = pics.get((s.code, t.title))
                if pic is None:
                    errs.append(f"Kelas {n} {s.code} {t.title}: belum ada gambar materi")
                elif fig.activity(pic)["mode"] == "explore" and pic["type"] in ("place", "frac", "line", "array", "count", "bars", "clock"):
                    errs.append(f"Kelas {n} {s.code} {t.title}: aktivitas gambar tidak terbentuk")
                if t.title in titles:
                    errs.append(f"Kelas {n}: judul topik kembar {t.title}")
                titles.add(t.title)
                if len(t.qs) < 4:
                    errs.append(f"Kelas {n} {t.title}: soal kurang dari 4")
                if t.lesson.visual and t.lesson.visual not in VISUALS:
                    errs.append(f"Kelas {n} {t.title}: visual tidak dikenal")
                for i, q in enumerate(t.qs):
                    errs += validate_question(q, f"Kelas {n} {s.code} {t.title} #{i + 1}")
            for i, q in enumerate(s.exam):
                if not 0 <= q.topic < len(flat):
                    errs.append(f"Kelas {n} {s.code} asesmen #{i + 1}: topik {q.topic} tidak ada")
                errs += validate_question(q, f"Kelas {n} {s.code} asesmen #{i + 1}")
        for topic, pg, ptopic in mod.PREREQ:
            if topic not in titles:
                errs.append(f"Kelas {n} prasyarat: topik {topic} tidak ada")
            try:
                ptitles = {t.title for s in load_grade(pg).SUBJECTS for c in s.chapters for t in c.topics}
            except ModuleNotFoundError:
                ptitles = set()
            if ptopic not in ptitles:
                errs.append(f"Kelas {n} prasyarat: {ptopic} (Kelas {pg}) tidak ada")
    return errs


def arrange(q: Q) -> tuple[list[str], dict]:
    if q.type not in ("mc", "multi"):
        return list(q.options), dict(q.answer)
    order = list(range(len(q.options)))
    random.Random(int(hashlib.sha256(q.body.encode()).hexdigest(), 16)).shuffle(order)
    options = [q.options[i] for i in order]
    if q.type == "mc":
        return options, {"index": order.index(q.answer["index"])}
    return options, {"indices": sorted(order.index(i) for i in q.answer["indices"])}


def _question(topic_id: int, q: Q, usage: str, diff: str, status: str, publish: bool) -> Question:
    options, answer = arrange(q)
    row = Question(topic_id=topic_id, type=q.type, body=q.body, difficulty=q.difficulty or diff, answer=answer, usage=usage, scaffold=q.scaffold if usage == "practice" else None,
                   status=status, version=1 if publish else 0, is_sample=True, published_at=utcnow() if publish else None)
    for j, label in enumerate(options):
        row.options.append(QuestionOption(position=j, label=label))
    if q.type == "essay":
        row.rubric = f"{q.answer['model']}\nPoin penting: " + "; ".join(q.answer["keys"])
    row.explanation = QuestionExplanation(explanation=q.explanation, mistake_hint=q.hint)
    row.sources.append(QuestionSource(source=SOURCE_NOTE))
    return row


def seed_full(db: Session, v: CurriculumVersion, publish: bool = False) -> dict:
    status = "published" if publish else "in_review"
    tpl = db.scalar(select(AssessmentTemplate).where(AssessmentTemplate.code == "ASAS")) or db.scalar(select(AssessmentTemplate).where(AssessmentTemplate.code == "ASLM"))
    counts = {"topics": 0, "lessons": 0, "questions": 0, "assessments": 0}
    topic_ids: dict[tuple[int, str], int] = {}
    mods = {n: load_grade(n) for n in GRADES}
    passes = [(n, s, mod) for n, mod in mods.items() for s in mod.SUBJECTS if s.code not in EXTRA_CODES]
    passes += [(n, s, mod) for n, mod in mods.items() for s in mod.SUBJECTS if s.code in EXTRA_CODES]
    plan = []
    for n, s, mod in passes:
        g = db.scalar(select(Grade).where(Grade.number == n))
        sub = db.scalar(select(Subject).where(Subject.curriculum_version_id == v.id, Subject.grade_id == g.id, Subject.code == s.code))
        if sub is None or db.scalar(select(Chapter.id).where(Chapter.subject_id == sub.id)) is not None:
            continue
        order = sorted(range(len(s.chapters)), key=lambda i: (s.chapters[i].semester, not s.chapters[i].first, i))
        numbers = {ci: rank + 1 for rank, ci in enumerate(order)}
        starts, k = [], 0
        for c in s.chapters:
            starts.append(k)
            k += len(c.topics)
        plan.append((n, s, sub, numbers, starts, [None] * k))

    def build(item, ext: bool) -> None:
        n, s, sub, numbers, starts, flat = item
        for ci, c in enumerate(s.chapters):
            if c.ext != ext:
                continue
            ch = Chapter(subject_id=sub.id, number=numbers[ci], title=c.title, semester=c.semester)
            db.add(ch)
            db.flush()
            prev = None
            for ti, t in enumerate(c.topics):
                topic = Topic(chapter_id=ch.id, title=t.title, sort_order=starts[ci] + ti, home_activity=t.act, common_mistake=t.mistake)
                db.add(topic)
                db.flush()
                flat[starts[ci] + ti] = topic
                topic_ids[(n, t.title)] = topic.id
                counts["topics"] += 1
                ls = t.lesson
                lesson = Lesson(topic_id=topic.id, title=t.title, minutes=ls.minutes, status=status, version=1 if publish else 0, is_sample=True, published_at=utcnow() if publish else None)
                pic = figures(n).get((s.code, t.title))
                act = fig.activity(pic) if pic else None
                blocks = [("Penjelasan", ls.explain, None, ls.visual, pic), ("Contoh", ls.example, None, None, readings(n).get((s.code, t.title)))]
                if act:
                    blocks.append(("Ayo coba", act["ask"], None, None, act))
                blocks += [("Poin penting", None, ls.points, None, None), ("Ringkasan", ls.summary, None, None, None)]
                for bi, (kind, text, points, visual, figure) in enumerate(blocks):
                    lesson.blocks.append(LessonBlock(position=bi, kind=kind, text=text, points=points, visual=visual, figure=figure))
                db.add(lesson)
                counts["lessons"] += 1
                for qi, q in enumerate(t.qs):
                    db.add(_question(topic.id, q, "practice", DIFF[min(qi, 3)], status, publish))
                    counts["questions"] += 1
                if prev is not None:
                    db.add(TopicPrerequisite(topic_id=topic.id, prerequisite_topic_id=prev.id))
                prev = topic
        db.flush()

    for item in plan:
        build(item, False)
    for item in plan:
        build(item, True)
    for n, s, sub, numbers, starts, flat in plan:
        sems = topic_semesters(s)
        for sem in (1, 2):
            qs = [q for q in s.exam if sems[q.topic] == sem]
            if not qs:
                continue
            exam = Assessment(template_id=tpl.id, title=f"SAS {'Ganjil' if sem == 1 else 'Genap'} (Semester {sem}): {sub.name} Kelas {n}", short_title=sub.name, subject_id=sub.id, grade_number=n, semester=sem,
                              duration_minutes=max(10, 2 * len(qs) + 3 * sum(1 for q in qs if q.type == "essay")), status="published" if publish else "draft", is_sample=True)
            db.add(exam)
            db.flush()
            for pos, q in enumerate(qs):
                row = _question(flat[q.topic].id, q, "assessment", "sedang", status, publish)
                db.add(row)
                db.flush()
                db.add(AssessmentQuestion(assessment_id=exam.id, question_id=row.id, position=pos))
                counts["questions"] += 1
            counts["assessments"] += 1
    db.flush()
    for n, mod in mods.items():
        for topic, pg, ptopic in mod.PREREQ:
            a, b = topic_ids.get((n, topic)), topic_ids.get((pg, ptopic))
            if a and b and db.scalar(select(TopicPrerequisite.id).where(TopicPrerequisite.topic_id == a, TopicPrerequisite.prerequisite_topic_id == b)) is None:
                db.add(TopicPrerequisite(topic_id=a, prerequisite_topic_id=b))
    db.flush()
    return counts
