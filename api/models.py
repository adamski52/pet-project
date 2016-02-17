from django.db import models

class ActiveManager(models.Manager):
    def active(self):
        return super(ActiveManager, self).get_queryset().filter(
            date_deleted__isnull = True)

class BaseModel(models.Model):
    objects = ActiveManager()

    date_created = models.DateTimeField(
        auto_now_add = True)
    
    date_modified = models.DateTimeField(
        auto_now = True,
        null = True)

    date_deleted = models.DateTimeField(
        null = True)


    class Meta:
        abstract = True
    