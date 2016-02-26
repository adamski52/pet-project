from rest_framework import serializers
from django.db import transaction

from api.generic.models import Property
from api.user.models import UserProfile
from .models import Dog, DogProperty
from api.constants import GENDERS
from api.breed.serializers import BreedSerializer
from api.breed.models import Breed


class DogPropertySerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset = Property.objects.all())

    value = serializers.CharField()

    name = serializers.ReadOnlyField(
        source = "property.name")

    format = serializers.ReadOnlyField(
        source = "property.format.name")

    class Meta:
        model = DogProperty
        fields = ("property", "value", "name", "format")
        read_only_fields = ("format", "name")




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

    #breed = BreedSerializer(Breed)

    breed = serializers.HyperlinkedRelatedField(
        queryset = Breed.objects,
        view_name = "breeds-detail")


    weight = serializers.IntegerField()
    
    color = serializers.CharField()

    gender = serializers.ChoiceField(
        choices = GENDERS.values)

    properties = DogPropertySerializer(
        many = True)

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

        for prop in validated_data.get("properties", None):
            dog_property = DogProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            dog.properties.add(dog_property)

        dog.humans.add(user)
        #dog.save()

        profile = UserProfile.objects.get(
            user = user)

        profile.dogs.add(dog)

        profile.save()

        return dog


    def update(self, instance, validated_data):
        dog = Dog.objects.get(
            id = instance.id)

        DogProperty.objects.filter(
            dog = dog).delete()

        dog.name = validated_data.get("name", None)
        dog.dob = validated_data.get("dob", None)
        dog.breed = validated_data.get("breed", None)
        dog.weight = validated_data.get("weight", None)
        dog.color = validated_data.get("color", None)
        dog.gender = validated_data.get("gender", None)

        dog.properties = []

        for prop in validated_data.get("properties", None):
            dog_property = DogProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            dog.properties.add(dog_property)

        dog.save()

        return dog

    class Meta:
        model = Dog
        fields = ("id", "url", "owner", "name", "dob", "breed", "weight", "color", "gender", "humans", "properties")
        read_only_fields = ("id", "url", "owner", "breed")
