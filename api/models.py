from django.db import models
from django.contrib.auth.models import User

class Family(models.Model):
    name = models.CharField(
        max_length = 40)

    date_created = models.DateTimeField(
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)

    def get_all():
        return Family.objects.filter(
            date_deleted__isnull = True)



class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        primary_key = True)

    family = models.ForeignKey(
        Family,
        null = True)

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
        max_length = 1)

    dob = models.DateField(
        null = True)

    def get_all():
        return Human.objects.filter(
            date_deleted__isnull = True)

    def get_by_user(id):
        return Human.objects.get(
            user_id = id,
            date_deleted__isnull = True)



class Dog(models.Model):
    family = models.ForeignKey(
        Family,
        null = True)

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

    breed = models.IntegerField()

    weight = models.IntegerField()

    color = models.CharField(
        max_length = 40)

    gender = models.CharField(
        max_length = 1)

    def get_all():
        return Dog.objects.filter(
            date_deleted__isnull = True)

