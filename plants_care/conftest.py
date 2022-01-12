import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from plants_care.factories import (
    FertilizerFactory,
    ProblemFactory,
    RegimeFactory,
    SolutionFactory,
    WateringFactory,
)


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(RegimeFactory, "regime")
register(FertilizerFactory, "fertilizer")
register(ProblemFactory, "problem")
register(SolutionFactory, "solution")
register(WateringFactory, "watering")
