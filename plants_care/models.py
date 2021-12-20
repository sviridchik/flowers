import uuid

from django.db import models

from .choices_care import WateringTypes


class Regime(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO:to discuss
    frequency = models.IntegerField()
    data_start = models.DateField()
    data_end = models.DateField()


class Fertilizer(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, auto_created=True, unique=True)
    description = models.TextField()
    title = models.CharField(max_length=245)
    # TODO:add fk or mixin
    regime = models.ForeignKey(Regime, models.SET_NULL, null=True)


class Watering(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: choice for type
    type = models.CharField(max_length=255, choices=WateringTypes.choices())
    description = models.TextField()
    # TODO:add fk or mixin
    regime = models.ForeignKey(Regime, models.SET_NULL, null=True)


class Solution(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: may be deleted (not sure if it is an informative field)
    title = models.CharField(max_length=245)
    description = models.TextField()
    # TODO:add fk
    regime = models.ForeignKey(Regime, models.SET_NULL, null=True)


class Problem(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: choice for type
    title = models.CharField(max_length=245)
    description = models.TextField()


# TODO: to do)
# class Obligations(models.Model):
