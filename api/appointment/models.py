from django.contrib.auth.models import User
from django.db import models

from api.generic.models import Property, BaseModel, ActiveManager
from api.room.models import Room
from api.dog.models import Dog


class AppointmentProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)


class AppointmentManager(ActiveManager):
    def get_queryset(self):
        return super(AppointmentManager, self).get_queryset().filter(
            is_cancelled = False)


class Appointment(BaseModel):
    objects = AppointmentManager()

    scheduled_by = models.ForeignKey(
        User)

    scheduled_for = models.ForeignKey(
        User)

    dog = models.ForeignKey(
        Dog,
        editable = False)

    room = models.ForeignKey(
        Room,
        editable = False)

    is_confirmed = models.BooleanField(
        default = False)

    is_cancelled = models.BooleanField(
        default = False)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    properties = models.ManyToManyField(
        AppointmentProperty,
        null = True)

    