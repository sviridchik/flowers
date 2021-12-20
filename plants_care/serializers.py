from rest_framework import serializers

from .models import *


class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = "__all__"


class FertilizerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(allow_null=False, read_only=True)

    class Meta:
        model = Fertilizer
        # fields = "__all__"
        fields = ("id", "description", "title", "regime")


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"


class RegimeSerializer(serializers.ModelSerializer):
    frequency = serializers.IntegerField(min_value=0)

    class Meta:
        model = Regime
        fields = "__all__"
