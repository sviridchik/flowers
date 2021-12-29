import pytest

from managment.models import Profile
from managment.factories import ProfileFactory


@pytest.mark.django_db
def test_get_user(client, profile_factory):
    profile_factory()
    response = client.get("/managment/users/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_users(client):
    response = client.post(
        (f"/managment/users/"), data={'username': 'test12345', 'password': 'test123123',
                                      'level_of_qualification': 3,
                                      'email': 'test@gmail.com'}
    )
    assert response.status_code == 201
    assert len(Profile.objects.all()) == 1


@pytest.mark.django_db
def test_get_users_pk(client, profile_factory):
    response = client.get(f"/managment/users/{profile_factory().id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_users(client, profile_factory):
    response = client.delete(f"/managment/users/{profile_factory().id}/")
    assert response.status_code == 204
    assert len(Profile.objects.all()) == 0


@pytest.mark.django_db
def test_patch_users(client, profile_factory):
    p = profile_factory()
    response = client.patch(
        (f"/managment/users/{p.id}/"), data={'level_of_qualification': 5}
    )
    p.refresh_from_db()
    assert p.level_of_qualification == 5
    assert len(Profile.objects.all()) == 1
    assert response.status_code == 200
