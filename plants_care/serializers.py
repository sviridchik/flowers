from rest_framework import serializers

from .models import *


class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = ("id", "type", "description", "regime")


class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = ("id", "description", "title", "regime")


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ("id", "description", "title")


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ("id", "description", "title", "regime")


class RegimeSerializer(serializers.ModelSerializer):
    frequency = serializers.IntegerField(min_value=0)

    class Meta:
        model = Regime
        fields = ("id", "frequency", "data_start", "data_end")
