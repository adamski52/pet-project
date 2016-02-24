from itertools import chain

from api.permissions import IsSenderOrReceiver
from .serializers import InviteSerializer, SenderSerializer, RecipientSerializer
from .models import Invite
from api.dog.models import Dog
from api.generic.views import BaseViewSet


class InviteViewSet(BaseViewSet):
    permission_classes = (IsSenderOrReceiver,)
    serializers = {
        "PUT": RecipientSerializer,
        "DELETE": SenderSerializer,
        "default": InviteSerializer
    }
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Invite.admin_objects.all()

        if self.action == "list":
            sent = Invite.objects.sent(self.request.user)
            received = Invite.objects.received(self.request.user)

            return list(chain(sent, received))

        return Invite.objects.all()

