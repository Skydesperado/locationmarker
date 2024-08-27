from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Custom Permission To Only Allow Owners of a Location To Access or Edit It
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
