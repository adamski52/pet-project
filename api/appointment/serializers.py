from rest_framework import serializers
from django.contrib.auth.models import User

from api.generic.serializers import PropertySerializer
from api.generic.models import Property
from .models import Appointment, AppointmentProperty
from .fields import ScheduledForHyperlinkedRelatedField, OwnedDogsHyperlinkedRelatedField
from api.user.serializers import UserSerializer, UserShallowSerializer
from api.dog.models import Dog
from api.dog.serializers import DogSerializer, DogShallowSerializer
from api.room.models import Room
from api.room.serializers import RoomSerializer


class AppointmentPropertySerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset = Property.objects.all())

    value = serializers.CharField()

    name = serializers.ReadOnlyField(
        source = "property.name")

    format = serializers.ReadOnlyField(
        source = "property.format.name")

    class Meta:
        model = AppointmentProperty
        fields = ("property", "value", "name", "format")
        read_only_fields = ("format", "name")



class AppointmentConfirmSerializer(serializers.HyperlinkedModelSerializer):
    is_confirmed = serializers.BooleanField()

    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)


    def update(self, instance, validated_data):        
        appointment = Appointment.objects.get(
            id = instance.id)

        appointment.is_confirmed = validated_data.get("is_confirmed", False)

        appointment.save()

        return appointment

    class Meta:
        model = Appointment
        fields = ("id", "url", "is_confirmed")
        read_only_fields = ("id", "url")


class AppointmentPutSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = AppointmentPropertySerializer(
        many = True)

    scheduled_by = UserShallowSerializer(
        read_only = True)

    scheduled_for = UserShallowSerializer(
        read_only = True)

    room = RoomSerializer(
        read_only = True)

    dog = DogShallowSerializer(
        read_only = True)

    class Meta:
        model = Appointment
        fields = ("id", "url", "scheduled_by", "scheduled_for", "room", "date_created", "date_modified", "dog", "properties")
        read_only_fields = ("id", "url", "dog", "room", "scheduled_for", "scheduled_by")




class AppointmentGetSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = AppointmentPropertySerializer(
        many = True)

    scheduled_by = UserShallowSerializer(
        read_only = True)

    scheduled_for = UserShallowSerializer(
        read_only = True)

    room = RoomSerializer(
        read_only = True)

    dog = DogShallowSerializer(
        read_only = True)

    class Meta:
        model = Appointment
        fields = ("id", "url", "scheduled_by", "scheduled_for", "room", "date_created", "date_modified", "is_confirmed", "dog", "start_date", "end_date", "properties")
        read_only_fields = ("id", "url", "dog", "room", "scheduled_for", "scheduled_by")




class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only = True,
        view_name = "appointments-detail")

    id = serializers.PrimaryKeyRelatedField(
        read_only = True)

    properties = AppointmentPropertySerializer(
        many = True)

    scheduled_by = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = "users-detail")

    scheduled_for = ScheduledForHyperlinkedRelatedField(
        queryset = User.objects.all(),
        view_name = "users-detail",
        required = False)    

    room = serializers.HyperlinkedRelatedField(
        queryset = Room.objects.all(),
        view_name = "rooms-detail")

    dog = OwnedDogsHyperlinkedRelatedField(
        queryset = Dog.objects.all(),
        view_name = "dogs-detail")

    start_date = serializers.DateTimeField()

    end_date = serializers.DateTimeField()

    def create(self, validated_data):
        appointment = Appointment.objects.create(
            dog = validated_data.get("dog", None),
            scheduled_by = self.context.get("request").user,
            scheduled_for = validated_data.get("scheduled_for", self.context.get("request").user),
            room = validated_data.get("room", None),
            start_date = validated_data.get("start_date", None),
            end_date = validated_data.get("end_date", None))



        for prop in validated_data.get("properties", None):
            appointment_property = AppointmentProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None))

            appointment.properties.add(appointment_property)

        return appointment


    def update(self, instance, validated_data):
        appointment = Appointment.objects.get(
            id = instance.id)

        AppointmentProperty.objects.filter(
            appointment = appointment).delete()


        # not allowed to change anything but add some props.  to change a booking, needs to be deleted/cancelled and redone
        appointment.properties = []

        for prop in validated_data.get("properties", None):
            appointment_property = AppointmentProperty.objects.create(
                property = prop.get("property", None),
                value = prop.get("value", None),)

            appointment.properties.add(appointment_property)

        appointment.save()

        return appointment


    class Meta:
        model = Appointment
        fields = ("id", "url", "scheduled_by", "scheduled_for", "room", "date_created", "date_modified", "is_confirmed", "dog", "start_date", "end_date", "properties")
        read_only_fields = ("id", "url", "is_confirmed")

