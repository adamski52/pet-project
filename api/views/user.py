from rest_framework import viewsets
from django.contrib.auth.models import User

from api.serializers.user import *
from api.permissions.onetimecreate import *


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (OneTimeCreate,)

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return User.objects.all()
        return []
