from rest_framework import viewsets

from .serializers import FormatSerializer, PropertySerializer, PropertyGetSerializer
from .models import Format, Property
from api.permissions import PublicReadAdminWrite

class BaseViewSet(viewsets.ModelViewSet):
    serializers = { 
        "default": None,
    }

    def get_serializer_class(self):
        return self.serializers.get(
            self.request.method,
            self.serializers["default"])


class FormatViewSet(BaseViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializers = {
        "default": FormatSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Format.admin_objects.all()

        return Format.objects.all()


class PropertyViewSet(BaseViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializers = {
        "default": PropertySerializer,
        "GET": PropertyGetSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Property.admin_objects.all()

        return Property.objects.all()
