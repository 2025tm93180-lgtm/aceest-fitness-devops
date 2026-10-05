import pytest
from app import app, clients


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        clients.clear()
        yield client


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "ACEest Fitness & Gym"
    assert data["status"] == "running"


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


def test_get_clients_empty(client):
    response = client.get("/clients")

    assert response.status_code == 200
    assert response.get_json() == []


def test_add_client(client):
    response = client.post(
        "/clients",
        json={
            "name": "Rahul",
            "age": 25,
            "height": 175,
            "weight": 75,
            "program": "Muscle Gain"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Rahul"
    assert data["age"] == 25
    assert data["program"] == "Muscle Gain"


def test_add_client_without_name(client):
    response = client.post(
        "/clients",
        json={
            "age": 25
        }
    )

    assert response.status_code == 400


def test_get_client(client):
    client.post(
        "/clients",
        json={
            "name": "Priya",
            "age": 24
        }
    )

    response = client.get("/clients/1")

    assert response.status_code == 200

    data = response.get_json()

    assert data["name"] == "Priya"


def test_get_nonexistent_client(client):
    response = client.get("/clients/999")

    assert response.status_code == 404


def test_get_programs(client):
    response = client.get("/programs")

    assert response.status_code == 200

    data = response.get_json()

    assert "Fat Loss" in data
    assert "Muscle Gain" in data
    assert "Beginner" in data
