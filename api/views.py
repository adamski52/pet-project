from api.models import UserProfile, Family
from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.get_all()
    serializer_class = UserProfileSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.get_all().order_by('-name')
    serializer_class = FamilySerializer