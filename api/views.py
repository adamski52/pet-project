from api.models import Human, Family
from rest_framework import viewsets
from api.serializers import HumanSerializer, FamilySerializer


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all().order_by('-lastName')
    serializer_class = HumanSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all().order_by('-name')
    serializer_class = FamilySerializer