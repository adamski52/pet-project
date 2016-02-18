from rest_framework import serializers
from api.dog.models import Dog

class SenderHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super(SenderHyperlinkedRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(
            owner = request.user)
