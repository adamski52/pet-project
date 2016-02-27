from rest_framework import serializers
from django.db import transaction
from django.contrib.auth.models import User
from django.conf import settings

from api.generic.models import Property
from api.user.models import UserProfile
from .models import Dog, DogProperty, DogAttachment
from api.constants import GENDERS
from api.breed.serializers import BreedSerializer
from api.breed.models import Breed


class DogAttachmentSerializer(serializers.ModelSerializer):
    dog = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "dogs-detail")

    file = serializers.FileField(
        use_url = settings.UPLOADED_FILES_USE_URL)

    content_type = serializers.CharField(
        read_only = True)

    #uploaded_by = UserShallowSerializer()


    uploaded_by = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    def validate_file(self, file):
        if file is None or file.content_type not in settings.UPLOADED_FILES_ALLOWED_TYPES:
            raise serializers.ValidationError("Invalid file type (" + file.content_type + ").  Must be one of: " + str(settings.UPLOADED_FILES_ALLOWED_TYPES))
        return file


    def create(self, validated_data):
        dog = Dog.objects.get(
            id = self.context.get("view").kwargs["dog_id"])


        file = validated_data.get("file", None)
        content_type = file.content_type

        attachment = DogAttachment.objects.create(
            dog = dog,
            file = file,
            uploaded_by = self.context.get("request").user,
            content_type = content_type,
            name = validated_data.get("name", None))

        return attachment


    class Meta:
        model = DogAttachment
        fields = ("id", "name", "file", "dog", "uploaded_by", "content_type")


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

    attachments = DogAttachmentSerializer(
        many = True,
        read_only = True)



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

    @transaction.atomic
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
        fields = ("id", "url", "owner", "name", "dob", "breed", "weight", "color", "gender", "humans", "properties", "attachments")
        read_only_fields = ("id", "url", "owner", "breed", "attachments")





class DogShallowSerializer(serializers.HyperlinkedModelSerializer):
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

    class Meta:
        model = Dog
        fields = ("id", "url", "owner", "name", "dob", "breed", "weight", "color", "gender", "humans")
        read_only_fields = ("id", "url", "owner", "breed")
