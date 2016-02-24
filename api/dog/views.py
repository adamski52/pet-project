from api.permissions import DogPermissions
from api.user.models import UserProfile
from api.generic.views import BaseViewSet
from .serializers import DogSerializer
from .models import Dog

class DogViewSet(BaseViewSet):
    permission_classes = (DogPermissions,)
    serializers = {
        "default": DogSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Dog.admin_objects.all()

        profile = UserProfile.objects.get(
            user = self.request.user)

        dogs = Dog.objects.filter(
            id__in = profile.dogs.values_list("id", flat = True))

        return dogs
