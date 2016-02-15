from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import BreedSerializer
from .models import Breed

class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.get_all()
    permission_classes = (IsAuthenticated,)
