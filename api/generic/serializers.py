from rest_framework import serializers
from .models import Format, Property, Attachment, Image

class FormatSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "formats-detail")

    name = serializers.CharField()

    class Meta:
        model = Format
        fields = ("id", "url", "name")
        read_only_fields = ("id", "url")



class ImageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "attachments-detail")

    name = serializers.CharField()

    file = serializers.ImageField()

    class Meta:
        model = Image,
        fields = ("id", "url", "name", "file")
        read_only_fields = ("id", "url")





class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "attachments-detail")

    name = serializers.CharField()

    file = serializers.FileField()

    class Meta:
        model = Attachment,
        fields = ("id", "url", "name", "file")
        read_only_fields = ("id", "url")


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "properties-detail")

    name = serializers.CharField()

    format = serializers.PrimaryKeyRelatedField(
        queryset = Format.objects)

    class Meta:
        model = Property
        fields = ("id", "url", "name", "format")
        read_only_fields = ("id", "url")



class PropertyGetSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    name = serializers.CharField()

    format = serializers.CharField(
        source = "format.name")

    class Meta:
        model = Property
        fields = ("id", "name", "format")
        read_only_fields = ("id",)

