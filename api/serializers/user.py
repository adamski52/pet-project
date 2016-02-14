from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.db import transaction

from api.constants.genders import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "user-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    email = serializers.EmailField()

    address = serializers.CharField(
        source = "userprofile.address")

    address2 = serializers.CharField(
        source = "userprofile.address2",
        allow_blank = True,
        required = False)

    city = serializers.CharField(
        source = "userprofile.city")

    state = serializers.CharField(
        source = "userprofile.state")

    zip_code = serializers.CharField(
        source = "userprofile.zip_code")

    home_phone = serializers.CharField(
        source = "userprofile.home_phone",
        allow_blank = True,
        required = False)

    cell_phone = serializers.CharField(
        source = "userprofile.cell_phone",
        allow_blank = True,
        required = False)

    dob = serializers.DateField(
        source = "userprofile.dob")

    gender = serializers.ChoiceField(
        source = "userprofile.gender",
        choices = GENDERS.values)

    date_created = serializers.DateTimeField(
        read_only = True,
        source = "userprofile.date_created",
        required = False)

    date_modified = serializers.DateTimeField(
        read_only = True,
        source = "userprofile.date_modified",
        required = False)

    dogs = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "dog-detail",
        source = "userprofile.dogs",
        many = True,
        required = False)


    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data.get("username", None),
            first_name = validated_data.get("first_name", None),
            last_name = validated_data.get("last_name", None),
            email = validated_data.get("email", None))

        user.set_password(validated_data["password"])

        profile_data = validated_data.get("userprofile", None)
        profile_data["user"] = user

        profile = UserProfile.objects.create(**profile_data)

        user.save()
        profile.save()

        logged_in_user = authenticate(
            username = validated_data["username"],
            password = validated_data["password"])

        login(self.context["request"], logged_in_user)

        return user

    @transaction.atomic
    def update(self, instance, validated_data):
        user = User.objects.get(
            id = instance.id)

        user.update(
            username = validated_data.get("username", None),
            first_name = validated_data.get("first_name", None),
            last_name = validated_data.get("last_name", None),
            email = validated_data.get("email", None))

        user.set_password(validated_data["password"])

        profile = UserProfile.objects.get(
            id = user.id)

        profile_data = validated_data.get("userprofile", None)
        profile_data["user"] = user

        profile.update(**profile_data)

        user.save()
        profile.save()

        return user

    class Meta:
        model = User
        fields = ("id", "url", "username", "password", "first_name", "last_name", "dob", "email", "address", "address2", "city", "state", "zip_code", "home_phone", "cell_phone", "gender", "dogs", "is_staff", "is_superuser", "is_active", "date_created", "date_modified")
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id", "url", "is_staff", "is_superuser", "is_active", "date_created", "date_modified")





