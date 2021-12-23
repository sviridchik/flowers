import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Create your models here.
class Profile(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rooms = models.IntegerField()
    level_of_qualification = models.IntegerField(verbose_name="dtp_times", default=0, blank=True)


class Rooms(models.Model):
    id = models.IntegerField(primary_key=True, default=uuid.uuid4, editable=False)

    humidity_summer = models.FloatField()
    humidity_winter = models.FloatField()
    temp_winter = models.FloatField()
    temp_summer = models.FloatField()
