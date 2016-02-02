from rest_framework import serializers
from api.models import Human, Family

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ("humanUUID", "familyUUID", "email", "firstName", "lastName", "address", "address2", "city", "state", "zipCode", "homePhone", "cellPhone", "gender")


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ("familyUUID", "name")