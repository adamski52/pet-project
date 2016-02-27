from .serializers import RoomSerializer
from .models import Room
from api.permissions import RoomPermissions
from api.generic.views import BaseViewSet

class RoomViewSet(BaseViewSet):
    permission_classes = (RoomPermissions,)
    serializers = {
        "default": RoomSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Room.admin_objects.all()

        if not self.request.user.is_authenticated():
            return Room.objects.filter(
                is_public = True)
            
        return Room.objects.all()
