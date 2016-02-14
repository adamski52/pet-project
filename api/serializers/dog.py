from rest_framework import serializers
from django.db import transaction

from api.models.userprofile import *
from api.models.breed import *
from api.models.dog import *
from api.constants.genders import *

class DogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "dog-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    humans = serializers.HyperlinkedRelatedField(
        read_only = True,
        many = True,
        view_name = "user-detail")

    owner = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "user-detail")

    name = serializers.CharField()

    dob = serializers.DateField()
    
    breed = serializers.HyperlinkedRelatedField(
        queryset = Breed.get_all(),
        view_name = "breed-detail")
    
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
