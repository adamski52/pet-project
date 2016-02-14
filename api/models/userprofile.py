from django.db import models
from django.contrib.auth.models import User


from api.models.dog import *
from api.constants.genders import *

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        primary_key = True)
    
    dogs = models.ManyToManyField(
        Dog)

    date_created = models.DateTimeField(
        null = True,
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)

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
