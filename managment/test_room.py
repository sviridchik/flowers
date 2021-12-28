import pytest

from managment.models import Rooms
from managment.serializers import ProfileSerializer


@pytest.mark.django_db
def test_get_room(client, room_factory):
    room_factory()
    response = client.get("/managment/rooms/")
    assert response.status_code == 200


#
# TODO integrity error
# @pytest.mark.django_db
# def test_post_room(client,profile_factory):
#     p = profile_factory()
#     # raise Exception(p)
#     response = client.post(
#         "/managment/rooms/",
#         data={"humidity_summer": 23,
#               "humidity_winter": 12.4,
#               "temp_winter": 23.23,
#               "temp_summer": 33,
#               "profile": p}
#     )
#     assert response.status_code == 201
#     assert len(Rooms.objects.all()) == 1
#
#

@pytest.mark.django_db
def test_get_room_pk(client, room_factory):
    response = client.get(f"/managment/rooms/{room_factory().id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_room(client, room_factory):
    response = client.delete(f"/managment/rooms/{room_factory().id}/")
    assert response.status_code == 204
    assert len(Rooms.objects.all()) == 0


@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_room(client, room_factory):
    response = client.patch(
        (f"/managment/rooms/{room_factory().id}/"), data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Rooms.objects.all()) == 1
