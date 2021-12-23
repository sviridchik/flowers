from rest_framework import serializers

from managment.models import Rooms


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ("id", "humidity_summer", "humidity_winter", "temp_winter", "temp_summer")
