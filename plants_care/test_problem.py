import pytest

from plants_care.models import Problem
from plants_care.serializers import ProblemSerializer


@pytest.mark.django_db
def test_get_problem(client, problem):
    response = client.get("/care/problems/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0] == {"id": str(problem.id), "description": problem.description, "title": problem.title}


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
    problem = Problem.objects.all()[0]
    assert response.json() == {"id": str(problem.id), "description": problem.description, "title": problem.title}


@pytest.mark.django_db
def test_get_problem_pk(client, problem):
    response = client.get(f"/care/problems/{problem.id}/")
    assert response.status_code == 200
    assert response.json() == {"id": str(problem.id), "description": problem.description, "title": problem.title}


@pytest.mark.django_db
def test_delete_problem(client, problem):
    response = client.delete(f"/care/problems/{problem.id}/")
    assert response.status_code == 204
    assert len(Problem.objects.all()) == 0


@pytest.mark.django_db
def test_patch_problem(client, problem):
    response = client.patch(f"/care/problems/{problem.id}/", data={"description": "very informative"})
    problem.refresh_from_db()

    assert problem.description == "very informative"
    assert response.status_code == 200
    assert len(Problem.objects.all()) == 1
    assert response.json() == {"id": str(problem.id), "description": problem.description, "title": problem.title}
