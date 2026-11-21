import uuid
from datetime import timedelta

from app.core.db import utcnow
from app.models import ExerciseAttempt, ReviewItem
from tests.conftest import add_child, register, staff


def _q(client, sh, body_contains, topic_id=None):
    path = "/v1/student/practice" + (f"?topic_id={topic_id}" if topic_id else "")
    return next(q for q in client.get(path, headers=sh).json()["questions"] if body_contains in q["body"])


def _ans(client, sh, q, resp, mode="practice"):
    return client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": resp, "mode": mode}, headers=sh).json()


def test_spaced_review_cycle(client, db):
    _, h = register(client)
    cid, sh = add_child(client, h)
    q = _q(client, sh, "1/4 + 2/4")
    wrong = next(o["index"] for o in q["options"] if o["label"] == "3/8")
    right = next(o["index"] for o in q["options"] if o["label"] == "3/4")
    r = _ans(client, sh, q, {"index": wrong})
    assert r["scaffold"]["steps"]
    assert client.get("/v1/student/review", headers=sh).json()["due"] == 0
    item = db.query(ReviewItem).one()
    item.due_at = utcnow() - timedelta(minutes=1)
    db.commit()
    rv = client.get("/v1/student/review", headers=sh).json()
    assert rv["due"] == 1 and rv["questions"][0]["id"] == q["id"]
    for step in range(3):
        _ans(client, sh, q, {"index": right}, "review")
        db.expire_all()
        it = db.query(ReviewItem).one_or_none()
        if step < 2:
            assert it.step == step + 1 and it.due_at > utcnow()
            it.due_at = utcnow() - timedelta(minutes=1)
            db.commit()
        else:
            assert it is None
    assert client.get("/v1/student/home", headers=sh).json()["review_due"] == 0


