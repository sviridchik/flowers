from rest_framework import generics

from .models import Fertilizer
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
