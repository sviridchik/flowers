from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User
from managment.models import Rooms, Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, source='user.username')
    password = serializers.CharField(max_length=128, source='user.password')
    email = serializers.EmailField(max_length=128, source='user.email')

    class Meta:
        model = Profile
        fields = ('email', 'level_of_qualification', 'username', 'password')

    def create(self, validated_data):
        ps = make_password(validated_data.get('user')['password'])
        user, created = User.objects.get_or_create(
            username=validated_data.get('user')['username'],
            defaults={'email': validated_data.get('user')['email'], 'password': ps})

        profile, created = Profile.objects.get_or_create(user=user,
                                                         defaults={'level_of_qualification': validated_data.get(
                                                             'level_of_qualification')})
        return profile

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            instance.user.email = validated_data['user'].get('email', instance.user.email)
            instance.user.username = validated_data['user'].get('username', instance.user.username)
        instance.user.password = validated_data.get('password', instance.user.password)
        # TODO here is ok
        instance.level_of_qualification = validated_data.get('level_of_qualification', instance.level_of_qualification)
        return instance


class RoomSerializer(serializers.ModelSerializer):
    # TODO not sure if it is a good idea
    profile = ProfileSerializer(read_only=True, many = True)

    class Meta:
        model = Rooms
        fields = ("id", "humidity_summer", "humidity_winter", "temp_winter", "temp_summer", "profile")

    def create(self, validated_data):
        profiles_data = validated_data.pop('profile')
        room = Rooms.objects.create(**validated_data)
        for profile_data in profiles_data:
            profile, created = Ingredient.objects.get_or_create(username=profile_data['username'])
            room.profile.add(profile)
        return room

    def update(self, instance, validated_data):
        profiles_data = validated_data.pop('profile')
        instance.humidity_summer = validated_data.get('humidity_summer', instance.humidity_summer)
        instance.last_name = validated_data.get('temp_winter', instance.temp_winter)
        instance.temp_winter = validated_data.get('humidity_winter', instance.humidity_winter)
        instance.temp_summer = validated_data.get('temp_summer', instance.temp_summer)

        instance.save()

        for profile_data in profiles_data:
            profile = profiles.pop(0)
            profile.username = profile_data.get('username', profile.username)
            profile.password = profile_data.get('password', profile.password)
            profile.email = profile_data.get('email', profile.email)
            profile.save()
        return instance
