from rest_framework import serializers
from api.models import Family, UserProfile
from django.db import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "is_staff", "is_superuser")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user", "family", "address", "address2", "city", "state", "zip_code", "home_phone", "cell_phone", "gender", "date_created", "date_modified")


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "date_created", "date_modified")