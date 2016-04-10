from django.contrib.auth.models import User

from .serializers import UserSerializer, UserAttachmentSerializer
from api.permissions import OneTimeCreate, AttachmentPermissions
from api.generic.views import BaseViewSet, BaseAttachmentViewSet
from .models import UserAttachment


class UserAttachmentViewSet(BaseAttachmentViewSet):
    serializers = {
        "default": UserAttachmentSerializer
    }

    permission_classes = (AttachmentPermissions,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return UserAttachment.admin_objects.filter(
                user = self.kwargs["user_id"])

        return UserAttachment.objects.filter(
            user = self.kwargs["user_id"])

    


class UserViewSet(BaseViewSet):
    serializers = {
        "default": UserSerializer
    }
    
    permission_classes = (OneTimeCreate,)

    def get_queryset(self):        
        return User.objects.filter(
            id = self.request.user.id)
