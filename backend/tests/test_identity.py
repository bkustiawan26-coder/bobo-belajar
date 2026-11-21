from tests.conftest import add_child, register


def test_register_requires_consent(client):
    r = client.post("/v1/auth/register", json={"email": "a@contoh.id", "password": "rahasia-kuat-1", "display_name": "Ayah", "accept_privacy_policy": True, "accept_child_data_processing": False})
    assert r.status_code == 422


def test_login_and_wrong_password(client):
    register(client, "b@contoh.id")
    assert client.post("/v1/auth/login", json={"email": "b@contoh.id", "password": "salah-sekali"}).status_code == 401
    r = client.post("/v1/auth/login", json={"email": "B@contoh.id", "password": "rahasia-kuat-1"})
    assert r.status_code == 200 and r.json()["has_pin"] is True


def test_refresh_requires_pin_and_locks(client):
    tok, _ = register(client, "c@contoh.id")
    assert client.post("/v1/auth/refresh", json={"refresh_token": tok["refresh_token"]}).status_code == 401
    assert client.post("/v1/auth/refresh", json={"refresh_token": tok["refresh_token"], "pin": "2468"}).status_code == 200
    for _ in range(5):
        client.post("/v1/auth/refresh", json={"refresh_token": tok["refresh_token"], "pin": "0000"})
    assert client.post("/v1/auth/refresh", json={"refresh_token": tok["refresh_token"], "pin": "2468"}).status_code == 423


def test_parent_sees_only_own_children(client):
    _, h1 = register(client)
    _, h2 = register(client)
    cid, _ = add_child(client, h1)
    assert len(client.get("/v1/parent/children", headers=h2).json()["children"]) == 0
    assert client.get(f"/v1/parent/children/{cid}/dashboard", headers=h2).status_code == 404
    assert client.post("/v1/auth/child-session", json={"child_id": cid}, headers=h2).status_code == 404


def test_student_token_cannot_use_parent_endpoints(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    assert client.get("/v1/parent/children", headers=sh).status_code == 403
    assert client.get(f"/v1/parent/children/{cid}/dashboard", headers=sh).status_code == 403
    assert client.get("/v1/admin/stats", headers=sh).status_code == 403


def test_child_nickname_rejects_digits_and_limit(client):
    _, h = register(client)
    assert client.post("/v1/parent/children", json={"nickname": "Budi08123", "grade": 3}, headers=h).status_code == 422
    for i, n in enumerate(["Ana", "Bima", "Caca", "Dodi", "Eka", "Fafa"]):
        assert client.post("/v1/parent/children", json={"nickname": n, "grade": 1 + i}, headers=h).status_code == 201
    assert client.post("/v1/parent/children", json={"nickname": "Gita", "grade": 2}, headers=h).status_code == 409


def test_delete_child_revokes_student_token(client):
    _, h = register(client)
    cid, sh = add_child(client, h)
    assert client.get("/v1/student/me", headers=sh).status_code == 200
    assert client.delete(f"/v1/parent/children/{cid}", headers=h).status_code == 200
    assert client.get("/v1/student/me", headers=sh).status_code == 401


def test_export_and_delete_account(client):
    tok, h = register(client, "d@contoh.id")
    add_child(client, h)
    data = client.get("/v1/parent/export", headers=h).json()
    assert data["children"][0]["nickname"] == "Nadia"
    assert client.post("/v1/parent/delete-account", json={"password": "rahasia-kuat-1", "confirm": "HAPUS"}, headers=h).status_code == 200
    assert client.post("/v1/auth/login", json={"email": "d@contoh.id", "password": "rahasia-kuat-1"}).status_code == 401
