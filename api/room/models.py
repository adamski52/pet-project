from django.db import models

from api.generic.models import BaseModel, Property


class RoomProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)


class Room(BaseModel):
    name = models.CharField(
        unique = True,
        max_length = 40)

    is_public = models.BooleanField(
        default = False)

    properties = models.ManyToManyField(
        RoomProperty,
        null = True)


    def __str__(self):
        return self.name

    