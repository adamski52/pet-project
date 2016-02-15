from rest_framework import viewsets
from rest_framework import serializers
from itertools import chain

from api.permissions import IsAuthenticatedAndOwner
from .serializers import InviteSerializer
from .models import Invite

class InviteViewSet(viewsets.ModelViewSet):
    serializer_class = InviteSerializer
    permission_classes = (IsAuthenticatedAndOwner,)

    def perform_create(self, serializer):        
        serializer.save(
            sender = self.request.user)


    def get_queryset(self):
        if self.request.user.is_staff:
            return Invite.objects.all()

        if self.action == "list":
            sent = Invite.get_sent(self)
            received = Invite.get_received(self)

            return list(chain(sent, received))

        return Invite.get_all(self)

