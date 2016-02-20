from rest_framework import serializers
from .models import Room, RoomProperty

class RoomPropertySerializer(serializers.HyperlinkedModelSerializer):
    property_name = serializers.CharField()
    property_value = serializers.CharField()

    class Meta:
        model = RoomProperty
        fields = ("id", "url", "property_name", "property_value")
        read_only_fields = ("id", "url")



class RoomSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "rooms-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = RoomPropertySerializer(
        read_only = True,
        many = True)

    class Meta:
        model = Room
        fields = ("id", "url", "name", "properties")
        read_only_fields = ("id", "url")
