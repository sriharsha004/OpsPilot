import uuid


def _create_tenant_and_lead(client):
    tenant = client.post("/tenants", json={"name": "Leander Campus"}).json()
    lead = client.post(
        f"/tenants/{tenant['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    ).json()
    return tenant, lead


def test_create_task_valid(client):
    tenant, lead = _create_tenant_and_lead(client)

    r = client.post(
        f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks",
        json={"title": "Call the lead"},
    )
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == "Call the lead"
    assert body["status"] == "open"
    assert body["priority"] == "medium"
    assert body["tenant_id"] == tenant["id"]
    assert body["lead_id"] == lead["id"]


def test_create_task_missing_title_is_rejected(client):
    tenant, lead = _create_tenant_and_lead(client)

    r = client.post(f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks", json={})
    assert r.status_code == 422


def test_create_task_rejects_unknown_lead(client):
    tenant, _ = _create_tenant_and_lead(client)

    r = client.post(
        f"/tenants/{tenant['id']}/leads/{uuid.uuid4()}/tasks",
        json={"title": "Call the lead"},
    )
    assert r.status_code == 404


def test_list_tasks_for_lead(client):
    tenant, lead = _create_tenant_and_lead(client)
    client.post(f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks", json={"title": "Task 1"})
    client.post(f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks", json={"title": "Task 2"})

    r = client.get(f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks")
    assert r.status_code == 200
    assert len(r.json()) == 2


def test_update_task_to_done_sets_completed_at(client):
    tenant, lead = _create_tenant_and_lead(client)
    task = client.post(
        f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks", json={"title": "Call the lead"}
    ).json()
    assert task["completed_at"] is None

    r = client.patch(
        f"/tenants/{tenant['id']}/leads/{lead['id']}/tasks/{task['id']}",
        json={"status": "done"},
    )
    assert r.status_code == 200
    assert r.json()["status"] == "done"
    assert r.json()["completed_at"] is not None


def test_get_task_cross_tenant_returns_404(client):
    tenant_a, lead_a = _create_tenant_and_lead(client)
    tenant_b, _ = _create_tenant_and_lead(client)
    task = client.post(
        f"/tenants/{tenant_a['id']}/leads/{lead_a['id']}/tasks", json={"title": "Call the lead"}
    ).json()

    r = client.get(f"/tenants/{tenant_b['id']}/leads/{lead_a['id']}/tasks/{task['id']}")
    assert r.status_code == 404
