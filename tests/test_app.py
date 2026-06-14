from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_delete_participant_removes_student_from_activity():
    activity_name = "Chess Club"
    email = "student@example.edu"

    client.post(f"/activities/{activity_name}/signup?email={email}")

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]


def test_delete_participant_returns_404_for_missing_activity():
    response = client.delete("/activities/Does Not Exist/participants/test@example.edu")

    assert response.status_code == 404
