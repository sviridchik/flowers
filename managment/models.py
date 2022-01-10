import uuid

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level_of_qualification = models.FloatField(default=0, blank=True)


class Rooms(models.Model):
    id = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=255)
    humidity_summer = models.FloatField()
    humidity_winter = models.FloatField()
    temp_winter = models.FloatField()
    temp_summer = models.FloatField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
