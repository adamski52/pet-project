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



class RecipientHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        pk = self.context.get("view").kwargs.get("pk", None)

        queryset = super(RecipientHyperlinkedRelatedField, self).get_queryset()
        if not request or not queryset or not pk:
            return None

        invite = queryset.get(
            id = pk)        

        return Dog.objects.get(
            id = invite.dog)