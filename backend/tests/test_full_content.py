from sqlalchemy import text

from app.core.db import get_engine
from app.seed.full import arrange, load_grade, validate_all
from app.seed.sample_content import SUBJECTS
from app.seed.seed import run
from app.services.bundle import build_bundle
from app.services.learning import band


def codes():
    return {n: [s[0] for s in SUBJECTS[band(n)]] for n in range(1, 10)}


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
    assert out["topics"] == 165 and out["lessons"] == 165 and out["assessments"] == 41
    assert out["questions"] >= 900
    b = build_bundle(db, include_sample=True)
    assert len(b["lessons"]) == 165 and len(b["assessments"]) == 41
    assert all(x["sample"] for x in b["lessons"])
    assert build_bundle(db)["lessons"] == []
    by_grade = {}
    for s in b["subjects"]:
        by_grade.setdefault(s["grade"], 0)
        by_grade[s["grade"]] += 1
    assert by_grade == {1: 4, 2: 4, 3: 4, 4: 4, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}
    again = run(db, sample=False, publish_sample=False, full=True)
    assert again["lessons"] == 0
