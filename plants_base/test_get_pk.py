import pytest

from plants_base.choices import BreedingTypes, ColorTypes, SoilTypes, TypeChoice
from plants_base.data_for_tests import DATA_FLOWERS, DATA_MICROGREEN, DATA_SUCCULENTS
from plants_base.models import Flowers, Microgreen, Succulents


@pytest.mark.django_db
def test_get_plants_succulents_pk(client, succulent):
    response = client.get(f"/plants_base/plants/{TypeChoice.SUCCULENT.value}/{succulent.id}/")
    assert response.status_code == 200
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
def test_get_plants_microgreen_pk(client, microgreen):
    response = client.get(f"/plants_base/plants/{TypeChoice.MICROGREEN.value}/{microgreen.id}/")
    assert response.status_code == 200
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
def test_get_plants_flowers_pk(client, flowers):
    response = client.get(f"/plants_base/plants/{TypeChoice.FLOWERS.value}/{flowers.id}/")
    assert response.status_code == 200
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
