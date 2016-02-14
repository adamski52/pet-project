from rest_framework import viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from api.authentication import *
from api.serializers import *
from api.models import *
from api.permissions import *

"""
mixins.CreateModelMixin, 
mixins.RetrieveModelMixin, 
mixins.UpdateModelMixin,
mixins.DestroyModelMixin,
mixins.ListModelMixin,
GenericViewSet
"""

class LoginViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = AuthenticationSerializer
    queryset = []

    def create(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username,
            password=password)


        if user is not None and user.is_active:
            login(request, user)
            return Response({"session_id": request.session.session_key, "id": user.id})
        
        return Response({"detail": "Invalid username/password."}, status=status.HTTP_403_FORBIDDEN)



class LogoutViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = []

    def create(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})



class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (OneTimeCreate,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return User.objects.all()
        return []


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Dog.get_all()

        return Dog.objects.filter(
            owner = self.request.user)



class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.get_all()
    permission_classes = (IsAuthenticated,)

