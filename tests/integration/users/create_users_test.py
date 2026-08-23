import pytest

def test_post_super_user(client):
    response = client.post(
        "/users/super",
        json={"username": "admin", "password": "password123", "email": "admin@mynest.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "admin"
    assert data["is_superuser"] is True

