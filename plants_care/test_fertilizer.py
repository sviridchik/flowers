import pytest

from plants_care.models import Fertilizer


@pytest.mark.django_db
def test_get_fert(client, fertilizer_factory):
    fertilizer_factory()
    response = client.get("/care/fertilizer/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_fert(client):
    response = client.post(
        "/care/fertilizer/",
        data={
            "description": "very good fertilizer for  flowers during flowering",
            "title": "Sodium Nitrate Calcium Nitrate ",
        },
    )
    assert response.status_code == 201
    assert len(Fertilizer.objects.all()) == 1


@pytest.mark.django_db
def test_get_fert_pk(fertilizer_factory, client):
    response = client.get(f"/care/fertilizer/{fertilizer_factory().id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_fert(fertilizer_factory, client):
    response = client.delete(f"/care/fertilizer/{fertilizer_factory().id}/")
    assert response.status_code == 204
    assert len(Fertilizer.objects.all()) == 0


# TODO: DEBUG SMTH WRONG
@pytest.mark.django_db
def test_patch_fert(fertilizer_factory, client):
    response = client.patch(
        f"/care/fertilizer/{fertilizer_factory().id}/", data={"description": "very informative description"}
    )
    assert response.status_code == 200
    assert len(Fertilizer.objects.all()) == 1
