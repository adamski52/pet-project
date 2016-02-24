import uuid
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from api.generic.models import BaseModel, ActiveManager
from api.dog.models import Dog

class InviteManager(ActiveManager):
    def get_queryset(self):
        return super(InviteManager, self).get_queryset().filter(
            date_expires__gt = datetime.now()).filter(
            status__isnull = True)

    def sent(self, user):
        return self.get_queryset().filter(
            sender = user)

    def received(self, user):
        return self.get_queryset().filter(
            recipient_email = user.email)



class Invite(BaseModel):
    objects = InviteManager()

    def get_expiration():
        now = datetime.now()
        return now + timedelta(
            days = 7)

    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4)

    sender = models.ForeignKey(
        User)

    dog = models.ForeignKey(
        Dog)

    processed = models.BooleanField(
        default = False)

    recipient_email = models.EmailField()

    status = models.NullBooleanField()

    date_expires = models.DateTimeField(
        default = get_expiration)
