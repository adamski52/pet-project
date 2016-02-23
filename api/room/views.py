from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin


from .serializers import RoomSerializer
from .models import Room
from api.permissions import PublicReadAdminWrite


class RoomViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializer_class = RoomSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Room.admin_objects.all()

        return Room.objects.all()
