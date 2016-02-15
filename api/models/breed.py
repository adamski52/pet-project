from django.db import models

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
