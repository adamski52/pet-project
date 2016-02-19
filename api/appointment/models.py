from django.db import models
from django.contrib.auth.models import User

from api.models import BaseModel
from api.dog.models import Dog
from api.room.models import Room


class AppointmentProperty(BaseModel):
    property_name = models.CharField(
        unique = True,
        max_length = 40)

    property_value = models.CharField(
        max_length = 40)


class Appointment(BaseModel):
    scheduled_by = models.ForeignKey(
        User)

    dog = models.ForeignKey(
        Dog)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    room = models.ForeignKey(
        Room)

    properties = models.ManyToManyField(
        AppointmentProperty)

    