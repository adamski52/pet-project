from rest_framework import viewsets
from rest_framework import serializers
from itertools import chain

from api.permissions import IsSenderOrReceiver
from .serializers import InviteSerializer, SenderSerializer, RecipientSerializer
from .models import Invite


class InviteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSenderOrReceiver,)

    def perform_create(self, serializer):        
        serializer.save(
            sender = self.request.user)

    def get_serializer_class(self):
        
        if self.request.method == "PUT":
            return RecipientSerializer

        if self.request.method == "DELETE":
            return SenderSerializer

        return InviteSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Invite.objects.all()

        if self.action == "list":
            sent = Invite.get_sent(self)
            received = Invite.get_received(self)

            return list(chain(sent, received))

        return Invite.get_all(self)

