from rest_framework import serializers
from api.generic.serializers import PropertySerializer
from api.generic.models import Property
from api.room.models import Room
from .models import Camera, CameraProperty


class CameraPropertySerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset = Property.objects.all())

    value = serializers.CharField()

    name = serializers.ReadOnlyField(
        source = "property.name")

    format = serializers.ReadOnlyField(
        source = "property.format.name")

    class Meta:
        model = CameraProperty
        fields = ("property", "value", "name", "format")
        read_only_fields = ("format", "name")



class CameraSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "cameras-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    is_public = serializers.BooleanField()

    properties = CameraPropertySerializer(
        many = True)

    room = serializers.HyperlinkedRelatedField(
        queryset = Room.objects.all(),
        view_name = "rooms-detail")


    def create(self, validated_data):
        camera = Camera.objects.create(
            ip = validated_data.get("ip", None),
            port = validated_data.get("port", None),
            is_public = validated_data.get("is_public", None),
            room = validated_data.get("room", None))

        for prop in validated_data.get("properties", None):
            camera_property = CameraProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            camera.properties.add(camera_property)

        return camera


    def update(self, instance, validated_data):
        camera = Camera.objects.get(
            id = instance.id)

        CameraProperty.objects.filter(
            camera = camera).delete()

        camera.ip = validated_data.get("ip", None)
        camera.port = validated_data.get("port", None)
        camera.is_public = validated_data.get("is_public", None)
        camera.room = validated_data.get("room", None)

        camera.properties = []

        for prop in validated_data.get("properties", None):
            camera_property = CameraProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            camera.properties.add(camera_property)

        camera.save()

        return camera


    class Meta:
        model = Camera
        fields = ("id", "room", "url", "ip", "is_public", "port", "properties")
        read_only_fields = ("id", "url")

