from rest_framework import generics

from .models import Fertilizer, Watering
from .serializers import *


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
