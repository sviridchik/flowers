import pytest

from plants_base.choices import SoilTypes, BreedingTypes

data = {"name": "qwerty",
        "scientific_name": "qwerty123",
        "level_of_complexity": 3,
        "type": "succulent",
        "type_of_soil": SoilTypes.SANDY.value,
        "date_of_last_transfer": "2003-09-09",
        "description": "very interesting plant",
        "spraying": True,
        "breeding_method": BreedingTypes.DIVISION.value,
        "date_of_last_resting_state": "2021-09-09"}


@pytest.mark.django_db
def test_post_plants(client):
    response = client.post("/plants_base/plants/", data=data)
    # TODO debug(response.json())
    assert response.status_code == 200
