from rest_framework import viewsets
from itertools import chain


from api.permissions import DogPermissions
from api.user.models import UserProfile
from .serializers import DogSerializer
from .models import Dog

class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    permission_classes = (DogPermissions,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Dog.admin_objects.all()

        profile = UserProfile.objects.get(
            user = self.request.user)

        dogs = Dog.objects.filter(
            id__in = profile.dogs.values_list("id", flat = True))



        return dogs