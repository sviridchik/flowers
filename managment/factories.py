import factory

from managment.models import Rooms


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rooms

    humidity_summer = 23.23
    humidity_winter = 12.3
    temp_winter = 3.4
    temp_summer = 1.23
