from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    date_created = models.DateTimeField(
                    auto_now_add=True)
    
    date_modified = models.DateTimeField(
                    auto_now=True,
                    null=True)

    date_deleted = models.DateTimeField(
                    null=True)

    name = models.CharField(
                    max_length=40)

    def __str__(self):
        return self.name

    def get_all():
        return Family.objects.filter(date_deleted__isnull=True)
    

    def get_choices():
        return [(family.id, family.name) for family in Family.get_all()]


class UserProfile(models.Model):
    date_created = models.DateTimeField(
                    auto_now_add=True)
    
    date_modified = models.DateTimeField(
                    auto_now=True,
                    null=True)

    date_deleted = models.DateTimeField(
                    null=True)

    user = models.ForeignKey(
                    User,
                    on_delete=models.DO_NOTHING)

    family = models.ForeignKey(
                    Family,
                    on_delete=models.DO_NOTHING)

    address = models.CharField(
                    max_length=40)

    address2 = models.CharField(
                    max_length=40,
                    null=True)

    city = models.CharField(
                    max_length=40)

    state = models.CharField(
                    max_length=2)

    zip_code = models.CharField(
                    max_length=10)

    home_phone = models.CharField(
                    max_length=10,
                    null=True)

    cell_phone = models.CharField(
                    max_length=10,
                    null=True)

    gender = models.CharField(
                    max_length=1)

    def get_all():
        return UserProfile.objects.filter(date_deleted__isnull=True)





