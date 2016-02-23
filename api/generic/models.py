from django.db import models

from api.models import BaseModel

class Format(BaseModel):
    name = models.CharField(
        max_length = 40,
        unique = True)

    def __str__(self):
        return self.name


class Property(BaseModel):
    name = models.CharField(
        max_length = 40,
        unique = True)

    format = models.ForeignKey(
        Format)

    def __str__(self):
        return self.name + " (" + self.format.name + ")"