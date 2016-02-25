from rest_framework import serializers
from api.user.models import UserProfile
from api.dog.models import Dog


class ScheduledForHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(ScheduledForHyperlinkedRelatedField, self).get_queryset()
        if not request or not queryset:
            return None

        if request.user.is_staff:
            return queryset

        return queryset.filter(
            id = request.user.id)

class OwnedDogsHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(OwnedDogsHyperlinkedRelatedField, self).get_queryset()
        if not request or not queryset:
            return None

        if request.user.is_staff:
            return queryset

        profile = UserProfile.objects.get(
            user = request.user)

        return Dog.objects.filter(
            id__in = profile.dogs.all())


