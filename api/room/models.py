from django.db import models

from api.models import BaseModel

class RoomProperty(BaseModel):
    property_name = models.CharField(
        unique = True,
        max_length = 40)

    property_value = models.CharField(
        max_length = 40)


class Room(BaseModel):
    width = models.IntegerField()
    
    depth = models.IntegerField()

    name = models.CharField(
        unique = True,
        max_length = 40)

    properties = models.ManyToManyField(
        RoomProperty,
        null = True)
    