from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    class Meta:
        model = Appointment
        fields = ("id", "url", "property_name", "property_value")
        read_only_fields = ("id", "url")
