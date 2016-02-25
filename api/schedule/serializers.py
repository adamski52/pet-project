from rest_framework import serializers
from django.contrib.auth.models import User

from api.room.models import Room
from api.room.serializers import RoomSerializer
from api.appointment.models import Appointment


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    room = serializers.HyperlinkedRelatedField(
        queryset = Room.objects.all(),
        view_name = "rooms-detail")

    class Meta:
        model = Appointment
        fields = ("id", "url", "room", "start_date", "end_date", "is_confirmed")
        read_only_fields = ("id", "url", "is_confirmed")

