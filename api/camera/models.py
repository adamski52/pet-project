from django.db import models
from django.db.models import Q

from api.room.models import Room
from api.generic.models import BaseModel, Property

class CameraProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)



class Camera(BaseModel):
    ip = models.CharField(
        unique = True,
        max_length = 40)

    port = models.CharField(
        max_length = 5)

    properties = models.ManyToManyField(
        CameraProperty,
        null = True)

    room = models.ForeignKey(
        Room)

    is_public = models.BooleanField(
        default = False)

    def __str__(self):
        return self.ip + ":" + self.port

    