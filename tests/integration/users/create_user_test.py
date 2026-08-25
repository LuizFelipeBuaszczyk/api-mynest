import pytest


def test_post_user(client):
    response = client.post(
        "/users/super",
        json={"username": "admin", "password": "password123", "email": "admin@admin.com"},
    )

    response = client.post(
        "/auth/login",
        json={"username": "admin", "password": "password123"},
    )
    access_token = response.json().get('access_token', None)
    headers = {"access-token": access_token}

    response = client.post(
        "/users/",
        json={"username": "testuser", "password": "password123", "email": "test@test.com"},
        headers=headers,
    )
    assert response.status_code == 200

