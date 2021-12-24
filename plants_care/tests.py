# Create your tests here.
import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from plants_care.factories import (
    FertilizerFactory,
    ProblemFactory,
    SolutionFactory,
    WateringFactory,
)
from plants_care.models import Fertilizer, Problem, Solution, Watering


@pytest.mark.django_db
def test_get_fert(client):
    # raise Exception(view_name)
    FertilizerFactory()
    response = client.get("/care/fertilizer/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_fert(client):
    response = client.post(
        "/care/fertilizer/",
        data={
            "description": "very good fertilizer for  flowers during flowering",
            "title": "Sodium Nitrate Calcium Nitrate ",
        },
    )
    assert response.status_code == 201
    assert len(Fertilizer.objects.all()) == 1


# f = FertilizerFactory()


# class TestFertilizerDetailView(TestCase):
#     def setUp(self) -> None:
        # self.client = APIClient()
        # self.view_name = "plants_care:fertilizer_detail"
        # self.f = FertilizerFactory()
@pytest.mark.django_db
def test_get_fert_pk(f,client):
    response = client.get("/care/fertilizer/" + str(f.id)+"/")

    # response = self.client.get(reverse(self.view_name, kwargs={"pk": self.f.id}))
    assert response.status_code == 200
@pytest.mark.django_db
def test_delete_fert(f,client):
    response = client.delete("/care/fertilizer/" + str(f.id)+"/")
    assert response.status_code == 204
    assert len(Fertilizer.objects.all()) == 0

# TODO: DEBUG SMTH WRONG
@pytest.mark.django_db
def test_patch_fert(f,client):
    response = client.patch(
        "/care/fertilizer/" + str(f.id) + "/", data={"description": "very informative description"}
    )
    assert response.status_code == 200
    assert len(Fertilizer.objects.all()) == 1



@pytest.mark.django_db
def test_get_watering(client):
    WateringFactory()
    response = client.get("/care/watering/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_watering(client):
    response = client.post(
        "/care/watering/",
        data={
            "description": "very good watering for  flowers during flowering",
            "title": "water ",
            "type": "ABOVE",
        },
    )
    assert response.status_code == 201
    assert len(Watering.objects.all()) == 1

@pytest.mark.django_db
def test_get_watering_pk(client,w):
    response = client.get(f"/care/watering/{w.id}/")
    assert response.status_code == 200
@pytest.mark.django_db
def test_delete_watering(client,w):
    response = client.delete(f"/care/watering/{w.id}/")
    assert response.status_code == 204
    assert len(Watering.objects.all()) == 0
@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_watering(client,w):
    response = client.patch(
        (f"/care/watering/{w.id}/"), data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Watering.objects.all()) == 1



@pytest.mark.django_db
def test_get_solution(client):
    SolutionFactory()
    response = client.get("/care/solutions/")
    assert response.status_code == 200
@pytest.mark.django_db
def test_post_solution(client):
    response = client.post(
        "/care/solutions/",
        data={"description": "very good solution for  flowers during flowering", "title": "to buy a new one"},
    )
    assert response.status_code == 201
    assert len(Solution.objects.all()) == 1
@pytest.mark.django_db
def test_get_solution_pk(client,s):
    response = client.get("/care/solutions/" +  str(s.id)+"/")
    assert response.status_code == 200
@pytest.mark.django_db
def test_delete_solution(client,s):
    response = client.delete("/care/solutions/" +  str(s.id)+"/")
    assert response.status_code == 204
    assert len(Solution.objects.all()) == 0

@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_solution(client,s):
    response = client.patch(
        "/care/solutions/" + str(s.id) + "/", data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Solution.objects.all()) == 1

@pytest.mark.django_db
def test_get_problem(client):
    ProblemFactory()
    response = client.get("/care/problems/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_problem(client):
    response = client.post(
        "/care/problems/",
        data={
            "description": "very good solution for  flowers during flowering",
            "title": "to buy a new one",
            "frequency": 5,
        },
    )
    assert response.status_code == 201
    assert len(Problem.objects.all()) == 1



@pytest.mark.django_db
def test_get_problem_pk(client,p):
    response = client.get("/care/problems/" + str(p.id) + "/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_problem(client,p):
    response = client.delete("/care/problems/" + str(p.id) + "/")
    assert response.status_code == 204
    assert len(Problem.objects.all()) == 0

@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_problem(client,p):
    response = client.patch(
        "/care/problems/" + str(p.id) + "/", data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Problem.objects.all()) == 1
