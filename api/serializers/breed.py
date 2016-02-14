from rest_framework import serializers
from api.models.breed import *

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breed
        fields = ("id", "name")
        read_only_fields = ("id,",)
