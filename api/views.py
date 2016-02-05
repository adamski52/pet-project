from rest_framework import viewsets
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from api.authentication import *
from api.serializers import UserSerializer, UserProfileSerializer, FamilySerializer
from api.models import UserProfile, Family
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)
    serializer_class = UserSerializer
 
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(self.serializer_class(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.get_all()
    serializer_class = UserProfileSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.get_all().order_by('-name')
    serializer_class = FamilySerializer