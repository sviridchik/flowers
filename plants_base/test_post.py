import pytest

from plants_base.choices import TypeChoice
from plants_base.data_for_tests import (
    DATA_FLOWERS,
    DATA_MICROGREEN,
    DATA_MICROGREEN_VALIDATION_FUNC,
    DATA_MICROGREEN_VALIDATORS,
    DATA_SUCCULENTS,
    DATA_SUCCULENTS_VALIDATORS_OBJECT_LEVEL,
)
from plants_base.models import Flowers, Microgreen, Succulents


@pytest.mark.django_db
def test_post_plants_succulents(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.SUCCULENT.value}/", data=DATA_SUCCULENTS)
    assert response.status_code == 201
    assert len(Succulents.objects.all()) == 1
    assert len(Flowers.objects.all()) == 0
    assert len(Microgreen.objects.all()) == 0
    assert response.json() == {
        "date_of_last_resting_state": "2021-09-09",
        "id": Succulents.objects.all()[0].id,
        "name": "qwerty",
        "scientific_name": "qwerty123",
        "level_of_complexity": 3.0,
        "type_of_soil": "SANDY",
        "date_of_last_transfer": "2003-09-09",
        "description": "very interesting plant",
        "spraying": True,
        "type_of_watering": None,
        "breeding_method": "DIVISION",
    }


@pytest.mark.django_db
def test_post_plants_succulents_check_validators_object_level(client):
    response = client.post(
        f"/plants_base/plants/{TypeChoice.SUCCULENT.value}/", data=DATA_SUCCULENTS_VALIDATORS_OBJECT_LEVEL
    )
    assert response.status_code == 400
    assert len(Succulents.objects.all()) == 0
    assert len(Flowers.objects.all()) == 0
    assert len(Microgreen.objects.all()) == 0


@pytest.mark.django_db
def test_post_plants_microgreen(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.MICROGREEN.value}/", data=DATA_MICROGREEN)
    assert response.status_code == 201
    assert len(Microgreen.objects.all()) == 1
    assert len(Flowers.objects.all()) == 0
    assert len(Succulents.objects.all()) == 0
    assert response.json() == {
        "benifit_for_health": "Vitamin A,C",
        "date_of_harvest": "2022-09-09",
        "id": Microgreen.objects.all()[0].pk,
        "name": "qwerty",
        "scientific_name": "qwerty123",
        "level_of_complexity": 3.0,
        "type_of_soil": "SANDY",
        "date_of_last_transfer": "2003-09-09",
        "description": "very interesting plant",
        "spraying": True,
        "type_of_watering": None,
        "breeding_method": "DIVISION",
    }


@pytest.mark.django_db
def test_post_plants_microgreen_check_validators(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.MICROGREEN.value}/", data=DATA_MICROGREEN_VALIDATORS)
    assert response.status_code == 400
    assert len(Microgreen.objects.all()) == 0
    assert len(Flowers.objects.all()) == 0
    assert len(Succulents.objects.all()) == 0


@pytest.mark.django_db
def test_post_plants_microgreen_check_validators_func(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.MICROGREEN.value}/", data=DATA_MICROGREEN_VALIDATION_FUNC)
    assert response.status_code == 400
    assert len(Microgreen.objects.all()) == 0
    assert len(Flowers.objects.all()) == 0
    assert len(Succulents.objects.all()) == 0


@pytest.mark.django_db
def test_post_plants_flowers(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.FLOWERS.value}/", data=DATA_FLOWERS)
    assert response.status_code == 201
    assert len(Flowers.objects.all()) == 1
    assert len(Microgreen.objects.all()) == 0
    assert len(Succulents.objects.all()) == 0
    assert response.json() == {
        "color": "YELLOW",
        "last_date_of_blossom": "2022-09-09",
        "id": Flowers.objects.all()[0].pk,
        "name": "qwerty",
        "scientific_name": "qwerty123",
        "level_of_complexity": 3.0,
        "type_of_soil": "SANDY",
        "date_of_last_transfer": "2003-09-09",
        "description": "very interesting plant",
        "spraying": True,
        "type_of_watering": None,
        "breeding_method": "DIVISION",
    }
