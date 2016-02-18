from rest_framework import permissions

from api.user.models import UserProfile

class DogPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if view.action == "destroy":
            return obj.owner == request.user

        profile = UserProfile.objects.get(
            user = request.user)

        if view.action == "update" or "retrieve":
            return obj.owner == request.user or obj.id in profile.dogs.values_list("id", flat = True)

        return False


class IsSenderOrReceiver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        if view.action == "destroy":
            return obj.sender_id == request.user.id

        if view.action == "update":
            return obj.recipient_email == request.user.email


        if view.action == "retrieve":
            return obj.sender_id == request.user.id or obj.recipient_email == request.user.email

        return False


class IsAuthenticatedAndOwner(permissions.BasePermission):
    def has_permission(self, request, view):        
        if view.action == "destroy":
            return request.user.is_staff

        return request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        
        return obj.sender_id == request.user.id or obj.recipient_email == request.user.email



class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated()

    def has_object_permissions(self, request, view, obj):
        return not request.user.is_authenticated()


class OneTimeCreate(permissions.BasePermission):
    def has_permission(self, request, view):        
        if view.action == "destroy":
            return request.user.is_staff

        if view.action == "create":
            if request.user.is_authenticated():
                return request.user.is_staff

            return True


        if view.action == "update" or view.action == "partial_update":
            return request.user.is_authenticated()

        return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        return obj.id == request.user.id




class OneToOneCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "destroy":
            return request.user.is_staff

        if view.action == "create" or view.action == "list":
            if request.user.is_authenticated():
                if request.user.is_staff:
                    return True
                return request.user.family is None
            return False

        if view.action == "update" or view.action == "partial_update":
            return request.user.is_authenticated()

        return True
 
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user
