import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_returns_200(client):
    res = client.get("/")
    assert res.status_code == 200

def test_home_message(client):
    res = client.get("/")
    data = res.get_json()
    assert data["status"] == "running"

def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "healthy"
