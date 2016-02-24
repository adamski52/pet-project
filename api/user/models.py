from django.contrib.auth.models import User
from django.db import models

from api.generic.models import BaseModel
from api.dog.models import Dog
from api.constants import GENDERS

class UserProfile(BaseModel):
    user = models.OneToOneField(
        User,
        primary_key = True)
    
    dogs = models.ManyToManyField(
        Dog)

    address = models.CharField(
        max_length = 40)

    address2 = models.CharField(
        max_length = 40,
        null = True)

    city = models.CharField(
        max_length = 40)

    state = models.CharField(
        max_length = 2)

    zip_code = models.CharField(
        max_length = 10)

    home_phone = models.CharField(
        max_length = 10,
        null = True)

    cell_phone = models.CharField(
        max_length = 10,
        null = True)

    gender = models.CharField(
        max_length = 1,
        choices = GENDERS.values)

    dob = models.DateField(
        null = True)
