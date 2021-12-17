from django.contrib import admin

# Register your models here.
from plants_care import models

# Register your models here.
admin.site.register(models.Fertilizer)
admin.site.register(models.Watering)
admin.site.register(models.Regime)
admin.site.register(models.Solution)
admin.site.register(models.Problem)
