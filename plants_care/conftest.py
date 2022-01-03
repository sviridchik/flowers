import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from plants_care.factories import FertilizerFactory
from plants_care.factories import FertilizerFactory, SolutionFactory, ProblemFactory, WateringFactory, RegimeFactory


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(RegimeFactory, "regime")
register(FertilizerFactory, "fertilizer")
register(ProblemFactory, "problem")
register(SolutionFactory, "solution")
register(WateringFactory, "watering")
