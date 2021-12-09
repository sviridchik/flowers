# Create your models here.
import uuid
from choices import watering_choose, soil_choose, breeding_choose, color_choose
from django.db import models
from django.db import models


class BasePlants(models.Model):
    class Meta:
        abstract = True

    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # и потом в сериализаторе лист сделать ???
    problems = models.IntegerField()
    antoginists = models.IntegerField()
    name = models.StringField()
    scientific_name = models.StringField()
    level_of_complexity = models.FloatField()
    type_of_soil = models.StringField(max_len=255, choice=soil_choose)
    # is not creared yet
    # maybe better to do list?
    # fertilizer =  models.ForeignKey(Fertilizer,on_delete = models.SE)
    date_of_last_transfer = models.DateField()
    description = models.TextField()
    spraying = models.BooleanField()
    type_of_watering = models.StringField(max_len=245, choice=watering_choose)
    breeding_method = models.StringField(max_len=245, choice=breeding_choose)
    # is not creared yet
    # maybe better to do list?
    # indicators= models.ForeignKey(Indicators,models.SET_NULL)


class Succulents(BasePlants):
    date_of_last_resting_state = models.DateField()


class Microgreen(BasePlants):
    benifit_for_health = models.TextField()
    date_of_harvest = models.DateField()


class Flowers(BasePlants):
    color = models.StringField(max_len=245, choice=color_choose)
    last_date_of_blossom = models.DateField()
