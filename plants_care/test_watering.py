import pytest

from plants_care.models import Watering


@pytest.mark.django_db
def test_get_watering(client, watering_factory):
    watering_factory()
    response = client.get("/care/watering/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_watering(client):
    response = client.post(
        "/care/watering/",
        data={
            "description": "very good watering for  flowers during flowering",
            "title": "water ",
            "type": "ABOVE",
        },
    )
    assert response.status_code == 201
    assert len(Watering.objects.all()) == 1


@pytest.mark.django_db
def test_get_watering_pk(client, watering_factory):
    response = client.get(f"/care/watering/{watering_factory().id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_watering(client, watering_factory):
    response = client.delete(f"/care/watering/{watering_factory().id}/")
    assert response.status_code == 204
    assert len(Watering.objects.all()) == 0


@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_watering(client, watering_factory):
    response = client.patch(
        (f"/care/watering/{watering_factory().id}/"), data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Watering.objects.all()) == 1
