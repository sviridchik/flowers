import pytest

from managment.models import Rooms, Profile
from managment.serializers import ProfileSerializer, RoomSerializer


@pytest.mark.django_db
def test_get_room(client):
    response = client.get("/managment/rooms/")
    assert response.status_code == 200


#
# TODO integrity error
@pytest.mark.django_db
def test_post_room(client, profile):
    profile_id = profile.id

    response = client.post(
        "/managment/rooms/",
        data={"humidity_summer": 23,
              "humidity_winter": 12.4,
              "temp_winter": 23.23,
              "temp_summer": 33,
              "profile": profile_id}
    )
    assert response.status_code == 201
    assert len(Rooms.objects.all()) == 1


@pytest.mark.django_db
def test_delete_room(client, room):
    response = client.delete(f"/managment/rooms/{room.id}/")
    assert response.status_code == 204
    assert len(Rooms.objects.all()) == 0


@pytest.mark.django_db
def test_patch_room(client, room):
    response = client.patch(
        (f"/managment/rooms/{room.id}/"), data={"humidity_summer": 98.9}
    )
    room.refresh_from_db()
    assert room.humidity_summer == 98.9
    assert response.status_code == 200
    assert len(Rooms.objects.all()) == 1
