# Create your models here.
import uuid

from django.db import models

from plants_care.models import Watering

from .choices import BreedingTypes, ColorTypes, SoilTypes


class BasePlants(models.Model):
    class Meta:
        abstract = True

    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO:add ManyToManyField in indicators
    # problems = models.IntegerField()
    antoginists = models.IntegerField()
    name = models.CharField(max_length=245)
    scientific_name = models.CharField(max_length=245)
    level_of_complexity = models.FloatField()
    type_of_soil = models.CharField(max_length=255, choices=SoilTypes.choices())
    # TODO: is not created yet. maybe better to do list?
    # fertilizer =  models.ForeignKey(Fertilizer,on_delete = models.SE)
    date_of_last_transfer = models.DateField()
    description = models.TextField()
    spraying = models.BooleanField()
    type_of_watering = models.ForeignKey(Watering, on_delete=models.SET_NULL, null=True)
    breeding_method = models.CharField(max_length=245, choices=BreedingTypes.choices())
    # TODO: is not creared yet. maybe better to do list?
    # indicators= models.ForeignKey(Indicators,models.SET_NULL)


class Succulents(BasePlants):
    date_of_last_resting_state = models.DateField()


class Microgreen(BasePlants):
    benifit_for_health = models.TextField()
    date_of_harvest = models.DateField()


class Flowers(BasePlants):
    color = models.CharField(max_length=245, choices=ColorTypes.choices())
    last_date_of_blossom = models.DateField()
