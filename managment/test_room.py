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
from managment.serializers import RoomSerializer


@pytest.mark.django_db
def test_get_room(client, room):
    response = client.get("/managment/rooms/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    processed_room = {'id': str(room.id), 'humidity_summer': room.humidity_summer,
                      'humidity_winter': room.humidity_winter, 'temp_winter': room.temp_winter,
                      'temp_summer': room.temp_summer, 'profile': str(room.profile.id)}
    assert response.json()[0] == processed_room


@pytest.mark.django_db
def test_post_room(client, profile):
    profile_id = profile.id

    response = client.post(
        "/managment/rooms/",
        data={
            "humidity_summer": 23,
            "humidity_winter": 12.4,
            "temp_winter": 23.23,
            "temp_summer": 33,
            "profile": profile_id,
        },
    )
    assert response.status_code == 201
    assert len(Rooms.objects.all()) == 1
    room = Rooms.objects.all()[0]
    processed_room = {'id': str(room.id), 'humidity_summer': room.humidity_summer,
                      'humidity_winter': room.humidity_winter, 'temp_winter': room.temp_winter,
                      'temp_summer': room.temp_summer, 'profile': str(room.profile.id)}
    assert response.json() == processed_room


@pytest.mark.django_db
def test_delete_room(client, room):
    response = client.delete(f"/managment/rooms/{room.id}/")
    assert response.status_code == 204
    assert len(Rooms.objects.all()) == 0


@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_room(client, room):
    response = client.patch((f"/managment/rooms/{room.id}/"), data={"humidity_summer": 98.9})
    room.refresh_from_db()
    assert room.humidity_summer == 98.9
    assert response.status_code == 200
    assert len(Rooms.objects.all()) == 1
    processed_room = {'id': str(room.id), 'humidity_summer': room.humidity_summer,
                      'humidity_winter': room.humidity_winter, 'temp_winter': room.temp_winter,
                      'temp_summer': room.temp_summer, 'profile': str(room.profile.id)}
    assert response.json() == processed_room
