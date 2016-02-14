from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers.dog import *
from api.models.dog import *

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Dog.get_all()

        return Dog.objects.filter(
            owner = self.request.user)
