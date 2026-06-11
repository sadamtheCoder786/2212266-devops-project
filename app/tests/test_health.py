def test_health_status(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_health_has_student_key(client):
    data = client.get("/health").json()
    assert "student" in data


def test_health_status_is_ok(client):
    data = client.get("/health").json()
    assert data["status"] == "ok"