from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .serializers import AppointmentSerializer, AppointmentGetSerializer, AppointmentConfirmSerializer, AppointmentPutSerializer
from .models import Appointment
from api.permissions import IsAuthenticatedAndScheduler
from api.generic.views import BaseViewSet

class AppointmentViewSet(BaseViewSet):
    permission_classes = (IsAuthenticatedAndScheduler,)
    serializers = {
        "default": AppointmentSerializer,
        "GET": AppointmentGetSerializer,
        "PUT": AppointmentPutSerializer,
    }


    @detail_route(
        methods = ["GET", "PUT"],
        permission_classes = [IsAdminUser],
        serializers = {
            "default": AppointmentConfirmSerializer
        })
    def confirm(self, request, pk = None):
        appointment = Appointment.objects.get(
            id = pk)

        if request.method == "PUT":
            appointment.is_confirmed = request.data.get("is_confirmed", False)
            appointment.save()


        serializer = AppointmentConfirmSerializer(
            appointment,
            context = {"request": request})
        
        return Response(serializer.data, status = 200)



    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.admin_objects.all()

        return Appointment.objects.filter(
            scheduled_by = self.request.user)
