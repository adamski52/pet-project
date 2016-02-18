from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BreedSerializer
from .models import Breed

class BreedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BreedSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Breed.admin_objects.all()

        return Breed.objects.all()