from fastapi.testclient import TestClient

from university.app import app


client = TestClient(app)


class TestLectureApi:
    def test_create_delete_lecture(self, create_fake_group):
        group_id = create_fake_group.id
        create_response = client.post(
            "/lectures/",
            json={
                "date": "2021-11-01",
                "lesson": "math",
                "group_id": group_id
            },
        )

        if create_response.ok:
            created_lecture_id = create_response.json()["id"]
            delete_response = client.delete(
                f"/lectures/{created_lecture_id}",
            )
            assert delete_response.status_code == 204
            assert client.get(f"/lectures/{created_lecture_id}").status_code == 404

    def test_get_lecture(self, create_fake_lecture):
        response = client.get(
            f"/lectures/{create_fake_lecture.id}",
        )
        assert response.status_code == 200
        assert response.json()["lesson"] == "biology"

    def test_update_lecture(self, create_fake_lecture):
        lecture = create_fake_lecture
        response = client.put(
            f"/lectures/{lecture.id}",
            json={
                "date": "2021-11-01",
                "lesson": "math",
                "group_id": lecture.group_id
            },
        )
        assert response.status_code == 200
        assert response.json()["lesson"] == "math"
        assert response.json()["group_id"] == lecture.group_id
