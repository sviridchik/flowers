from rest_framework import serializers

from plants_base.models import BasePlants, Flowers, Microgreen, Succulents


class PLantSerializer(serializers.ModelSerializer):
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


class SucculentsSerializer(PLantSerializer):
    class Meta(PLantSerializer.Meta):
        model = Succulents
        fields = ["date_of_last_resting_state"] + list(PLantSerializer.Meta.fields)

    def create(self, validated_data):
        succulent = Succulents.objects.create(**validated_data)
        return succulent


class MicrogreenSerializer(serializers.ModelSerializer):
    class Meta(PLantSerializer.Meta):
        model = Microgreen
        fields = ["benifit_for_health", "date_of_harvest"] + list(PLantSerializer.Meta.fields)


class FlowersSerializer(serializers.ModelSerializer):
    class Meta(PLantSerializer.Meta):
        model = Flowers
        fields = ["color", "last_date_of_blossom"] + list(PLantSerializer.Meta.fields)
