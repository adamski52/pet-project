from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions

from .serializers import AuthenticationSerializer, SessionSerializer

class LoginViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = AuthenticationSerializer
    queryset = []

    def create(self, request):
        username = request.data["username"]
        password = request.data["password"]

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
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})
