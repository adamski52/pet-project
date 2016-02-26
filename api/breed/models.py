from django.db import models

from api.generic.models import BaseModel, Property

class BreedProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)



class Breed(BaseModel):
    name = models.CharField(
        max_length = 40)

    properties = models.ManyToManyField(
        BreedProperty,
        null = True)

    def __str__(self):
        return self.name
