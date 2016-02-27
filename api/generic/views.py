from rest_framework import viewsets, mixins
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FormatSerializer, PropertySerializer, PropertyGetSerializer, ImageSerializer
from .models import Format, Property
from api.permissions import PublicReadAdminWrite

class BaseAttachmentViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    serializers = { 
        "default": None,
    }

    def get_serializer_class(self):
        return self.serializers.get(
            self.request.method,
            self.serializers["default"])


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



class ImageViewSet(BaseViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializers = {
        "default": ImageSerializer
    }



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
