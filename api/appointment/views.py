from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from .serializers import AppointmentSerializer
from .models import Appointment


class AppointmentViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.admin_objects.all()

        return Appointment.objects.all()