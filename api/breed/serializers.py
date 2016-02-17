from rest_framework import serializers
from .models import Breed

class BreedSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "breeds-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    class Meta:
        model = Breed
        fields = ("id", "url", "name")
        read_only_fields = ("id", "url")
