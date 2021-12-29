import pytest

from plants_care.models import Solution


@pytest.mark.django_db
def test_get_solution(client, solution_factory):
    solution_factory()
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
def test_get_solution_pk(client, solution_factory):
    response = client.get(f"/care/solutions/{solution_factory().id}/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_solution(client, solution_factory):
    response = client.delete(f"/care/solutions/{solution_factory().id}/")
    assert response.status_code == 204
    assert len(Solution.objects.all()) == 0


@pytest.mark.django_db
def test_patch_solution(client, solution_factory):
    s = solution_factory()
    response = client.patch(
        f"/care/solutions/{s.id}/", data={"description": "very informative"}
    )
    s.refresh_from_db()
    assert s.description == "very informative"
    assert response.status_code == 200
    assert len(Solution.objects.all()) == 1
