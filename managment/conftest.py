import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from managment.factories import ProfileFactory, RoomFactory, UserFactory


@pytest.fixture(autouse=True)
def client():
    client = APIClient()
    return client


register(UserFactory, "user")
register(ProfileFactory, "profile")
register(RoomFactory, "room")
