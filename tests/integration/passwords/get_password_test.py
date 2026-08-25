import pytest


def test_get_password_by_id(client):
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

    create_response = client.post(
        "/passwords/",
        json={"name": "My Password", "description": "mysecret123", "password": "password"},
        headers=headers,
    )

    response = client.get("/passwords/1", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
