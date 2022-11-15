import pytest
from starlette.testclient import TestClient
from src.server import app


def test_read_users(client: TestClient):
    response = client.get(url="/")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
