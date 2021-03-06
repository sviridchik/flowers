from rest_framework import generics

from plants_care.models import Fertilizer, Problem, Regime, Solution, Watering
from plants_care.serializers import (
    FertilizerSerializer,
    ProblemSerializer,
    RegimeSerializer,
    SolutionSerializer,
    WateringSerializer,
)


class FertilizerList(generics.ListCreateAPIView):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class FertilizerListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fertilizer.objects.all()
    serializer_class = FertilizerSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class WateringList(generics.ListCreateAPIView):
    queryset = Watering.objects.all()
    serializer_class = WateringSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class WateringListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Watering.objects.all()
    serializer_class = WateringSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class SolutionsList(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class SolutionsListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class RegimeList(generics.ListCreateAPIView):
    queryset = Regime.objects.all()
    serializer_class = RegimeSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class RegimeListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Regime.objects.all()
    serializer_class = RegimeSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class ProblemListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)
