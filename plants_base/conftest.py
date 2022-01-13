import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from plants_base.factories import FlowersFactory, MicrogreenFactory, SucculentFactory


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(SucculentFactory, "succulent")
register(FlowersFactory, "flowers")
register(MicrogreenFactory, "microgreen")
