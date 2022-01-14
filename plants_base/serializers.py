import datetime

from rest_framework import serializers

from plants_base.models import BasePlants, Flowers, Microgreen, Succulents


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePlants
        fields = (
            "id",
            "name",
            "scientific_name",
            "level_of_complexity",
            "type_of_soil",
            "date_of_last_transfer",
            "description",
            "spraying",
            "type_of_watering",
            "breeding_method",
        )

    def validate(self, data):
        if "date_of_last_resting_state" in data and "date_of_last_transfer" in data:
            if data["date_of_last_resting_state"] < data["date_of_last_transfer"]:
                raise serializers.ValidationError("give some rest to the plant")
        return data


class SucculentsSerializer(PlantSerializer):
    class Meta(PlantSerializer.Meta):
        model = Succulents
        fields = ["date_of_last_resting_state", *PlantSerializer.Meta.fields]

    def create(self, validated_data):
        succulent = Succulents.objects.create(**validated_data)
        return succulent


def check_harvest(value):
    if value < datetime.date.today():
        raise serializers.ValidationError("it's too late")


class MicrogreenSerializer(serializers.ModelSerializer):
    date_of_harvest = serializers.DateField(validators=[check_harvest])

    def validate_benifit_for_health(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("too short description")
        return value

    class Meta(PlantSerializer.Meta):
        model = Microgreen
        fields = ["benifit_for_health", "date_of_harvest", *PlantSerializer.Meta.fields]


class FlowersSerializer(serializers.ModelSerializer):
    class Meta(PlantSerializer.Meta):
        model = Flowers
        fields = ["color", "last_date_of_blossom", *PlantSerializer.Meta.fields]
