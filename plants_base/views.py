from rest_framework import generics

from plants_base.choices import TypeChoice

# TODO: Create your views here.
from plants_base.models import BasePlants, Flowers, Microgreen, Succulents
from plants_base.serializers import (
    FlowersSerializer,
    MicrogreenSerializer,
    PLantSerializer,
    SucculentsSerializer,
)


# TODO to think how to do it right
class Plants(generics.ListCreateAPIView):
    def get_serializer_class(self, *args, **kwargs):
        if self.request.data["type"] == TypeChoice.SUCCULENT.value:
            return SucculentsSerializer
        elif self.request.data["type"] == TypeChoice.MICROGREEN.value:
            return MicrogreenSerializer
        elif self.request.data["type"] == TypeChoice.FLOWERS.value:
            return FlowersSerializer

    def get_queryset(self, *args, **kwargs):
        if self.request.data["type"] == TypeChoice.SUCCULENT.value:
            return Succulents.objects.all()
        elif self.request.data["type"] == TypeChoice.MICROGREEN.value:
            return Microgreen.objects.all()
        elif self.request.data["type"] == TypeChoice.FLOWERS.value:
            return Flowers.objects.all()


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
