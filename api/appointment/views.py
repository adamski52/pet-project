from .serializers import AppointmentSerializer, AppointmentGetSerializer
from .models import Appointment
from api.permissions import IsAuthenticatedAndScheduler
from api.generic.views import BaseViewSet

class AppointmentViewSet(BaseViewSet):
    permission_classes = (IsAuthenticatedAndScheduler,)
    serializers = {
        "default": AppointmentSerializer,
        "GET": AppointmentGetSerializer
    }

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.admin_objects.all()

        return Appointment.objects.filter(
            scheduled_by = self.request.user)
