import pytest


def test_post_password(client):
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
        "/passwords/",
        json={"name": "My Password", "description": "mysecret123", "password": "password"},
        headers=headers,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Password registered"
