import pytest

from managment.factories import ProfileFactory
from managment.models import Profile


@pytest.mark.django_db
def test_get_user(client, profile):
    response = client.get("/managment/users/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {
        "email": profile.user.email,
        "level_of_qualification": profile.level_of_qualification,
        "username": profile.user.username,
        "password": response.json()[0]["password"],
    }


@pytest.mark.django_db
def test_post_users(client):
    response = client.post(
        (f"/managment/users/"),
        data={
            "username": "test12345",
            "password": "test123123",
            "level_of_qualification": 3,
            "email": "test@gmail.com",
        },
    )
    assert response.status_code == 201
    assert len(Profile.objects.all()) == 1
    assert response.json() == {
        "username": "test12345",
        "level_of_qualification": 3,
        "email": "test@gmail.com",
        "password": response.json()["password"],
    }


@pytest.mark.django_db
def test_get_users_pk(client, profile):
    response = client.get(f"/managment/users/{profile.id}/")
    assert response.status_code == 200
    assert response.json() == {
        "email": profile.user.email,
        "level_of_qualification": profile.level_of_qualification,
        "username": profile.user.username,
        "password": response.json()["password"],
    }


@pytest.mark.django_db
def test_delete_users(client, profile):
    response = client.delete(f"/managment/users/{profile.id}/")
    assert response.status_code == 204
    assert len(Profile.objects.all()) == 0


@pytest.mark.django_db
def test_patch_users(client, profile):
    response = client.patch((f"/managment/users/{profile.id}/"), data={"level_of_qualification": 5})
    profile.refresh_from_db()
    profile.user.refresh_from_db()
    assert Profile.objects.all()[0].level_of_qualification == 5
    assert profile.level_of_qualification == 5
    assert len(Profile.objects.all()) == 1
    assert response.status_code == 200
