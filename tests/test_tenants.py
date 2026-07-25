import uuid


def test_create_tenant_valid(client):
    r = client.post("/tenants", json={"name": "Leander Campus"})
    assert r.status_code == 201
    body = r.json()
    assert body["name"] == "Leander Campus"
    assert body["status"] == "active"
    assert body["franchisor_id"] is None


def test_create_tenant_missing_name_is_rejected(client):
    r = client.post("/tenants", json={})
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validation_error"


def test_get_tenant_valid(client):
    created = client.post("/tenants", json={"name": "Cedar Park Campus"}).json()

    r = client.get(f"/tenants/{created['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == created["id"]


def test_get_tenant_not_found(client):
    r = client.get(f"/tenants/{uuid.uuid4()}")
    assert r.status_code == 404
    assert r.json()["error"]["code"] == "not_found"


def test_get_tenant_invalid_id_format(client):
    r = client.get("/tenants/not-a-uuid")
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validation_error"


def test_update_tenant_partial(client):
    created = client.post("/tenants", json={"name": "Round Rock Campus"}).json()

    r = client.patch(f"/tenants/{created['id']}", json={"status": "suspended"})
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "suspended"
    assert body["name"] == "Round Rock Campus"  # untouched by the partial update


def test_update_tenant_not_found(client):
    r = client.patch(f"/tenants/{uuid.uuid4()}", json={"name": "Doesn't matter"})
    assert r.status_code == 404
