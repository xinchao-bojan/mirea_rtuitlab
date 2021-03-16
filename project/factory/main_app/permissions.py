from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (admin)'

    def has_permission(self, request, view):
        return request.user.is_admin
