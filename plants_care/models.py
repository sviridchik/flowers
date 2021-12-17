import uuid

from django.db import models


class Fertilizer(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    title = models.CharField(max_length=245)
    # TODO:add fk or mixin
    # regime = models.ForeignKey(Regime, models.SET_NULL)


class Watering(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: choice for type
    # type = models.CharField(max_length=255, choices=SoilTypes.choices())
    description = models.TextField()
    # TODO:add fk or mixin
    # regime = models.ForeignKey(Regime, models.SET_NULL)


class Problem(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: choice for type
    title = models.CharField(max_length=245)
    description = models.TextField()
    # TODO:add fk or mixin
    # solution = models.ForeignKey(Solution, models.SET_NULL)


class Solution(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO: may be deleted (not sure if it is an informative field)
    title = models.CharField(max_length=245)
    description = models.TextField()
    # TODO:add fk
    # regime = models.ForeignKey(Regime, models.SET_NULL)


class Regime(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)
    # TODO:to discuss
    frequency = models.IntegerField()
    data_start = models.DateField()
    data_end = models.DateField()


# TODO: to do)
# class Obligations(models.Model):
