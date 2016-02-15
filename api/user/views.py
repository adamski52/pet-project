from rest_framework import viewsets
from django.contrib.auth.models import User

from .serializers import UserSerializer
from api.permissions import OneTimeCreate

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (OneTimeCreate,)

    def get_queryset(self):        
        if self.request.user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(
                id = self.request.user.id)
