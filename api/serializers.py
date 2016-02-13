from rest_framework import serializers
from api.models import Family, UserProfile
from django.db import models
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email", "is_staff", "is_superuser", "is_active")
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ("id", "is_staff", "is_superuser", "is_active", "date_joined")

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if validated_data.get('password'):
        	instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("id", "user", "family", "address", "address2", "city", "state", "zip_code", "home_phone", "cell_phone", "gender", "date_created", "date_modified")


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("id", "name", "date_created", "date_modified")