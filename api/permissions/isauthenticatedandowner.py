from rest_framework import permissions

class IsAuthenticatedAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):        
        if view.action == "destroy":
            return request.user.is_staff

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        return obj.sender_id == request.user.id or obj.recipient_email == request.user.email