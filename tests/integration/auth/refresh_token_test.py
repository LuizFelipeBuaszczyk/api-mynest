import pytest

def test_post_refresh_token(client):
    client.post(
        "/users/super",
        json={"username": "admin", "password": "password123", "email": "admin@admin.com"},
    )

    response = client.post(
        "/auth/login",
        json={"username": "admin", "password": "password123"},
    )
    refresh_token = response.json().get('refresh_token', None)

    response = client.post(
        "/auth/refresh-token",
        json={"refresh_token": refresh_token},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
