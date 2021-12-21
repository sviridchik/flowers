# Create your tests here.
import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from plants_care.views import FertilizerList

from .factories import *
from .models import Fertilizer


class TestFertilizerView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:fertilizer_list"

    def test_get(self):
        FertilizerFactory()
        response = self.client.get(reverse(self.view_name))
        assert response.status_code == 200

    def test_post(self):
        response = self.client.post(
            reverse(self.view_name),
            data={
                "description": "very good fertilizer for  flowers during flowering",
                "title": "Sodium Nitrate Calcium Nitrate ",
            },
        )
        assert response.status_code == 201
        assert len(Fertilizer.objects.all()) == 1


class TestFertilizerDetailView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:fertilizer_detail"
        self.f = FertilizerFactory()

    def test_get(self):
        response = self.client.get(reverse(self.view_name, kwargs={"pk": self.f.id}))
        assert response.status_code == 200

    def test_delete(self):
        response = self.client.delete(reverse(self.view_name, kwargs={"pk": self.f.id}))
        assert response.status_code == 204
        assert len(Fertilizer.objects.all()) == 0

    # TODO: DEBUG SMTH WRONG
    def test_patch(self):
        response = self.client.patch(
            reverse(self.view_name, kwargs={"pk": self.f.id}), data={"description": "very informative description"}
        )
        assert response.status_code == 200
        assert len(Fertilizer.objects.all()) == 1


class TestWateringView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:watering_list"

    def test_get(self):
        WateringFactory()
        response = self.client.get(reverse(self.view_name))
        assert response.status_code == 200

    # TODO: SMTH WITH CHOICE
    def test_post(self):
        response = self.client.post(
            reverse(self.view_name),
            data={
                "description": "very good watering for  flowers during flowering",
                "title": "water ",
                "type": "ABOVE",
            },
        )
        # raise Exception(response.data)
        assert response.status_code == 201
        assert len(Watering.objects.all()) == 1


class TestWateringDetailView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:watering_detail"
        self.w = WateringFactory()

    def test_get(self):
        response = self.client.get(reverse(self.view_name, kwargs={"pk": self.w.id}))
        assert response.status_code == 200

    def test_delete(self):
        response = self.client.delete(reverse(self.view_name, kwargs={"pk": self.w.id}))
        assert response.status_code == 204
        assert len(Watering.objects.all()) == 0

    # TODO: DEBUG SMTH WRONG
    def test_patch(self):
        response = self.client.patch(
            reverse(self.view_name, kwargs={"pk": self.w.id}), data={"description": "very informative "}
        )
        assert response.status_code == 200
        assert len(Watering.objects.all()) == 1


class TestSolutionView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:solutions_list"

    def test_get(self):
        SolutionFactory()
        response = self.client.get(reverse(self.view_name))
        assert response.status_code == 200

    def test_post(self):
        response = self.client.post(
            reverse(self.view_name),
            data={"description": "very good solution for  flowers during flowering", "title": "to buy a new one"},
        )
        assert response.status_code == 201
        assert len(Solution.objects.all()) == 1


class TestSolutionDetailView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:solutions_detail"
        self.s = SolutionFactory()

    def test_get(self):
        response = self.client.get(reverse(self.view_name, kwargs={"pk": self.s.id}))
        assert response.status_code == 200

    def test_delete(self):
        response = self.client.delete(reverse(self.view_name, kwargs={"pk": self.s.id}))
        assert response.status_code == 204
        assert len(Solution.objects.all()) == 0

    # TODO: DEBUG SMTH WRONG
    def test_patch(self):
        response = self.client.patch(
            reverse(self.view_name, kwargs={"pk": self.s.id}), data={"description": "very informative "}
        )
        assert response.status_code == 200
        assert len(Solution.objects.all()) == 1


class TestProblemView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:problems_list"

    def test_get(self):
        ProblemFactory()
        response = self.client.get(reverse(self.view_name))
        assert response.status_code == 200

    def test_post(self):
        response = self.client.post(
            reverse(self.view_name),
            data={
                "description": "very good solution for  flowers during flowering",
                "title": "to buy a new one",
                "frequency": 5,
            },
        )
        assert response.status_code == 201
        assert len(Problem.objects.all()) == 1


class TestProblemDetailView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.view_name = "plants_care:problems_detail"
        self.p = ProblemFactory()

    def test_get(self):
        response = self.client.get(reverse(self.view_name, kwargs={"pk": self.p.id}))
        assert response.status_code == 200

    def test_delete(self):
        response = self.client.delete(reverse(self.view_name, kwargs={"pk": self.p.id}))
        assert response.status_code == 204
        assert len(Problem.objects.all()) == 0

    # TODO: DEBUG SMTH WRONG
    def test_patch(self):
        response = self.client.patch(
            reverse(self.view_name, kwargs={"pk": self.p.id}), data={"description": "very informative "}
        )
        assert response.status_code == 200
        assert len(Problem.objects.all()) == 1
