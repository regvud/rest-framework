from rest_framework.permissions import BasePermission


class IsAdminOrWriteOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_staff)


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)
