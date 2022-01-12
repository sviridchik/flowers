from rest_framework import generics

from managment.models import Profile, Rooms
from managment.serializers import ProfileSerializer, RoomSerializer


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
