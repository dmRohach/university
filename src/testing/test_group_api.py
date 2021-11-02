from fastapi.testclient import TestClient

from university.app import app


client = TestClient(app)


class TestGroupApi:
    def test_get_group(self, create_fake_group):
        response = client.get(
            f"/groups/{create_fake_group.id}",
        )
        assert response.status_code == 200
        assert response.json()["number"] == 777

    def test_update_group(self, create_fake_group):
        response = client.put(
            f"/groups/{create_fake_group.id}",
            json={
                "number": "1488",
            },
        )
        assert response.status_code == 200
        assert response.json()["number"] == 1488
    
    def test_create_delete_group(self):
        create_response = client.post(
            "/groups/",
            json={
                "number": 666,
            },
        )
        assert create_response.status_code == 200
        assert create_response.json()["number"] == 666

        if create_response.ok:
            created_group_id = create_response.json()["id"]
            delete_response = client.delete(
                f"/groups/{created_group_id}",
            )
            assert delete_response.status_code == 204
            assert client.get(f"/groups/{created_group_id}").status_code == 404
