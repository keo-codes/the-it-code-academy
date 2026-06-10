import importlib
import sys
from pathlib import Path

from fastapi.testclient import TestClient


ASSIGNMENT_DIR = Path(__file__).resolve().parents[1]
if str(ASSIGNMENT_DIR) not in sys.path:
    sys.path.insert(0, str(ASSIGNMENT_DIR))


def _load_main_module():
    sys.modules.pop("main", None)
    return importlib.import_module("main")


def test_get_student_enrollments_returns_saved_courses(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main = _load_main_module()
    client = TestClient(main.app)

    create_response = client.post(
        "/api/students",
        params={
            "student_id": 1,
            "first_name": "Ada",
            "last_name": "Lovelace",
            "email": "ada@example.com",
        },
    )
    assert create_response.status_code == 200

    enroll_response = client.post("/api/students/1/enroll", params={"course_id": 200})
    assert enroll_response.status_code == 200

    response = client.get("/api/students/1/enrollments")

    assert response.status_code == 200
    assert response.json() == {"student_id": 1, "courses": [200]}


def test_get_student_enrollments_returns_404_for_missing_student(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main = _load_main_module()
    client = TestClient(main.app)

    response = client.get("/api/students/999/enrollments")

    assert response.status_code == 404
    assert response.json() == {"detail": "Student with ID 999 not found"}
