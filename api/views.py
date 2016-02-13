from rest_framework import viewsets, mixins
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from api.authentication import *
from api.serializers import UserSerializer, UserProfileSerializer, FamilySerializer
from api.models import UserProfile, Family
from api.permissions import *
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

class SignUpViewSet(mixins.CreateModelMixin, 
                    viewsets.GenericViewSet):
    serializer_class = UserSerializer
    model = User


class UserViewSet(mixins.CreateModelMixin, 
                  mixins.RetrieveModelMixin, 
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_permissions(self):
        return (IsStaffOrTargetUser(),)

class UserProfileViewSet(mixins.CreateModelMixin, 
                         mixins.RetrieveModelMixin, 
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = UserProfile.get_all()
    serializer_class = UserProfileSerializer


class FamilyViewSet(mixins.CreateModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Family.get_all().order_by('-name')
    serializer_class = FamilySerializer