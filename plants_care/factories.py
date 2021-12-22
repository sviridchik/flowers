import factory

from plants_care.choices_care import WateringTypes
from plants_care.models import Fertilizer, Problem, Regime, Solution, Watering


class RegimeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Regime

    frequency = 3
    data_start = "2021-12-12"
    data_end = "2021-12-22"


class FertilizerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Fertilizer

    regime = factory.SubFactory(RegimeFactory)
    description = "very good fertilizer for  flowers during flowering"
    title = "Sodium Nitrate Calcium Nitrate "


class WateringFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Watering

    regime = factory.SubFactory(RegimeFactory)
    description = "very good watering for  flowers during flowering"
    type = WateringTypes.SUBMERSIBLE


class SolutionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Solution

    regime = factory.SubFactory(RegimeFactory)
    description = "a very good solution for  flowers during flowering"
    title = "to buy a new one "


class ProblemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Problem

    description = " forgot to water"
    title = "the end"
