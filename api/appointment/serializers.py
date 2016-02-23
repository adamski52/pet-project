from rest_framework import serializers
from .models import Appointment
from api.generic.serializers import PropertySerializer

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = PropertySerializer(
        read_only = True,
        many = True)

    class Meta:
        model = Appointment
        fields = ("id", "url", "properties")
        read_only_fields = ("id", "url")
