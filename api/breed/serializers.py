from rest_framework import serializers
from api.generic.models import Property
from .models import Breed, BreedProperty


class BreedPropertySerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset = Property.objects.all())

    value = serializers.CharField()

    name = serializers.ReadOnlyField(
        source = "property.name")

    format = serializers.ReadOnlyField(
        source = "property.format.name")

    class Meta:
        model = BreedProperty
        fields = ("property", "value", "name", "format")
        read_only_fields = ("format", "name")



class BreedSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "breeds-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = BreedPropertySerializer(
        many = True)



    def create(self, validated_data):
        breed = Breed.objects.create(
            name = validated_data.get("name", None))

        for prop in validated_data.get("properties", None):
            breed_property = BreedProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            breed.properties.add(breed_property)

        return breed


    def update(self, instance, validated_data):
        breed = Breed.objects.get(
            id = instance.id)

        BreedProperty.objects.filter(
            breed = breed).delete()

        breed.name = validated_data.get("name", None)
        breed.properties = []

        for prop in validated_data.get("properties", None):
            breed_property = BreedProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            breed.properties.add(breed_property)

        breed.save()

        return breed



    class Meta:
        model = Breed
        fields = ("id", "url", "name", "properties")
        read_only_fields = ("id", "url")
