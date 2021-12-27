import pytest

from plants_care.models import Problem


@pytest.mark.django_db
def test_get_problem(client, problem_factory):
    problem_factory()
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
def test_get_problem_pk(client, problem_factory):
    response = client.get(f"/care/problems/{str(problem_factory().id)}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_problem(client, problem_factory):
    response = client.delete(f"/care/problems/{str(problem_factory().id)}/")
    assert response.status_code == 204
    assert len(Problem.objects.all()) == 0


@pytest.mark.django_db
# TODO: DEBUG SMTH WRONG
def test_patch_problem(client, problem_factory):
    response = client.patch(
        f"/care/problems/{str(problem_factory().id)}/", data={"description": "very informative "}
    )
    assert response.status_code == 200
    assert len(Problem.objects.all()) == 1
