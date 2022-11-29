from starlette.testclient import TestClient


def test_read_users(server_test: TestClient):
    response = server_test.get(url="/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
