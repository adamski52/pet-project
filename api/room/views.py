from .serializers import RoomSerializer
from .models import Room
from api.permissions import PublicReadAdminWrite
from api.generic.views import BaseViewSet

class RoomViewSet(BaseViewSet):
    permission_classes = (PublicReadAdminWrite,)
    serializers = {
        "default": RoomSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Room.admin_objects.all()

        return Room.objects.all()
