from rest_framework import permissions
from .base import IsAuthenticated


class IsAuthenticatedListCreate(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'like']:
            return super(IsAuthenticatedListCreate, self).has_permission(request, view)

        return True


class IsAdminOrOwnerOrPublic(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action not in ['like', 'comment']:
            return super(IsAdminOrOwnerOrPublic, self).has_permission(request, view) \
                or request.user.pk == obj.user.pk or obj.public

        if obj.public and request.user.is_authenticated:
            return True

        return False
