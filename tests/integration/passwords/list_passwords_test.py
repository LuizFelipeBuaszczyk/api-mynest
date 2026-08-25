import pytest


def test_get_list_passwords(client):
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

    response = client.get("/passwords/", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["data"], list)