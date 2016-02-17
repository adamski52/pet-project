from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import DogSerializer
from .models import Dog

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Dog.objects.all()

        return Dog.objects.active().filter(
            owner = self.request.user)
