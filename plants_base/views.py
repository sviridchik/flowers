from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from managment.factories import ProfileFactory, RoomFactory
from managment.models import Profile, Rooms
from plants_base.choices import TypeChoice
from plants_base.factories import IndicatorsFactory
from plants_base.models import BasePlants, Flowers, Indicators, Microgreen, Succulents
from plants_base.serializers import (
    FlowersSerializer,
    MicrogreenSerializer,
    PlantSerializer,
    SucculentsSerializer,
)


# TODO: or it is better to use viewsets
class PlantsPlans(generics.ListCreateAPIView):
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

    def post(self, request, *args, **kwargs):
        owner = None
        room_of_owner = None
        indicators_of_plant = None
        try:
            owner = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            pass

        try:
            room_of_owner = Rooms.objects.get(profile=owner)
        except Rooms.DoesNotExist:
            pass

        warnings = []
        # TODO : or it is better to do via permissions?
        # TODO : in future can not be None (permissions)
        if owner is not None:
            if owner.level_of_qualification > float(request.data["level_of_complexity"]):
                warnings.append("Might be too hard, not enougn level of qualification")
        # i think it is critical
        if room_of_owner is None or len(room_of_owner) == 0:
            warnings.append("Sorry, but looks like you don't have a room, please add room")
            return Response(warnings, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        try:
            indicators_of_plant = Indicators.objects.get(plant=serializer.data["id"])
        except Indicators.DoesNotExist:
            pass
        if (
            room_of_owner.temp_winter != indicators_of_plant.temp_winter
            or room_of_owner.temp_summer != indicators_of_plant.temp_summer
        ):
            warnings.append("unsuitable temperature regime")
        if (
            room_of_owner.humidity_summer != indicators_of_plant.humidity_summer
            or room_of_owner.humidity_winter != indicators_of_plant.humidity_winter
        ):
            warnings.append("unsuitable humidity regime")

        headers = self.get_success_headers(serializer.data)
        return Response(
            {"plant": serializer.data, "warnings": warnings}, status=status.HTTP_201_CREATED, headers=headers
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
