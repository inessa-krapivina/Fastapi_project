from starlette.testclient import TestClient


def test_read_users(client: TestClient):
    response = client.get(url="/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
