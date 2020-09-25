from rest_framework import permissions


class IsAuthenticatedListCreate(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return super(IsAuthenticatedListCreate, self).has_permission(request, view)

        return True


class IsAdminOrOwnerOrPublic(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return super(IsAdminOrOwnerOrPublic, self).has_permission(request, view) \
                or request.user.pk == obj.user.pk or obj.public
