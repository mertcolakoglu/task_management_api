from rest_framework import serializers
from .models import Profile, User
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user_name_surname', 'bio', 'profile_image', 'job_title')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password', 'profile')