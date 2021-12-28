import pytest
from rest_framework.test import APIClient
from managment.factories import RoomFactory, ProfileFactory
from pytest_factoryboy import register


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(RoomFactory)
register(ProfileFactory)
