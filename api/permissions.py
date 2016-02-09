from rest_framework import permissions

class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return not request.user.is_authenticated()

    def has_object_permissions(self, request, view, obj):
        return not request.user.is_authenticated()

class IsAdminOrSelfOrSafe(permissions.BasePermission):
    def has_permission(self, request, view):

        if view.action == "list":
            return request.user.is_staff

        return request.method in permissions.SAFE_METHODS or request.user.is_staff
 
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user