from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from managment.factories import ProfileFactory, RoomFactory
from managment.models import Profile, Rooms
from plants_base.choices import TypeChoice

# TODO: Create your views here.
from plants_base.models import BasePlants, Flowers, Indicators, Microgreen, Succulents
from plants_base.serializers import (
    FlowersSerializer,
    MicrogreenSerializer,
    PlantSerializer,
    SucculentsSerializer,
)


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
        owner = ProfileFactory()

        RoomFactory()
        room_of_owner = Rooms.objects.get(profile=owner)
        raise Exception(request.data["id"], room_of_owner)
        indicators_of_plant = Indicators.objects.get(plant=request)
        owner = Profile.objects.all()[0]
        warnings = []
        # raise Exception(Rooms.objects.get(profile==owner),Rooms.objects.all())
        # raise Exception(owner,Rooms.objects.all(),Rooms.objects.get(profile=owner))

        # raise Exception(owner.level_of_qualification,float(request.data['level_of_complexity']))
        # TODO : or it is better to do via permissions?
        if owner.level_of_qualification > float(request.data["level_of_complexity"]):
            warnings.append("Might be too hard, not enougn level of qualification")
        if len(room_of_owner) == 0:
            warnings.append("Sorry, but looks like you don't have a room, please add room")
        # if room_of_owner.temp_winter !=
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
