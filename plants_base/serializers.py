from rest_framework import serializers

from plants_base.models import Flowers, Microgreen, Succulents, Indicators, BasePlants


class PlantBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePlants
        fields = (
        'id', 'problems', 'antoginists', 'name', 'scientific_name', 'level_of_complexity', 'type_of_soil', 'fertilizer',
        'date_of_last_transfer', 'description', 'spraying', 'type_of_watering', 'breeding_method')


class SucculentsSerializer(PlantBaseSerializer):
    class Meta:
        model = Succulents
        fields = ('date_of_last_resting_state',)


class MicrogreenSerializer(PlantBaseSerializer):
    class Meta:
        model = Microgreen
        fields = ('benifit_for_health', 'date_of_harvest')


class FlowersSerializer(PlantBaseSerializer):
    class Meta:
        model = Flowers
        fields = ('color', 'last_date_of_blossom')


class IndicatorsSerializer(serializers.ModelSerializer):
    plant = PlantBaseSerializer()
    class Meta:
        model = Indicators
        fields = ('humidity', 'lightning')
