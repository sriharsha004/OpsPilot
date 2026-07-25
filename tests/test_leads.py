import uuid


def _create_tenant(client, name="Leander Campus"):
    return client.post("/tenants", json={"name": name}).json()


def test_create_lead_valid(client):
    tenant = _create_tenant(client)

    r = client.post(
        f"/tenants/{tenant['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form", "email": "jane@example.com"},
    )
    assert r.status_code == 201
    body = r.json()
    assert body["tenant_id"] == tenant["id"]
    assert body["status"] == "new"


def test_create_lead_missing_source_is_rejected(client):
    tenant = _create_tenant(client)

    r = client.post(f"/tenants/{tenant['id']}/leads", json={"name": "Jane Doe"})
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validation_error"


def test_create_lead_rejects_unknown_tenant(client):
    r = client.post(
        f"/tenants/{uuid.uuid4()}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    )
    assert r.status_code == 404
    assert r.json()["error"]["code"] == "not_found"


def test_create_lead_ignores_client_supplied_tenant_id(client):
    tenant = _create_tenant(client)
    other_tenant_id = str(uuid.uuid4())

    r = client.post(
        f"/tenants/{tenant['id']}/leads",
        json={
            "name": "Jane Doe",
            "source": "website_form",
            "tenant_id": other_tenant_id,  # not a real field on LeadCreate - must be ignored
        },
    )
    assert r.status_code == 201
    # the lead belongs to the tenant in the URL, never the one smuggled into the body
    assert r.json()["tenant_id"] == tenant["id"]


def test_get_lead_valid(client):
    tenant = _create_tenant(client)
    lead = client.post(
        f"/tenants/{tenant['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    ).json()

    r = client.get(f"/tenants/{tenant['id']}/leads/{lead['id']}")
    assert r.status_code == 200
    assert r.json()["id"] == lead["id"]


def test_get_lead_cross_tenant_returns_404_not_403(client):
    tenant_a = _create_tenant(client, "Tenant A")
    tenant_b = _create_tenant(client, "Tenant B")
    lead = client.post(
        f"/tenants/{tenant_a['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    ).json()

    # lead exists, but under tenant_a - requesting it via tenant_b must look identical
    # to "doesn't exist at all", per authorization_rules.md rule 9
    r = client.get(f"/tenants/{tenant_b['id']}/leads/{lead['id']}")
    assert r.status_code == 404
    assert r.json()["error"]["code"] == "not_found"


def test_update_lead_valid(client):
    tenant = _create_tenant(client)
    lead = client.post(
        f"/tenants/{tenant['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    ).json()

    r = client.patch(f"/tenants/{tenant['id']}/leads/{lead['id']}", json={"status": "contacted"})
    assert r.status_code == 200
    assert r.json()["status"] == "contacted"


def test_update_lead_cross_tenant_not_found(client):
    tenant_a = _create_tenant(client, "Tenant A")
    tenant_b = _create_tenant(client, "Tenant B")
    lead = client.post(
        f"/tenants/{tenant_a['id']}/leads",
        json={"name": "Jane Doe", "source": "website_form"},
    ).json()

    r = client.patch(
        f"/tenants/{tenant_b['id']}/leads/{lead['id']}", json={"status": "contacted"}
    )
    assert r.status_code == 404
