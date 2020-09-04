from rest_framework import permissions


class IsAuthenticatedListCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return super(IsAuthenticatedListCreate, self).has_permission(request, view)

        return True
