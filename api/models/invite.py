import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from api.models.dog import *

class Invite(models.Model):

    def get_expiration():
        now = datetime.now()
        return now + timedelta(
            days = 7)

    def get_all(self):
        return Invite.objects.filter(
            date_expires__gt = datetime.now()).filter(
            status__isnull = True)

    def get_sent(self):
        return Invite.objects.filter(
            sender = self.request.user)

    def get_received(self):        
        return Invite.objects.filter(
            recipient_email = self.request.user.email)


    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4)

    sender = models.ForeignKey(
        User)

    dogs = models.ManyToManyField(
        Dog)

    recipient_email = models.EmailField()

    status = models.NullBooleanField()

    date_created = models.DateTimeField(
        auto_now_add = True)

    date_expires = models.DateTimeField(
        default = get_expiration)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)
