from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from plants_base.choices import TypeChoice

# TODO: Create your views here.
from plants_base.models import BasePlants, Flowers, Microgreen, Succulents
from plants_base.serializers import (
    FlowersSerializer,
    MicrogreenSerializer,
    PlantSerializer,
    SucculentsSerializer,
)


class Plants(generics.ListCreateAPIView):
    def get_serializer_class(self, *args, **kwargs):

        if self.kwargs["type"] == TypeChoice.SUCCULENT.value:
            return SucculentsSerializer
        elif self.kwargs["type"] == TypeChoice.MICROGREEN.value:
            return MicrogreenSerializer
        elif self.kwargs["type"] == TypeChoice.FLOWERS.value:
            return FlowersSerializer

    def get_queryset(self, *args, **kwargs):
        if self.kwargs["type"] == TypeChoice.SUCCULENT.value:
            return Succulents.objects.all()
        elif self.kwargs["type"] == TypeChoice.MICROGREEN.value:
            return Microgreen.objects.all()
        elif self.kwargs["type"] == TypeChoice.FLOWERS.value:
            return Flowers.objects.all()


class PlantsDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self, *args, **kwargs):
        if self.kwargs["type"] == TypeChoice.SUCCULENT.value:
            return SucculentsSerializer
        elif self.kwargs["type"] == TypeChoice.MICROGREEN.value:
            return MicrogreenSerializer
        elif self.kwargs["type"] == TypeChoice.FLOWERS.value:
            return FlowersSerializer

    def get_object(self):
        pk = self.kwargs["pk"]
        if self.kwargs["type"] == TypeChoice.SUCCULENT.value:
            return get_object_or_404(Succulents, pk=pk)
        elif self.kwargs["type"] == TypeChoice.MICROGREEN.value:
            return get_object_or_404(Microgreen, pk=pk)
        elif self.kwargs["type"] == TypeChoice.FLOWERS.value:
            return get_object_or_404(Flowers, pk=pk)


class SucculentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Succulents.objects.all()
    serializer_class = SucculentsSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class FlowersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flowers.objects.all()
    serializer_class = FlowersSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class MicrogreenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Microgreen.objects.all()
    serializer_class = MicrogreenSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)
