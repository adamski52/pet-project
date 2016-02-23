from rest_framework import serializers
from api.generic.serializers import PropertySerializer
from api.generic.models import Property
from .models import Room, RoomProperty


class RoomPropertySerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset = Property.objects.all())

    value = serializers.CharField()

    name = serializers.ReadOnlyField(
        source = "property.name")

    format = serializers.ReadOnlyField(
        source = "property.format.name")

    class Meta:
        model = RoomProperty
        fields = ("property", "value", "name", "format")
        read_only_fields = ("format", "name")



class RoomSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "rooms-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = RoomPropertySerializer(
        many = True)

    def create(self, validated_data):
        room = Room.objects.create(
            name = validated_data.get("name", None))


        for prop in validated_data.get("properties", None):
            room_property = RoomProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            room.properties.add(room_property)

        return room


    def update(self, instance, validated_data):
        room = Room.objects.get(
            id = instance.id)

        RoomProperty.objects.filter(
            room = room).delete()

        room.name = validated_data.get("name", None)
        room.properties = []

        for prop in validated_data.get("properties", None):
            room_property = RoomProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            room.properties.add(room_property)

        room.save()

        return room


    class Meta:
        model = Room
        fields = ("id", "url", "name", "properties")
        read_only_fields = ("id", "url")

