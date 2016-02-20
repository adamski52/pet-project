from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import AppointmentSerializer, AppointmentPropertySerializer
from .models import Appointment, AppointmentProperty


class AppointmentPropertyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentPropertySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return AppointmentProperty.admin_objects.all()

        return AppointmentProperty.objects.all()



class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.admin_objects.all()

        return Appointment.objects.all()