import pytest

from plants_care.models import Fertilizer
from plants_care.serializers import FertilizerSerializer


@pytest.mark.django_db
def test_get_fert(client, fertilizer):
    response = client.get("/care/fertilizer/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    processed_fertilizer = {
        "id": str(fertilizer.id),
        "description": fertilizer.description,
        "title": fertilizer.title,
        "regime": str(fertilizer.regime.id),
    }
    assert response.json()[0] == processed_fertilizer


@pytest.mark.skip(reason="for now")
@pytest.mark.django_db
def test_post_fert(client):
    response = client.post(
        "/care/fertilizer/",
        data={
            "description": "very good fertilizer for  flowers during flowering",
            "title": "Sodium Nitrate Calcium Fe",
        },
    )
    assert response.status_code == 201
    assert len(Fertilizer.objects.all()) == 1
    fertilizer = Fertilizer.objects.all()[0]
    processed_fertilizer = {
        "id": str(fertilizer.id),
        "description": fertilizer.description,
        "title": fertilizer.title,
        "regime": fertilizer.regime,
    }
    if processed_fertilizer["regime"] is not None:
        processed_fertilizer["regime"] = str(processed_fertilizer["regime"])
    assert response.json() == processed_fertilizer


@pytest.mark.django_db
def test_get_fert_pk(fertilizer, client):
    response = client.get(f"/care/fertilizer/{fertilizer.id}/")
    assert response.status_code == 200
    processed_fertilizer = {
        "id": str(fertilizer.id),
        "description": fertilizer.description,
        "title": fertilizer.title,
        "regime": str(fertilizer.regime.id),
    }
    assert response.json() == processed_fertilizer


@pytest.mark.django_db
def test_delete_fert(fertilizer, client):
    response = client.delete(f"/care/fertilizer/{fertilizer.id}/")
    assert response.status_code == 204
    assert len(Fertilizer.objects.all()) == 0


@pytest.mark.django_db
def test_patch_fert(fertilizer, client):
    response = client.patch(f"/care/fertilizer/{fertilizer.id}/", data={"description": "very informative description"})
    fertilizer.refresh_from_db()
    assert fertilizer.description == "very informative description"
    assert response.status_code == 200
    assert len(Fertilizer.objects.all()) == 1
    processed_fertilizer = {
        "id": str(fertilizer.id),
        "description": fertilizer.description,
        "title": fertilizer.title,
        "regime": str(fertilizer.regime.id),
    }
    assert response.json() == processed_fertilizer
