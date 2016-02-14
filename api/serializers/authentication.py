from rest_framework import serializers
from django.contrib.auth.models import User


class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {"password": {"write_only": True}, "username": {"write_only": True}}
