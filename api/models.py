from django.db import models
from django.contrib.auth.models import User
from api.constants import CONSTANTS

class Breed(models.Model):
    name = models.CharField(
        max_length = 40)

    date_created = models.DateTimeField(
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)

    def __str__(self):
        return self.name

    def get_all():
        return Breed.objects.filter(
            date_deleted__isnull = True)




class Dog(models.Model):
    date_created = models.DateTimeField(
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)

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
        choices = CONSTANTS.GENDERS)

    owner = models.ForeignKey(
        User,
        related_name = "owner")

    humans = models.ManyToManyField(
        User)

    def get_all():
        return Dog.objects.filter(
            date_deleted__isnull = True)



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
        choices = CONSTANTS.GENDERS)

    dob = models.DateField(
        null = True)




