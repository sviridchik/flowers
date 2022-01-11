import factory
from django.contrib.auth.models import User

from managment.models import Profile, Rooms


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    email = "test@gmail.com"
    password = "test123123"


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    level_of_qualification = 4.7


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rooms

    humidity_summer = 23.23
    humidity_winter = 12.3
    temp_winter = 3.4
    temp_summer = 1.23
    profile = factory.SubFactory(ProfileFactory)
