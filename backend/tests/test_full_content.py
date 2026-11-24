from sqlalchemy import text

from app.core.db import get_engine
from app.seed.full import arrange, load_grade, validate_all
from app.seed.sample_content import EXTRA_SUBJECTS, SUBJECTS
from app.seed.seed import run
from app.services.bundle import build_bundle
from app.services.learning import band


def codes():
    return {n: [s[0] for s in SUBJECTS[band(n)]] + [s[0] for s in EXTRA_SUBJECTS] for n in range(1, 10)}


def test_full_content_is_valid():
    assert validate_all(codes()) == []


def test_option_order_keeps_answer():
    for n in range(1, 10):
        for s in load_grade(n).SUBJECTS:
            for q in [q for c in s.chapters for t in c.topics for q in t.qs] + s.exam:
                options, answer = arrange(q)
                assert sorted(options) == sorted(q.options)
                if q.type == "mc":
                    assert options[answer["index"]] == q.options[q.answer["index"]]
                if q.type == "multi":
                    assert sorted(options[i] for i in answer["indices"]) == sorted(q.options[i] for i in q.answer["indices"])


def test_seed_full_builds_every_grade(db):
    with get_engine().begin() as c:
        tables = [r[0] for r in c.execute(text("select tablename from pg_tables where schemaname='public' and tablename <> 'alembic_version'"))]
        c.execute(text("TRUNCATE " + ", ".join(f'"{t}"' for t in tables) + " RESTART IDENTITY CASCADE"))
    out = run(db, sample=False, publish_sample=False, full=True)
    assert out["topics"] == 701 and out["lessons"] == 701 and out["assessments"] == 176
    assert out["questions"] >= 18000
    b = build_bundle(db, include_sample=True)
    assert len(b["lessons"]) == 701 and len(b["assessments"]) == 176
    qtype = {q["id"]: q["type"] for q in b["questions"]}
    for a in b["assessments"]:
        types = [qtype[x["id"]] for x in a["questions"]]
        want = (20, 10, 5) if a["grade"] <= 6 else (35, 5, 5)
        assert (types.count("mc"), types.count("fill"), types.count("essay")) == want, a["title"]
    assert {a["semester"] for a in b["assessments"]} == {1, 2}
    assert {c["semester"] for c in b["chapters"]} == {1, 2}
    for lesson in b["lessons"]:
        kinds = [x["kind"] for x in lesson["blocks"]]
        assert kinds == ["Penjelasan", "Contoh", "Ayo coba", "Poin penting", "Ringkasan"], lesson["title"]
        assert lesson["blocks"][0]["figure"]["type"] and lesson["blocks"][2]["figure"]["type"] == "activity"
    assert all(x["sample"] for x in b["lessons"])
    assert build_bundle(db)["lessons"] == []
    by_grade = {}
    for s in b["subjects"]:
        by_grade.setdefault(s["grade"], 0)
        by_grade[s["grade"]] += 1
    assert by_grade == {1: 7, 2: 7, 3: 9, 4: 9, 5: 10, 6: 10, 7: 12, 8: 12, 9: 12}
    practice = {}
    for q in b["questions"]:
        if q["usage"] == "practice":
            practice[q["topic_id"]] = practice.get(q["topic_id"], 0) + 1
    assert set(practice.values()) == {20} and len(practice) == 701
    reads = [x["figure"]["type"] for lesson in b["lessons"] for x in lesson["blocks"] if x["kind"] == "Contoh" and x.get("figure")]
    assert reads.count("quran") >= 18 and reads.count("doa") >= 2
    again = run(db, sample=False, publish_sample=False, full=True)
    assert again["lessons"] == 0
