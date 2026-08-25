import pytest


def test_get_role_by_id(client):
    # Create a role first
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
        "/roles/",
        json={"codename": "admin", "description": "Administrator role"},
        headers=headers,
    )

    response = client.get("/roles/1", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
