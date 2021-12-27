from rest_framework import generics

from managment.models import Rooms, Profile
from managment.serializers import (
    RoomSerializer,ProfileSerializer
)


class RoomList(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class RoomListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class UserList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)


class UserListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # TODO: maybe allowANy?
    # permission_classes = (permissions.IsAuthenticated)
