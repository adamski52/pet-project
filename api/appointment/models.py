from django.db import models
from django.contrib.auth.models import User

from api.models import BaseModel
from api.dog.models import Dog
from api.room.models import Room
from api.generic.models import Property

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
        Property)

    