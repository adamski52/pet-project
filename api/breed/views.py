from rest_framework.permissions import IsAuthenticated

from .serializers import BreedSerializer
from .models import Breed
from api.generic.views import BaseViewSet

class BreedViewSet(BaseViewSet):
    permission_classes = (IsAuthenticated,)
    serializers = {
        "default": BreedSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Breed.admin_objects.all()

        return Breed.objects.all()