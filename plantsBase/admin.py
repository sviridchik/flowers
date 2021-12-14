from django.contrib import admin
from plantsBase import models
# Register your models here.
admin.site.register(models.BasePlants)
admin.site.register(models.Succulents)
admin.site.register(models.Microgreen)
admin.site.register(models.Flowers)