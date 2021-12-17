from rest_framework import serializers

from .models import *


class SucculentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Succulents
        fields = "__all__"


class MicrogreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microgreen
        fields = "__all__"


class FlowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flowers
        fields = "__all__"
