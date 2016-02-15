from rest_framework import serializers

class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(
            owner = request.user)

class UserFilteredHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredHyperlinkedRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(
            owner = request.user)