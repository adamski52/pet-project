from django.db import models

from api.generic.models import BaseModel

class Breed(BaseModel):
    name = models.CharField(
        max_length = 40)

    def __str__(self):
        return self.name
