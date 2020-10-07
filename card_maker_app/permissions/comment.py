from rest_framework import permissions


class IsAuthenticatedComment(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'like']:
            return super(IsAuthenticatedComment, self).has_permission(request, view)
