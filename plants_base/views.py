from rest_framework import generics, status
from rest_framework.response import Response

from plants_base.choices import TypeChoice

# TODO: Create your views here.
from plants_base.models import BasePlants, Flowers, Microgreen, Succulents
from plants_base.serializers import (
    FlowersSerializer,
    MicrogreenSerializer,
    PLantSerializer,
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
            try:
                return Succulents.objects.get(pk=pk)
            except Succulents.DoesNotExist:
                return Response({"error": "Not found!"}, status=status.HTTP_404_NOT_FOUND)
        elif self.kwargs["type"] == TypeChoice.MICROGREEN.value:
            return Microgreen.objects.get(pk=pk)
        elif self.kwargs["type"] == TypeChoice.FLOWERS.value:
            return Flowers.objects.get(pk=pk)


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
