from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from managment.models import Rooms, Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, source='user.username')
    password = serializers.CharField(max_length=128, source='user.password')
    email = serializers.EmailField(max_length=128, source='user.email')

    class Meta:
        model = Profile
        fields = ('email', 'level_of_qualification', 'username', 'password')

    def create(self, validated_data):
        password = make_password(validated_data.get('user')['password'])
        user, created = User.objects.get_or_create(
            username=validated_data.get('user')['username'],
            defaults={'email': validated_data.get('user')['email'], 'password': password})

        profile, created = Profile.objects.get_or_create(user=user,
                                                         defaults={'level_of_qualification': validated_data.get(
                                                             'level_of_qualification')})
        return profile

    def update(self, instance, validated_data):
        user = validated_data.get("user", {})
        instance.user.email = user.get('email', instance.user.email)
        instance.user.username = user.get('username', instance.user.username)
        instance.user.password = validated_data.get('password', instance.user.password)
        instance.level_of_qualification = validated_data.get('level_of_qualification', instance.level_of_qualification)
        return instance


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ("id", "humidity_summer", "humidity_winter", "temp_winter", "temp_summer", "profile")
