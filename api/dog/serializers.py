from rest_framework import serializers
from django.db import transaction

from api.user.models import UserProfile
from .models import Dog
from api.constants import GENDERS
from api.breed.serializers import BreedSerializer
from api.breed.models import Breed

class DogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "dogs-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    humans = serializers.HyperlinkedRelatedField(
        read_only = True,
        many = True,
        view_name = "users-detail")

    owner = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    name = serializers.CharField()

    dob = serializers.DateField()
    
    #breed = BreedSerializer()
    breed = serializers.HyperlinkedRelatedField(
        queryset = Breed.objects,
        view_name = "breeds-detail")
    
    weight = serializers.IntegerField()
    
    color = serializers.CharField()

    gender = serializers.ChoiceField(
        choices = GENDERS.values)

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user

        dog = Dog.objects.create(
            name = validated_data.get("name", None),
            breed = validated_data.get("breed", None),
            dob = validated_data.get("dob", None),
            weight = validated_data.get("weight", None),
            color = validated_data.get("color", None),
            gender = validated_data.get("gender", None),
            owner = user)

        #dog.humans.add(user)
        dog.save()

        profile = UserProfile.objects.get(
            user = user)

        profile.dogs.add(dog)

        profile.save()

        return dog

    class Meta:
        model = Dog
        fields = ("id", "url", "owner", "name", "dob", "breed", "weight", "color", "gender", "humans")
        read_only_fields = ("id", "url", "owner")
