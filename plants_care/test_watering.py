import pytest

from plants_care.models import Watering
from plants_care.serializers import WateringSerializer


@pytest.mark.django_db
def test_get_watering(client, watering):
    response = client.get("/care/watering/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    response.json()[0]["type"] = response.json()[0]["type"].split(".")[-1]
    processed_watering = {
        "id": str(watering.id),
        "type": watering.type.name,
        "description": watering.description,
        "regime": watering.regime,
    }
    if processed_watering["regime"] is not None:
        processed_watering["regime"] = str(processed_watering["regime"].id)
    assert response.json()[0] == processed_watering


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
    watering = Watering.objects.all()[0]
    response.json()["type"] = response.json()["type"].split(".")[-1]
    processed_watering = {
        "id": str(watering.id),
        "type": watering.type,
        "description": watering.description,
        "regime": watering.regime,
    }
    if processed_watering["regime"] is not None:
        processed_watering["regime"] = str(processed_watering["regime"].id)
    assert response.json() == processed_watering


@pytest.mark.django_db
def test_get_watering_pk(client, watering):
    response = client.get(f"/care/watering/{watering.id}/")
    assert response.status_code == 200
    response.json()["type"] = response.json()["type"].split(".")[-1]
    processed_watering = {
        "id": str(watering.id),
        "type": watering.type.name,
        "description": watering.description,
        "regime": watering.regime,
    }
    if processed_watering["regime"] is not None:
        processed_watering["regime"] = str(processed_watering["regime"].id)
    assert response.json() == processed_watering


@pytest.mark.django_db
def test_delete_watering(client, watering):
    response = client.delete(f"/care/watering/{watering.id}/")
    assert response.status_code == 204
    assert len(Watering.objects.all()) == 0


@pytest.mark.django_db
def test_patch_watering(client, watering):
    response = client.patch((f"/care/watering/{watering.id}/"), data={"description": "very informative"})
    watering.refresh_from_db()
    assert watering.description == "very informative"
    assert response.status_code == 200
    assert len(Watering.objects.all()) == 1
    processed_watering = {
        "id": str(watering.id),
        "type": watering.type,
        "description": watering.description,
        "regime": watering.regime,
    }
    if processed_watering["regime"] is not None:
        processed_watering["regime"] = str(processed_watering["regime"].id)
    assert response.json() == processed_watering
