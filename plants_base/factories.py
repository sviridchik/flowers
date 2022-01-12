import factory
from django.contrib.auth.models import User

from plants_base.choices import BreedingTypes, ColorTypes, SoilTypes, TypeChoice
from plants_base.models import BasePlants, Flowers, Microgreen, Succulents


class PlantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BasePlants

    name = "qwerty"
    scientific_name = "qwerty123"
    level_of_complexity = 3
    type_of_soil = SoilTypes.SANDY.name
    date_of_last_transfer = "2003-09-09"
    description = "very interesting plant"
    spraying = True
    breeding_method = BreedingTypes.DIVISION.name


class SucculentFactory(PlantFactory):
    class Meta:
        model = Succulents

    date_of_last_resting_state = "2021-09-09"


class MicrogreenFactory(PlantFactory):
    class Meta:
        model = Microgreen

    date_of_harvest = "2022-09-09"
    benifit_for_health = "Vitamin A,C"


class FlowersFactory(PlantFactory):
    class Meta:
        model = Flowers

    color = ColorTypes.YELLOW.name
    last_date_of_blossom = "2022-09-09"
