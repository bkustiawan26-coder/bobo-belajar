from app.models import SubscriptionEntitlement
from tests.conftest import add_child, register, staff


def test_tutor_grounded_answer_with_source(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    r = client.post("/v1/student/tutor/messages", json={"text": "Apa itu pecahan senilai?"}, headers=sh).json()
    assert "senilai" in r["reply"].lower() and r["sources"] and r["refused"] is False
    assert r["quota_left"] == 9


def test_tutor_hint_mode(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    r = client.post("/v1/student/tutor/messages", json={"text": "Beri aku petunjuk penjumlahan pecahan 1/4 + 2/4"}, headers=sh).json()
    assert r["reply"].startswith("Petunjuk")


def test_tutor_refuses_personal_info_and_logs(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    r = client.post("/v1/student/tutor/messages", json={"text": "boleh minta nomor hp kamu?"}, headers=sh).json()
    assert r["refused"] is True and "informasi pribadi" in r["reply"]
    r2 = client.post("/v1/student/tutor/messages", json={"text": "nomorku 081234567890 ya"}, headers=sh).json()
    assert r2["refused"] is True
    kids = client.get("/v1/parent/children", headers=h).json()["children"]
    assert kids[0]["safety_refusals"] == 2


def test_tutor_out_of_scope_is_honest(client):
    _, h = register(client)
    _, sh = add_child(client, h)
    r = client.post("/v1/student/tutor/messages", json={"text": "Siapa presiden pertama Amerika?"}, headers=sh).json()
    assert "belum tersedia" in r["reply"] or "hanya menjawab" in r["reply"]


def test_tutor_quota_enforced(client, db):
    for row in db.query(SubscriptionEntitlement).filter(SubscriptionEntitlement.plan == "free", SubscriptionEntitlement.key == "tutor_daily_limit"):
        row.value = "2"
    db.commit()
    _, h = register(client)
    _, sh = add_child(client, h)
    for _ in range(2):
        assert client.post("/v1/student/tutor/messages", json={"text": "pecahan senilai"}, headers=sh).status_code == 200
    assert client.post("/v1/student/tutor/messages", json={"text": "pecahan senilai"}, headers=sh).status_code == 429


def test_parent_assistant_evidence_and_no_diagnosis(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    r = client.post("/v1/parent/assistant/messages", json={"child_id": cid, "text": "Apakah anak saya disleksia?"}, headers=h).json()
    assert "tidak memberi diagnosis" in r["reply"]
    r2 = client.post("/v1/parent/assistant/messages", json={"child_id": cid, "text": "Kenapa anak saya kesulitan?"}, headers=h).json()
    assert "Berdasarkan 0 jawaban" in r2["basis"]
    _, h2 = register(client)
    assert client.post("/v1/parent/assistant/messages", json={"child_id": cid, "text": "halo"}, headers=h2).status_code == 404


def test_content_review_publish_flow(client, db):
    ed = staff(db, "editor")
    rv = staff(db, "reviewer")
    tree_subjects = client.get("/v1/admin/subjects?grade=3", headers=ed).json()
    mat = next(s for s in tree_subjects if s["code"] == "MAT")
    ch = client.post("/v1/admin/chapters", json={"subject_id": mat["id"], "number": 1, "title": "Perkalian"}, headers=ed).json()
    tp = client.post("/v1/admin/topics", json={"chapter_id": ch["id"], "title": "Perkalian Dasar", "home_activity": "Hitung kelompok benda di rumah."}, headers=ed).json()
    bad = client.post("/v1/admin/questions", json={"topic_id": tp["id"], "type": "mc", "body": "3 × 4 = …", "options": [{"label": "12"}, {"label": "7"}], "answer": {"index": 5}, "explanation": "3 kelompok isi 4.", "source": "Tim konten"}, headers=ed)
    assert bad.status_code == 422
    q = client.post("/v1/admin/questions", json={"topic_id": tp["id"], "type": "mc", "body": "3 × 4 = …", "options": [{"label": "12"}, {"label": "7"}], "answer": {"index": 0}, "explanation": "3 kelompok isi 4 = 12.", "source": "Tim konten"}, headers=ed).json()
    assert client.post(f"/v1/admin/questions/{q['id']}/publish", headers=rv).status_code == 409
    assert client.post(f"/v1/admin/questions/{q['id']}/submit", headers=ed).status_code == 200
    assert client.post(f"/v1/admin/questions/{q['id']}/review", json={"decision": "approve"}, headers=ed).status_code == 403
    assert client.post(f"/v1/admin/questions/{q['id']}/review", json={"decision": "approve"}, headers=rv).status_code == 200
    _, h = register(client)
    _, sh = add_child(client, h, "Bima", 3)
    assert client.get("/v1/student/practice", headers=sh).json()["questions"] == []
    assert client.post(f"/v1/admin/questions/{q['id']}/publish", headers=rv).json()["status"] == "published"
    assert len(client.get("/v1/student/practice", headers=sh).json()["questions"]) == 1


def test_import_is_always_draft_and_stats(client, db):
    ad = staff(db, "admin")
    payload = {"format": "bobo-content-v1", "curriculum_version_id": 1, "subjects": [{"grade_number": 4, "code": "MATX", "name": "Matematika Tambahan", "chapters": [{"number": 1, "title": "Bangun Datar", "topics": [{"title": "Persegi", "lessons": [{"title": "Persegi", "minutes": 5, "blocks": [{"kind": "Penjelasan", "text": "Persegi punya empat sisi sama panjang."}]}], "questions": [{"type": "tf", "body": "Persegi punya 4 sisi.", "answer": {"index": 0}, "explanation": "Benar.", "source": "Impor"}]}]}]}]}
    r = client.post("/v1/admin/import", json=payload, headers=ad).json()
    assert r["lessons"] == 1 and r["questions"] == 1
    st = client.get("/v1/admin/stats", headers=ad).json()
    assert st["lessons"]["draft"] == 1 and st["unverified_sources"] == 1
    assert client.post("/v1/admin/curriculum/versions/1/sources", json={"title": "CP Matematika", "verification_status": "verified"}, headers=ad).status_code == 422
    usage = client.get("/v1/admin/ai/usage", headers=ad).json()
    assert usage["total_cost_usd"] == 0.0


class _Resp:
    def __init__(self, data, code=200):
        self._d, self.status_code = data, code

    def json(self):
        return self._d

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError("http error")


def test_external_provider_cost_logging_and_fallback(client, db, monkeypatch):
    from app.core.config import get_settings
    from app.models import AIUsageLog
    from app.services.ai import providers
    s = get_settings()
    monkeypatch.setattr(s, "ai_provider", "openai_compat")
    monkeypatch.setattr(s, "ai_model", "model-uji")
    monkeypatch.setattr(s, "openai_compat_base_url", "http://llm.local/v1")
    monkeypatch.setattr(s, "ai_price_input_per_mtok", 1.0)
    monkeypatch.setattr(s, "ai_price_output_per_mtok", 4.0)
    seen = {}

    def fake_post(url, headers=None, json=None, timeout=None):
        seen["system"] = json["messages"][0]["content"]
        seen["user"] = json["messages"][1]["content"]
        return _Resp({"choices": [{"message": {"content": "Pecahan senilai punya nilai sama. Lihat https://contoh.com ya."}}], "usage": {"prompt_tokens": 1000, "completion_tokens": 500}})

    monkeypatch.setattr(providers.httpx, "post", fake_post)
    _, h = register(client)
    _, sh = add_child(client, h)
    r = client.post("/v1/student/tutor/messages", json={"text": "apa itu pecahan senilai"}, headers=sh).json()
    assert "https://" not in r["reply"] and "kelas 5" in seen["system"] and "MATERI RUJUKAN" in seen["user"]
    log = db.query(AIUsageLog).order_by(AIUsageLog.id.desc()).first()
    assert log.provider == "openai_compat" and abs(log.cost_usd - 0.003) < 1e-9

    def broken(*a, **k):
        raise RuntimeError("timeout")

    monkeypatch.setattr(providers.httpx, "post", broken)
    r2 = client.post("/v1/student/tutor/messages", json={"text": "jelaskan penjumlahan pecahan"}, headers=sh).json()
    assert r2["reply"]
    db.expire_all()
    log2 = db.query(AIUsageLog).order_by(AIUsageLog.id.desc()).first()
    assert log2.outcome == "fallback" and log2.cost_usd == 0.0
    monkeypatch.setattr(s, "ai_global_daily_cost_limit_usd", 0.001)
    called = {"n": 0}

    def counting(*a, **k):
        called["n"] += 1
        return fake_post(*a, **k)

    monkeypatch.setattr(providers.httpx, "post", counting)
    client.post("/v1/student/tutor/messages", json={"text": "tripel apa saja"}, headers=sh)
    assert called["n"] == 0
