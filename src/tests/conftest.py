from pytest import fixture
from starlette.testclient import TestClient

from src.main import app


@fixture(scope="session")
def server_test() -> TestClient:
    with TestClient(app) as client:
        yield client
