from rest_framework import permissions


class IsAdminDelete(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action == 'destroy':
            return super(IsAdminDelete, self).has_permission(request, view)
        else:
            return True


class IsAdminOrUpdateSelf(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action in ['update', 'partial_update']:
            return super(IsAdminOrUpdateSelf, self).has_permission(request, view) \
                    or request.user.pk == int(request.path[-2:-1])
        else:
            return True
