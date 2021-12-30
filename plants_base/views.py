from rest_framework import generics
# TODO: Create your views here.
from plants_base.models import BasePlants, Succulents, Flowers, Microgreen
from plants_base.serializers import PLantSerializer, SucculentsSerializer, MicrogreenSerializer, FlowersSerializer
from plants_base.choices import TypeChoice


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
