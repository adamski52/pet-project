from django.db.models import Q
from itertools import chain
from datetime import datetime, timedelta

from .serializers import CameraSerializer
from .models import Camera
from api.permissions import CameraPermissions
from api.generic.views import BaseViewSet
from api.appointment.models import Appointment

class CameraViewSet(BaseViewSet):
    permission_classes = (CameraPermissions,)
    serializers = {
        "default": CameraSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Camera.admin_objects.all()
  

        if not self.request.user.is_authenticated():
            return Camera.objects.filter(
                is_public = True)

        # get confirmed, active appts for this user
        appointments = Appointment.objects.filter(
            scheduled_for = self.request.user,
            start_date__lte = datetime.now(),
            end_date__gte = datetime.now(),
            is_confirmed = True)

        rooms = []
        for appointment in appointments.all():
            rooms.append(appointment.room)

        return Camera.objects.filter(
            Q(is_public = True) | 
            Q(is_public = False, room__in = rooms))


