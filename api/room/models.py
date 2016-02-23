from django.db import models

from api.models import BaseModel
from api.generic.models import Property


class RoomProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)


class Room(BaseModel):
    name = models.CharField(
        unique = True,
        max_length = 40)

    properties = models.ManyToManyField(
        RoomProperty,
        null = True)

    