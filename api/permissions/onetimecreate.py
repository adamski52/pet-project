from rest_framework import permissions

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