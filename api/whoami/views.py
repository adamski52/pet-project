from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework import permissions

from api.user.serializers import UserSerializer

class WhoAmIViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):        
        return User.objects.filter(
            id = self.request.user.id)
