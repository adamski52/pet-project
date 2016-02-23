from rest_framework import viewsets
from rest_framework import serializers
from itertools import chain
from django.db import transaction
from rest_framework_extensions.mixins import NestedViewSetMixin


from api.permissions import IsSenderOrReceiver
from .serializers import InviteSerializer, SenderSerializer, RecipientSerializer
from .models import Invite
from api.dog.models import Dog


class InviteViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (IsSenderOrReceiver,)
    
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return RecipientSerializer

        if self.request.method == "DELETE":
            return SenderSerializer

        return InviteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Invite.admin_objects.all()

        if self.action == "list":
            sent = Invite.objects.sent(self.request.user)
            received = Invite.objects.received(self.request.user)

            return list(chain(sent, received))

        return Invite.objects.all()

