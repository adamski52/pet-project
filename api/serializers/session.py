from rest_framework import serializers
from django.contrib.auth.models import User

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = []
