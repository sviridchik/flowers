import uuid

from django.db import models

from plants_base.choices import BreedingTypes, ColorTypes, SoilTypes
from plants_care.models import Fertilizer, Problem, Watering


class BasePlants(models.Model):
    class Meta:
        abstract = True

    id = models.CharField(max_length=245, primary_key=True, default=uuid.uuid4, editable=False)
    problems = models.ForeignKey(Problem, on_delete=models.SET_NULL, null=True)
    # TODO: antogonist fk?
    # antoginists = models.IntegerField()
    name = models.CharField(max_length=245)
    scientific_name = models.CharField(max_length=245)
    level_of_complexity = models.FloatField()
    type_of_soil = models.CharField(max_length=255, choices=SoilTypes.choices())
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.SET_NULL, null=True)
    date_of_last_transfer = models.DateField()
    description = models.TextField()
    spraying = models.BooleanField()
    type_of_watering = models.ForeignKey(Watering, on_delete=models.SET_NULL, null=True)
    breeding_method = models.CharField(max_length=245, choices=BreedingTypes.choices())
    type = models.CharField(max_length=255)


class Succulents(BasePlants):
    date_of_last_resting_state = models.DateField()


class Microgreen(BasePlants):
    benifit_for_health = models.TextField()
    date_of_harvest = models.DateField()


class Flowers(BasePlants):
    color = models.CharField(max_length=245, choices=ColorTypes.choices())
    last_date_of_blossom = models.DateField()


class Indicators(models.Model):
    # TODO smth very wrong
    # plant = models.ManyToManyField(BasePlants)
    humidity = models.FloatField()
    lightning = models.IntegerField()
