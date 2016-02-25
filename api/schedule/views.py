from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins
from datetime import datetime

from .serializers import ScheduleSerializer
from api.appointment.models import Appointment

class ScheduleViewSet(mixins.ListModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            results = Appointment.admin_objects.all()
        else:
            results = Appointment.objects.all()


        if "end" in self.kwargs and "start" in self.kwargs:
            start_date = datetime.strptime(self.kwargs["start"], "%Y-%m-%d")
            end_date = datetime.strptime(self.kwargs["end"], "%Y-%m-%d")
            
            return results.filter(
                start_date__gte = start_date,
                start_date__lte = end_date)

        return results
        