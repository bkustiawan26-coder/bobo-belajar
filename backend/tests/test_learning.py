import uuid
from datetime import timedelta

from app.core.db import utcnow
from app.models import AssessmentSession
from tests.conftest import add_child, register


def _q(client, sh, body_contains):
    qs = client.get("/v1/student/practice", headers=sh).json()["questions"]
    return next(q for q in qs if body_contains in q["body"])


def test_catalog_lesson_and_grade_isolation(client):
    _, h = register(client)
    _, sh5 = add_child(client, h, "Nadia", 5)
    _, sh8 = add_child(client, h, "Dimas", 8)
    cat = client.get("/v1/student/catalog", headers=sh5).json()
    mat = next(s for s in cat["subjects"] if s["name"] == "Matematika")
    assert mat["ready"] and mat["chapters"][0]["title"] == "Pecahan"
    lid = mat["chapters"][0]["topics"][0]["lesson"]["id"]
    les = client.get(f"/v1/student/lessons/{lid}", headers=sh5).json()
    assert les["title"] == "Pecahan Senilai" and len(les["blocks"]) == 4
    assert client.get(f"/v1/student/lessons/{lid}", headers=sh8).status_code == 404
    other = [s for s in cat["subjects"] if s["name"] != "Matematika"]
    assert other and not any(s["ready"] for s in other)


