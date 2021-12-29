from django.test import TestCase

import pytest

from plants_care.models import Fertilizer



@pytest.mark.django_db
def test_post_plants(client):
    response = client.post("/plants_base/plants/",data={"name":"qwerty","scientific_name":"qwerty123","level_of_complexity":3})
    assert response.status_code == 200
