from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from api.permissions import DogPermissions, AttachmentPermissions
from api.user.models import UserProfile
from api.generic.views import BaseViewSet
from .serializers import DogSerializer, DogAttachmentSerializer
from .models import Dog, DogAttachment

class DogAttachmentViewSet(BaseViewSet):
    serializers = {
        "default": DogAttachmentSerializer
    }

    permission_classes = (AttachmentPermissions,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return DogAttachment.admin_objects.filter(
                dog = self.kwargs["dog_id"])

        return DogAttachment.objects.filter(
            dog = self.kwargs["dog_id"])

    



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
