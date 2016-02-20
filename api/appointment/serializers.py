from rest_framework import serializers
from .models import Appointment, AppointmentProperty

class AppointmentPropertySerializer(serializers.HyperlinkedModelSerializer):
    property_name = serializers.CharField()
    property_value = serializers.CharField()

    class Meta:
        model = AppointmentProperty
        fields = ("id", "url", "property_name", "property_value")
        read_only_fields = ("id", "url")


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = AppointmentPropertySerializer(
        read_only = True,
        many = True)

    class Meta:
        model = Appointment
        fields = ("id", "url", "properties")
        read_only_fields = ("id", "url")
