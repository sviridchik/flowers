import pytest
from rest_framework.test import APIClient
from plants_care.factories import FertilizerFactory, SolutionFactory, ProblemFactory, WateringFactory
from pytest_factoryboy import register
from plants_care.factories import FertilizerFactory


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(FertilizerFactory, name="fertilizer_factory")
register(ProblemFactory)
register(SolutionFactory)
register(WateringFactory)
