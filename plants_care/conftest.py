import pytest
from rest_framework.test import APIClient
from plants_care.factories import FertilizerFactory,SolutionFactory,ProblemFactory,WateringFactory
from pytest_factoryboy import register
from plants_care.factories import FertilizerFactory

@pytest.fixture(autouse = True)
def client():
    client = APIClient()
    return client

@pytest.fixture()
def f():
    return FertilizerFactory()

@pytest.fixture()
def p():
    return ProblemFactory()

@pytest.fixture()
def s():
    return SolutionFactory()

@pytest.fixture()
def w():
    return WateringFactory()

# TODO neme is not defined whateever I do ???????????
register(FertilizerFactory)
