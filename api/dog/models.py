from django.db import models
from django.contrib.auth.models import User
import os

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


class DogAttachment(BaseModel):
    def get_file_name(instance = None, filename = ""):
        return os.path.join("attachments", "dogs", str(instance.dog.id), filename)

    uploaded_by = models.ForeignKey(
        User)

    name = models.CharField(
        max_length = 40)

    file = models.FileField(
        upload_to = get_file_name)

    content_type = models.CharField(
        max_length = 40)

    dog = models.ForeignKey(
        Dog,
        related_name = "attachments")
