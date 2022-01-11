import pytest

from managment.models import Profile, Rooms
from managment.serializers import ProfileSerializer, RoomSerializer


@pytest.mark.django_db
def test_get_room(client, room):
    response = client.get("/managment/rooms/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    response.json()[0]["profile"] = response.json()[0]["profile"]["username"]
    processed_room = {
        "id": str(room.id),
        "humidity_summer": room.humidity_summer,
        "humidity_winter": room.humidity_winter,
        "temp_winter": room.temp_winter,
        "temp_summer": room.temp_summer,
        "profile": str(room.profile.user.username),
    }
    assert response.json()[0] == processed_room


@pytest.mark.django_db
def test_post_room(client, user, profile):
    profile_id = profile.id
    response = client.post(
        "/managment/rooms/",
        data={
            "humidity_summer": 23,
            "humidity_winter": 12.4,
            "temp_winter": 23.23,
            "temp_summer": 33,
            "profile": Profile.objects.all()[0],
        },
    )
    assert response.status_code == 201
    assert len(Rooms.objects.all()) == 1
    # TODO to figure out why no profile in validated data
    # room = Rooms.objects.all()[0]
    # processed_room = {'id': str(room.id), 'humidity_summer': room.humidity_summer,
    #                   'humidity_winter': room.humidity_winter, 'temp_winter': room.temp_winter,
    #                   'temp_summer': room.temp_summer, 'profile': str(room.profile.id)}
    # assert response.json() == processed_room


@pytest.mark.django_db
def test_delete_room(client, room):
    response = client.delete(f"/managment/rooms/{room.id}/")
    assert response.status_code == 204
    assert len(Rooms.objects.all()) == 0


@pytest.mark.django_db
def test_patch_room(client, room):
    response = client.patch((f"/managment/rooms/{room.id}/"), data={"humidity_summer": 98.9})
    room.refresh_from_db()
    assert room.humidity_summer == 98.9
    assert response.status_code == 200
    assert len(Rooms.objects.all()) == 1
    response.json()["profile"] = str(response.json()["profile"]["username"])
    processed_room = {
        "id": str(room.id),
        "humidity_summer": room.humidity_summer,
        "humidity_winter": room.humidity_winter,
        "temp_winter": room.temp_winter,
        "temp_summer": room.temp_summer,
        "profile": str(room.profile.user.username),
    }
    assert response.json() == processed_room
