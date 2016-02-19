from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import RoomSerializer
from .models import Room

class RoomViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Room.admin_objects.all()

        return Room.objects.all()