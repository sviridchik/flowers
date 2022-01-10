from rest_framework import serializers

from plants_base.models import Flowers, Microgreen, Succulents, BasePlants


class PLantSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasePlants
        fields = (
            "id", "name", "scientific_name", "level_of_complexity", "type_of_soil", "date_of_last_transfer",
            "description",
            "spraying", "type_of_watering", "breeding_method")


class SucculentsSerializer(serializers.ModelSerializer):
    class Meta(PLantSerializer.Meta):
        model = Succulents
        fields = ("date_of_last_resting_state",)

    def create(self, validated_data):
        # TODO debug Exception(validated_data, self)
        return Succulents(**validated_data)


class MicrogreenSerializer(serializers.ModelSerializer):
    class Meta(PLantSerializer.Meta):
        model = Microgreen
        fields = ("benifit_for_health", " date_of_harvest")


class FlowersSerializer(serializers.ModelSerializer):
    class Meta(PLantSerializer.Meta):
        model = Flowers
        fields = ("color", "last_date_of_blossom")
