from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

from api.serializers.authentication import *


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
