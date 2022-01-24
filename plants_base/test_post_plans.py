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

# TODO here in progress
@pytest.mark.django_db
def test_post_plants_succulents(client):
    response = client.post(f"/plants_base/plants/{TypeChoice.SUCCULENT.value}/plans", data=DATA_SUCCULENTS)
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
