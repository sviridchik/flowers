import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rooms = models.IntegerField()
    level_of_qualification = models.IntegerField(verbose_name="dtp_times", default=0, blank=True)