def test_scaffold_hidden_until_wrong_and_similar(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    q = _q(client, sh, "2/3")
    assert "scaffold" not in q
    ok = _ans(client, sh, q, {"index": 0})
    assert ok["correct"] and ok["scaffold"] is None
    sim = client.get(f"/v1/student/practice/similar?question_id={q['id']}", headers=sh).json()
    assert sim["id"] != q["id"] and sim["topic"] == "Pecahan Senilai" and "answer" not in sim


def test_foundation_path_cross_grade(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    q = _q(client, sh, "1/4 + 2/4")
    wrong = next(o["index"] for o in q["options"] if o["label"] == "3/8")
    for _ in range(6):
        _ans(client, sh, q, {"index": wrong})
    f = client.get("/v1/student/foundation", headers=sh).json()["topics"]
    titles = {x["topic"]: x for x in f}
    assert "Pecahan Senilai" in titles and "Penjumlahan sampai 100" in titles
    low = titles["Penjumlahan sampai 100"]
    assert low["grade"] == 2 and low["lesson_id"]
    les = client.get(f"/v1/student/lessons/{low['lesson_id']}", headers=sh)
    assert les.status_code == 200
    pq = client.get(f"/v1/student/practice?topic_id={low['topic_id']}", headers=sh).json()["questions"]
    assert pq and _ans(client, sh, pq[0], {"index": 0}, "foundation")["question_id"] == pq[0]["id"]
    recs = client.get(f"/v1/parent/children/{cid}/recommendations", headers=h).json()["recommendations"]
    assert any(r["kind"] == "foundation" and "Kelas 2" in r["title"] for r in recs)
    _, sh8 = add_child(client, h, "Dimas", 8)
    assert client.get(f"/v1/student/lessons/{low['lesson_id']}", headers=sh8).status_code == 404


def test_settings_fewer_options_and_privacy(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    assert len(_q(client, sh, "2/3")["options"]) == 4
    r = client.patch(f"/v1/parent/children/{cid}", json={"settings": {"fewer_options": True, "larger_text": True}}, headers=h).json()
    assert r["settings"]["fewer_options"] and r["settings"]["larger_text"] and not r["settings"]["read_aloud"]
    q = _q(client, sh, "2/3")
    assert len(q["options"]) == 3 and "4/6" in [o["label"] for o in q["options"]]
    assert client.get("/v1/student/me", headers=sh).json()["settings"]["fewer_options"] is True
    assert "Kebijakan Privasi" in client.get("/privacy").text


def test_tutor_styles(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    base = client.post("/v1/student/tutor/messages", json={"text": "apa itu pecahan senilai"}, headers=sh).json()
    assert base["can_restyle"] and base["visual_available"]
    steps = client.post("/v1/student/tutor/messages", json={"text": "apa itu pecahan senilai", "style": "steps"}, headers=sh).json()
    assert steps["reply"].startswith("Langkah demi langkah") and "1." in steps["reply"]
    story = client.post("/v1/student/tutor/messages", json={"text": "apa itu pecahan senilai", "style": "story"}, headers=sh).json()
    assert "martabak" in story["reply"]
    vis = client.post("/v1/student/tutor/messages", json={"text": "apa itu pecahan senilai", "style": "visual"}, headers=sh).json()
    assert vis["visual"] == "frac"


def test_growth_signals_summary(client, db):
    _, h = register(client)
    cid, sh = add_child(client, h)
    q = _q(client, sh, "1/4 + 2/4")
    right = next(o["index"] for o in q["options"] if o["label"] == "3/4")
    wrong = next(o["index"] for o in q["options"] if o["label"] == "3/8")
    pattern = [1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
    for p in pattern:
        _ans(client, sh, q, {"index": right if p else wrong})
    rows = db.query(ExerciseAttempt).order_by(ExerciseAttempt.id).all()
    for i, row in enumerate(rows):
        row.answered_at = utcnow() - timedelta(days=(len(rows) - i) // 3)
    db.commit()
    g = client.get("/v1/student/growth", headers=sh).json()
    assert g["total_answers"] == 10 and g["topics"][0]["topic"] == "Penjumlahan Pecahan"
    assert next(b for b in g["badges"] if b["key"] == "persist")["earned"]
    d = client.get(f"/v1/parent/children/{cid}/dashboard", headers=h).json()
    assert d["signals"] and d["signals"][0]["topic"] == "Penjumlahan Pecahan" and len(d["signals"][0]["plan"]) == 7
    text = client.get(f"/v1/parent/children/{cid}/summary", headers=h).json()["text"]
    assert "Nadia" in text and "bukan diagnosis" in text and "Penjumlahan Pecahan" in text
    _, h2 = register(client)
    assert client.get(f"/v1/parent/children/{cid}/summary", headers=h2).status_code == 404


def test_admin_prerequisites_and_scaffold(client, db):
    ed = staff(db, "editor")
    subs = client.get("/v1/admin/subjects?grade=5", headers=ed).json()
    tree = client.get(f"/v1/admin/subjects/{next(s for s in subs if s['code'] == 'MAT')['id']}/tree", headers=ed).json()
    topics = {t["title"]: t["id"] for t in tree["chapters"][0]["topics"]}
    got = client.get(f"/v1/admin/topics/{topics['Penjumlahan Pecahan']}/prerequisites", headers=ed).json()
    assert {x["title"] for x in got} == {"Pecahan Senilai", "Penjumlahan sampai 100"}
    loop = client.put(f"/v1/admin/topics/{topics['Pecahan Senilai']}/prerequisites", json={"prerequisite_topic_ids": [topics["Soal Cerita Pecahan"]]}, headers=ed)
    assert loop.status_code == 422
    q = client.post("/v1/admin/questions", json={"topic_id": topics["Pecahan Desimal"], "type": "fill", "body": "0,5 = …/10", "answer": {"accepted": ["5"]}, "explanation": "0,5 = 5/10", "source": "Tim", "scaffold": {"example": "0,3 = 3/10", "steps": ["Lihat angka di belakang koma", " "]}}, headers=ed).json()
    assert q["scaffold"] == {"example": "0,3 = 3/10", "steps": ["Lihat angka di belakang koma"]}
