from django.db.models import Q
from itertools import chain
from datetime import datetime, timedelta

from .serializers import CameraSerializer
from .models import Camera#, CameraStream
from api.permissions import CameraPermissions
from api.generic.views import BaseViewSet
from api.appointment.models import Appointment
from flask import Flask, Response

class CameraViewSet(BaseViewSet):
    permission_classes = (CameraPermissions,)
    serializers = {
        "default": CameraSerializer
    }



    """
    @detail_route(
        methods = ["GET"],
        permission_classes = [CameraPermissions],
        serializers = {
            "default": CameraSerializer
        })
    def watch(self, request, pk = None):
        app = Flask("wat")
        app.run(host='0.0.0.0', debug=True)


        def gen(camera):
            while True:
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


        return Response(gen(Camera()),
            mimetype='multipart/x-mixed-replace; boundary=frame')
    """


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


