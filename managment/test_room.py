import pytest

from managment.models import Rooms


@pytest.mark.django_db
def test_get_solution(client, room_factory):
    room_factory()
    response = client.get("/managment/rooms/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_solution(client):
    response = client.post(
        "/managment/rooms/",
        data={"humidity_summer": 23,
              "humidity_winter": 12.4,
              "temp_winter": 23.23,
              "temp_summer": 33}
    )
    assert response.status_code == 201
    assert len(Rooms.objects.all()) == 1
