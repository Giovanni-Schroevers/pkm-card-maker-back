from rest_framework import permissions


class IsAuthenticated(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.banned:
            return False

        return super(IsAuthenticated, self).has_permission(request, view)
