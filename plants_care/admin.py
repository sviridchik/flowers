from django.contrib import admin

from plants_care import models

admin.site.register(models.Fertilizer)
admin.site.register(models.Watering)
admin.site.register(models.Regime)
admin.site.register(models.Solution)
admin.site.register(models.Problem)
