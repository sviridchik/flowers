from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from plants_care.models import Fertilizer, Problem, Regime, Solution, Watering


class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = ("id", "type", "description", "regime")


class FertilizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fertilizer
        fields = ("id", "description", "title", "regime")
        # TODO https://django.fun/docs/django-rest-framework/ru/3.12/api-guide/validators/
        validators = [UniqueTogetherValidator(queryset=Fertilizer.objects.all(), fields=["id"])]


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
