from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import serializers

from managment.models import Profile, Rooms


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, source="user.username")
    password = serializers.CharField(max_length=128, source="user.password")
    email = serializers.EmailField(max_length=128, source="user.email")

    class Meta:
        model = Profile
        fields = ("email", "level_of_qualification", "username", "password")

    def create(self, validated_data):
        password = make_password(validated_data.get("user")["password"])
        user, created = User.objects.get_or_create(
            username=validated_data.get("user")["username"],
            defaults={"email": validated_data.get("user")["email"], "password": password},
        )

        profile, created = Profile.objects.get_or_create(
            user=user, defaults={"level_of_qualification": validated_data.get("level_of_qualification")}
        )
        return profile

    def update(self, instance, validated_data):
        if "user" in validated_data:
            instance.user.email = validated_data["user"].get("email", instance.user.email)
            instance.user.username = validated_data["user"].get("username", instance.user.username)
        instance.user.password = validated_data.get("password", instance.user.password)
        instance.level_of_qualification = validated_data.get("level_of_qualification", instance.level_of_qualification)
        instance.save()
        return instance


class RoomSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Rooms
        fields = ("id", "humidity_summer", "humidity_winter", "temp_winter", "temp_summer", "profile")

    # TODO looks like no profile
    def create(self, validated_data):
        profile = validated_data.get("profile")
        # TODO none WHY WHY WHY AAAAAAA
        # raise Exception(profile)
        room, created = Rooms.objects.get_or_create(
            profile=profile,
            defaults={
                "humidity_summer": validated_data.get("humidity_summer"),
                "humidity_winter": validated_data.get("humidity_winter"),
                "temp_winter": validated_data.get("temp_winter"),
                "temp_summer": validated_data.get("temp_summer"),
            },
        )
        return room

    def update(self, instance, validated_data):
        instance.profile = validated_data.get("profile", instance.profile)
        instance.humidity_summer = validated_data.get("humidity_summer", instance.humidity_summer)
        instance.humidity_winter = validated_data.get("humidity_winter", instance.humidity_winter)
        instance.temp_winter = validated_data.get("temp_winter", instance.temp_winter)
        instance.temp_summer = validated_data.get("temp_summer", instance.temp_summer)
        instance.save()
        return instance
