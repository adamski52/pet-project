from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.db import transaction

from api.invite.fields import SenderHyperlinkedRelatedField, RecipientHyperlinkedRelatedField
from .models import Invite
from api.dog.models import Dog


class InviteSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "invites-detail")

    sender = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    dog = SenderHyperlinkedRelatedField(
        queryset = Dog.objects,
        view_name = "dogs-detail")

    class Meta:
        model = Invite
        fields = ("id", "url", "sender", "status", "recipient_email", "dog", "date_created", "date_modified", "date_deleted", "date_expires")
        read_only_fields = ("id", "url", "sender", "status", "date_created", "date_modified", "date_deleted", "date_expires")



class SenderSerializer(InviteSerializer):

    status = serializers.ChoiceField(
        choices = (True, False))

    class Meta:
        model = Invite
        fields = ("id", "url", "sender", "status", "recipient_email", "dog", "date_created", "date_modified", "date_deleted", "date_expires")
        read_only_fields = ("id", "url", "sender", "status", "recipient_email", "date_created", "date_modified", "date_deleted", "date_expires")


class RecipientSerializer(InviteSerializer):

    status = serializers.ChoiceField(
        choices = (True, False))

    dog = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "dogs-detail")

    class Meta:
        model = Invite
        fields = ("id", "url", "sender", "status", "recipient_email", "dog", "date_created", "date_modified", "date_deleted", "date_expires")
        read_only_fields = ("id", "url", "sender", "recipient_email", "dog", "date_created", "date_modified", "date_deleted", "date_expires")
