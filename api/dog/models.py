from django.db import models
from django.contrib.auth.models import User

from api.generic.models import BaseModel, Property
from api.breed.models import Breed
from api.constants import GENDERS


class DogProperty(BaseModel):
    property = models.ForeignKey(
        Property)

    value = models.CharField(
        max_length = 40)


class Dog(BaseModel):
    name = models.CharField(
        max_length = 40)

    dob = models.DateField(
        null = True)

    breed = models.ForeignKey(
        Breed)

    weight = models.IntegerField()

    color = models.CharField(
        max_length = 40)

    gender = models.CharField(
        max_length = 1,
        choices = GENDERS.values)

    owner = models.ForeignKey(
        User,
        related_name = "owner")

    humans = models.ManyToManyField(
        User)

    properties = models.ManyToManyField(
        DogProperty,
        null = True)

    def __str__(self):
        return self.name + " (" + self.owner.first_name + " " + self.owner.last_name + "'s)"
