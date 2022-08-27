import pytest
from unittest import mock
from fastapi.testclient import TestClient
from src.repositories import UserRepository
from src.models import User
from src.main import app


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_list(client):
    repository_mock = mock.Mock(spec=UserRepository)
    repository_mock.get_all.return_value = [
        User(id=1, email="test1@email.com", hashed_password="pwd", is_active=True),
        User(id=2, email="test2@email.com", hashed_password="pwd", is_active=False),
    ]

    with app.container.user_repository.override(repository_mock):
        response = client.get("/users")

    assert response.status_code == 200
    data = response.json()
    assert data == [
        {"id": 1, "email": "test1@email.com", "hashed_password": "pwd", "is_active": True},
        {"id": 2, "email": "test2@email.com", "hashed_password": "pwd", "is_active": False},
    ]


def sample_test(client):
    assert 1 == 2