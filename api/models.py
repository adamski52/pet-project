from django.db import models
from datetime import datetime


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

    def delete(self, *args, **kwargs):
        #super(BaseModel, self).delete(*args, **kwargs)
        self.date_deleted = datetime.now()
        self.save()
        return self
        


    class Meta:
        abstract = True
    