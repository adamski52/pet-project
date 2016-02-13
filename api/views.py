from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from api.authentication import *
from api.serializers import *
from api.models import *
from api.permissions import *


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

    serializer_class = UserSerializer
    permission_classes = (OneTimeCreate,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return User.objects.all()
        return []


class FamilyViewSet(viewsets.ModelViewSet):

    serializer_class = FamilySerializer
    permission_classes = (OneToOneCreate,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return User.objects.all()
        return []



