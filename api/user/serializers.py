from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import transaction
from django.contrib.auth import authenticate, login


from .models import UserProfile, UserAttachment
from api.constants import GENDERS
from api.dog.serializers import DogSerializer


class UserShallowSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "users-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    class Meta:
        model = User
        fields = ("id", "url", "username", "first_name", "last_name")
        read_only_fields = ("id", "url", "username", "first_name", "last_name")



class UserAttachmentSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    uploaded_by = UserShallowSerializer(
        read_only = True)

    file = serializers.FileField(
        use_url = settings.UPLOADED_FILES_USE_URL)

    content_type = serializers.CharField(
        read_only = True)

    def validate_file(self, file):
        if file is None or file.content_type not in settings.UPLOADED_FILES_ALLOWED_TYPES:
            raise serializers.ValidationError("Invalid file type (" + file.content_type + ").  Must be one of: " + str(settings.UPLOADED_FILES_ALLOWED_TYPES))
        return file


    def create(self, validated_data):
        user = User.objects.get(
            id = self.kwargs["user_id"]
        )

        file = validated_data.get("file", None)
        content_type = file.content_type

        attachment = UserAttachment.objects.create(
            user = user,
            file = file,
            uploaded_by = self.context.get("request").user,
            content_type = content_type,
            name = validated_data.get("name", None))

        return attachment


    class Meta:
        model = UserAttachment
        fields = ("id", "name", "file", "user", "uploaded_by", "content_type")





class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "users-detail")

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

    dogs = DogSerializer(
        source = "userprofile.dogs",
        read_only = True,
        many = True)
    
    attachments = UserAttachmentSerializer(
        many = True,
        read_only = True)

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
        fields = ("id", "url", "username", "password", "first_name", "last_name", "dob", "email", "address", "address2", "city", "state", "zip_code", "home_phone", "cell_phone", "gender", "dogs", "attachments", "is_staff", "is_superuser", "is_active", "date_created", "date_modified")
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ("id", "url", "dogs", "is_staff", "is_superuser", "is_active", "date_created", "date_modified")



