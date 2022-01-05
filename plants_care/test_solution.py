import pytest

from plants_care.models import Solution
from plants_care.serializers import SolutionSerializer


@pytest.mark.django_db
def test_get_solution(client, solution):
    response = client.get("/care/solutions/")
    assert response.status_code == 200
    assert len(response.json()) == 1
    processed_solution = SolutionSerializer(solution).data.copy()
    processed_solution["regime"] = str(processed_solution["regime"])
    assert response.json()[0] == processed_solution


@pytest.mark.django_db
def test_post_solution(client):
    response = client.post(
        "/care/solutions/",
        data={"description": "very good solution for  flowers during flowering", "title": "to buy a new one"},
    )
    assert response.status_code == 201
    assert len(Solution.objects.all()) == 1
    processed_solution = SolutionSerializer(Solution.objects.all()[0]).data.copy()
    if processed_solution["regime"] is not None:
        processed_solution["regime"] = str(processed_solution["regime"])
    assert response.json() == processed_solution


@pytest.mark.django_db
def test_get_solution_pk(client, solution):
    response = client.get(f"/care/solutions/{solution.id}/")
    assert response.status_code == 200
    processed_solution = SolutionSerializer(solution).data.copy()
    processed_solution["regime"] = str(processed_solution["regime"])
    assert response.json() == processed_solution


@pytest.mark.django_db
def test_delete_solution(client, solution):
    response = client.delete(f"/care/solutions/{solution.id}/")
    assert response.status_code == 204
    assert len(Solution.objects.all()) == 0


@pytest.mark.django_db
def test_patch_solution(client, solution):
    response = client.patch(f"/care/solutions/{solution.id}/", data={"description": "very informative"})
    solution.refresh_from_db()
    assert solution.description == "very informative"
    assert response.status_code == 200
    assert len(Solution.objects.all()) == 1
    processed_solution = SolutionSerializer(Solution.objects.all()[0]).data.copy()
    if processed_solution["regime"] is not None:
        processed_solution["regime"] = str(processed_solution["regime"])
    assert response.json() == processed_solution
