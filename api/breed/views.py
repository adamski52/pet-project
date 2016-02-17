from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BreedSerializer
from .models import Breed

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.active()
    permission_classes = (IsAuthenticated,)
    serializer_class = BreedSerializer
