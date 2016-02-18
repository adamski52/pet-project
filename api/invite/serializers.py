from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.db import transaction
from django.core.mail import send_mail
from django.template.loader import render_to_string

from api.user.models import UserProfile
from api.invite.fields import SenderHyperlinkedRelatedField
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




    @transaction.atomic
    def create(self, validated_data):
        user = self.context.get("request").user
        dog = validated_data.get("dog", None)
        recipient = validated_data.get("recipient_email", None)

        text_message = render_to_string("templates/template.txt", {"user": user, "dog": dog})
        html_message = render_to_string("templates/template.html", {"user": user, "dog": dog})

        invite = Invite.objects.create(
            sender = user,
            recipient_email = recipient,
            dog = dog)

        send_mail(
            "Storybook Kennels Invite",
            text_message,
            user.email,
            [recipient],
            html_message = html_message)

        return invite



    @transaction.atomic
    def update(self, instance, validated_data):
        invite = Invite.objects.get(
            id = instance.id)

        invite.status = validated_data.get("status")
        user = self.context.get("request").user
        profile = UserProfile.objects.get(
            user = user)
        dog = invite.dog

        if validated_data.get("status") == True:
            profile.dogs.add(dog)


        dog.humans.add(user)
        
        dog.save()
        profile.save()
        invite.save()


        return invite



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
