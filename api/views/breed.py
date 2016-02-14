from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers.breed import *
from api.models.breed import *

class BreedViewSet(viewsets.ModelViewSet):
    serializer_class = BreedSerializer
    queryset = Breed.get_all()
    permission_classes = (IsAuthenticated,)
