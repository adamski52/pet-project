from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.db import transaction

from api.fields import *
from api.models.invite import *
from api.models.dog import *
from api.serializers.dog import *


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "invites-detail")

    sender = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    recipient_email = serializers.EmailField()

    
    dogs = UserFilteredHyperlinkedRelatedField(
        many = True,
        queryset = Dog.objects,
        view_name = "dogs-detail")

    """
    dogs = UserFilteredPrimaryKeyRelatedField(
        many = True,
        queryset = Dog.objects)
    """

    class Meta:
        model = Invite
        fields = ("id", "url", "sender", "status", "recipient_email", "dogs", "date_created", "date_modified", "date_deleted", "date_expires")
        read_only_fields = ("id", "url", "sender", "status", "date_created", "date_modified", "date_deleted", "date_expires")


