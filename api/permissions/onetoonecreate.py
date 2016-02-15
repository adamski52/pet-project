from rest_framework import permissions

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
