from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 


class AdminManager(models.Manager):
    def get_queryset(self):
        return super(AdminManager, self).get_queryset()

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super(ActiveManager, self).get_queryset().filter(
            date_deleted__isnull = True)

class BaseModel(models.Model):
    objects = ActiveManager()
    admin_objects = AdminManager()

    date_created = models.DateTimeField(
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)

    def delete(self, *args, **kwargs):
        self.date_deleted = datetime.now()
        self.save()
        return self


    class Meta:
        abstract = True
    


class Format(BaseModel):
    name = models.CharField(
        max_length = 40,
        unique = True)

    def __str__(self):
        return self.name


class Image(BaseModel):
    name = models.CharField(
        max_length = 40)

    file = models.ImageField()


class Attachment(BaseModel):
    name = models.CharField(
        max_length = 40)

    file = models.FileField()




class Property(BaseModel):
    name = models.CharField(
        max_length = 40,
        unique = True)

    format = models.ForeignKey(
        Format)

    def __str__(self):
        return self.name + " (" + self.format.name + ")"