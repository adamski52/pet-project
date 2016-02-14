from rest_framework import viewsets, mixins
from rest_framework.response import Response
from django.contrib.auth import logout

from api.serializers.session import *

class LogoutViewSet(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = SessionSerializer
    queryset = []

    def create(self, request):
        logout(request)
        return Response({"detail": "Successfully logged out."})
