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


class UserViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            if self.request.user.is_authenticated():
                return (IsAdminUser(),)
            return (AllowAny(),)
        return (IsAdminOrSelfOrSafe(),)



class FamilyViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin, 
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    serializer_class = FamilySerializer

    def get_permissions(self):
        user = User.objects.get(
            id = self.request.user.id)

        if self.request.method == "POST" and user.family is not None:
            return (IsAdminUser(),)

        return (IsAuthenticated(),)



    def get_queryset(self):
        if self.request.user.is_staff:
            return Family.objects.all()


        human = Human.get_by_user(self.request.user.id)

        if human.family is None:
            return []

        return Family.objects.get(
            id = human.family)