def test_practice_hides_answers_and_grades_server_side(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    q = _q(client, sh, "1/4 + 2/4")
    assert "answer" not in q and "explanation" not in q
    wrong = next(o["index"] for o in q["options"] if o["label"] == "3/8")
    r = client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": {"index": wrong}}, headers=sh).json()
    assert r["correct"] is False and r["correct_answer"] == "3/4" and "Penyebut tidak ikut" in r["mistake_hint"]
    multi = _q(client, sh, "Pilih semua pecahan")
    ok = client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": multi["id"], "response": {"indices": [3, 1, 0]}}, headers=sh).json()
    assert ok["correct"] is True
    fill = _q(client, sh, "(isi pembilangnya)")
    ok2 = client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": fill["id"], "response": {"text": " 4 "}}, headers=sh).json()
    assert ok2["correct"] is True


def test_attempt_idempotent(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    q = _q(client, sh, "2/3")
    cu = str(uuid.uuid4())
    for _ in range(3):
        client.post("/v1/student/practice/attempts", json={"client_uuid": cu, "question_id": q["id"], "response": {"index": 0}}, headers=sh)
    d = client.get(f"/v1/parent/children/{cid}/dashboard", headers=h).json()
    assert d["kpis"]["answers_total"] == 1


def test_mastery_rules_and_recommendations(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    q = _q(client, sh, "2/3")
    client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": {"index": 0}}, headers=sh)
    m = {x["topic"]: x for x in client.get("/v1/student/progress", headers=sh).json()["mastery"]}
    assert m["Pecahan Senilai"]["state"] == "insufficient"
    assert m["Pecahan Desimal"]["state"] == "not_started"
    for _ in range(3):
        client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": {"index": 0}}, headers=sh)
    m = {x["topic"]: x for x in client.get("/v1/student/progress", headers=sh).json()["mastery"]}
    assert m["Pecahan Senilai"]["state"] == "demonstrated"
    add = _q(client, sh, "1/4 + 2/4")
    for idx in (1, 1, 0):
        client.post("/v1/student/practice/attempts", json={"client_uuid": str(uuid.uuid4()), "question_id": add["id"], "response": {"index": idx}}, headers=sh)
    recs = client.get(f"/v1/parent/children/{cid}/recommendations", headers=h).json()["recommendations"]
    dev = next(r for r in recs if r["kind"] == "practice")
    assert "Penjumlahan Pecahan" in dev["title"] and "1 dari 3" in dev["evidence"]
    assert recs[0]["kind"] == "practice"
    done = client.post(f"/v1/parent/children/{cid}/recommendations/{dev['id']}/done", json={"done": True}, headers=h).json()
    assert done["done"] is True


def test_offline_pack_and_sync(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    pack = client.get("/v1/student/offline-pack", headers=sh).json()
    assert pack["lessons"] and all("answer" in q for q in pack["questions"])
    assert not any("Asesmen" in q["body"] for q in pack["questions"])
    q = pack["questions"][0]
    batch = {"batch_uuid": str(uuid.uuid4()), "attempts": [
        {"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": q["answer"], "answered_at": (utcnow() - timedelta(hours=2)).isoformat()},
        {"client_uuid": str(uuid.uuid4()), "question_id": q["id"], "response": q["answer"], "answered_at": (utcnow() + timedelta(days=2)).isoformat()},
        {"client_uuid": str(uuid.uuid4()), "question_id": 999999, "response": {"index": 0}},
    ], "lesson_progress": [{"lesson_id": pack["lessons"][0]["id"], "step": 3, "completed": True}]}
    r1 = client.post("/v1/student/sync", json=batch, headers=sh).json()
    assert r1["summary"] == {"accepted": 1, "duplicate": 0, "rejected": 2}
    r2 = client.post("/v1/student/sync", json=batch, headers=sh).json()
    assert r2["summary"]["accepted"] == 0 and r2["summary"]["duplicate"] == 1
    d = client.get(f"/v1/parent/children/{cid}/dashboard", headers=h).json()
    assert d["kpis"]["answers_total"] == 1 and d["kpis"]["lessons_completed"] == 1


def _start(client, sh):
    a = client.get("/v1/student/assessments", headers=sh).json()["assessments"][0]
    return client.post(f"/v1/student/assessments/{a['id']}/start", headers=sh).json()


def test_assessment_flow_scoring_and_idempotent_submit(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    s = _start(client, sh)
    assert len(s["questions"]) == 5 and "answer" not in s["questions"][0]
    again = client.post(f"/v1/student/assessments/{s['assessment_id']}/start", headers=sh).json()
    assert again["session_id"] == s["session_id"]
    keys = {"Pecahan senilai dengan 3/5": "6/10", "2/7 + 3/7": "5/7", "4/8 senilai": "Benar", "Sebuah tali": "2/5"}
    for q in s["questions"]:
        want = next((v for k, v in keys.items() if k in q["body"]), None)
        if want:
            idx = next(o["index"] for o in q["options"] if o["label"] == want)
            assert client.put(f"/v1/student/assessment-sessions/{s['session_id']}/answers", json={"question_id": q["id"], "response": {"index": idx}}, headers=sh).status_code == 200
    r1 = client.post(f"/v1/student/assessment-sessions/{s['session_id']}/submit", json={"idempotency_key": "kunci-12345"}, headers=sh).json()
    assert r1["correct"] == 3 and r1["total"] == 5 and r1["score"] == 60
    assert {w["title"] for w in r1["weak_topics"]} == {"Soal Cerita Pecahan", "Penjumlahan Pecahan"}
    r2 = client.post(f"/v1/student/assessment-sessions/{s['session_id']}/submit", json={"idempotency_key": "kunci-lain-999"}, headers=sh).json()
    assert r2 == r1
    d = client.get(f"/v1/parent/children/{cid}/dashboard", headers=h).json()
    assert len(d["assessments"]) == 1 and d["kpis"]["last_assessment"]["score"] == 60
    assert client.put(f"/v1/student/assessment-sessions/{s['session_id']}/answers", json={"question_id": s["questions"][0]["id"], "response": {"index": 0}}, headers=sh).status_code == 409


def test_assessment_deadline_enforced(client, db):
    _, h = register(client)
    _, sh = add_child(client, h)
    s = _start(client, sh)
    sess = db.get(AssessmentSession, uuid.UUID(s["session_id"]))
    sess.deadline_at = utcnow() - timedelta(minutes=5)
    db.commit()
    assert client.put(f"/v1/student/assessment-sessions/{s['session_id']}/answers", json={"question_id": s["questions"][0]["id"], "response": {"index": 0}}, headers=sh).status_code == 409
    q0 = s["questions"][0]
    r = client.post(f"/v1/student/assessment-sessions/{s['session_id']}/submit", json={"idempotency_key": "telat-12345", "answers": [{"question_id": q0["id"], "response": {"index": 0}}]}, headers=sh).json()
    assert r["auto_submitted"] is True and r["correct"] == 0


def test_expired_session_auto_finalized_on_list(client, db):
    _, h = register(client)
    _, sh = add_child(client, h)
    s = _start(client, sh)
    sess = db.get(AssessmentSession, uuid.UUID(s["session_id"]))
    sess.deadline_at = utcnow() - timedelta(minutes=5)
    db.commit()
    lst = client.get("/v1/student/assessments", headers=sh).json()["assessments"][0]
    assert lst["active_session_id"] is None and lst["last_result"]["score"] == 0
