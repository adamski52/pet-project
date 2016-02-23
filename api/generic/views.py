from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import FormatSerializer, PropertySerializer
from .models import Format, Property
from api.permissions import PublicReadAdminWrite

class FormatViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializer_class = FormatSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Format.admin_objects.all()

        return Format.objects.all()



class PropertyViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializer_class = PropertySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Property.admin_objects.all()

        return Property.objects.all()

