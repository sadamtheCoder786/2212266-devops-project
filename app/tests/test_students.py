def test_create_student(client):
    payload = {"name": "Ali Hassan", "reg_no": "F21-001", "course": "CS"}
    response = client.post("/students", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["reg_no"] == "F21-001"
    assert "id" in data


def test_list_students(client):
    client.post("/students", json={"name": "Sara Khan", "reg_no": "F21-002", "course": "IT"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_student_by_reg_no(client):
    client.post("/students", json={"name": "Umar Farooq", "reg_no": "F21-003", "course": "SE"})
    response = client.get("/students/F21-003")
    assert response.status_code == 200
    assert response.json()["name"] == "Umar Farooq"


def test_student_not_found(client):
    response = client.get("/students/DOESNOTEXIST")
    assert response.status_code == 404