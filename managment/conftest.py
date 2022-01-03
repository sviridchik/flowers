import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from managment.factories import RoomFactory, ProfileFactory, UserFactory


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(UserFactory, "user")
register(RoomFactory, "room")
register(ProfileFactory, "profile")
