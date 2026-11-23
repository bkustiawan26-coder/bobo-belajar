from app.services.bundle import build_bundle
from tests.conftest import register, staff


def test_bundle_contains_published_content_with_keys(db):
    b = build_bundle(db)
    assert b["format"] == 1
    assert b["lessons"] and b["questions"] and b["assessments"]
    q = b["questions"][0]
    assert {"answer", "explanation", "options", "usage", "scaffold"} <= set(q)
    assert all(x["answer"].get("model") and x["answer"].get("keys") for x in b["questions"] if x["type"] == "essay")
    ids = {x["id"] for x in b["questions"]}
    assert all(x["id"] in ids for a in b["assessments"] for x in a["questions"])
    topic_ids = {t["id"] for t in b["topics"]}
    assert all(a in topic_ids and p in topic_ids for a, p in b["prerequisites"])
    assert {s["grade"] for s in b["subjects"]} == set(range(1, 10))


def test_bundle_excludes_unpublished_unless_sample_requested(db):
    from app.models import Assessment, Lesson, Question
    for model in (Lesson, Question):
        for row in db.query(model).all():
            row.status = "in_review"
    for a in db.query(Assessment).all():
        a.status = "draft"
    db.commit()
    plain = build_bundle(db)
    assert plain["lessons"] == [] and plain["questions"] == [] and plain["assessments"] == []
    with_sample = build_bundle(db, include_sample=True)
    assert with_sample["lessons"] and all(x["sample"] for x in with_sample["lessons"])
    assert with_sample["assessments"]


def test_bundle_endpoint_requires_editor(client, db):
    _, h = register(client)
    assert client.get("/v1/admin/content-bundle", headers=h).status_code == 403
    rv = staff(db, "reviewer")
    assert client.get("/v1/admin/content-bundle", headers=rv).status_code == 403
    ed = staff(db, "editor")
    r = client.get("/v1/admin/content-bundle?include_sample=true", headers=ed)
    assert r.status_code == 200 and r.json()["includes_sample"] is True
