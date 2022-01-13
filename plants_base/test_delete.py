import pytest

from plants_base.choices import BreedingTypes, ColorTypes, SoilTypes, TypeChoice
from plants_base.data_for_tests import DATA_FLOWERS, DATA_MICROGREEN, DATA_SUCCULENTS
from plants_base.models import Flowers, Microgreen, Succulents


@pytest.mark.django_db
def test_delete_plants_succulents_pk(client, succulent):
    response = client.delete(f"/plants_base/plants/{TypeChoice.SUCCULENT.value}/{succulent.id}/")
    assert response.status_code == 204



@pytest.mark.django_db
def test_delete_plants_microgreen(client, microgreen):
    response = client.delete(f"/plants_base/plants/{TypeChoice.MICROGREEN.value}/{microgreen.id}/")
    assert response.status_code == 204



@pytest.mark.django_db
def test_delete_plants_flowers(client, flowers):
    response = client.delete(f"/plants_base/plants/{TypeChoice.FLOWERS.value}/{flowers.id}/")
    assert response.status_code == 204

