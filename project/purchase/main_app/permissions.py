from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'It is wrong neighborhood for u (admin)'

    def has_permission(self, request, view):
        return request.user.is_admin


class IsStaff(BasePermission):
    message = 'It is wrong neighborhood for u (Staff)'

    def has_permission(self, request, view):
        return request.user.is_staff


class IsOwner(BasePermission):
    message = 'It is wrong neighborhood for u (mycart)'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
