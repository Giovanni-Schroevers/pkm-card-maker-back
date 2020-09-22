from rest_framework import permissions


class IsAdminDelete(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action == 'destroy':
            return super(IsAdminDelete, self).has_permission(request, view)
        else:
            return True


class IsAdminOrUpdateSelf(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update', 'update_email']:
            return super(IsAdminOrUpdateSelf, self).has_permission(request, view) \
                    or request.user.pk == obj.pk
        else:
            return True


class IsAdminOrOwner(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return super(IsAdminOrOwner, self).has_permission(request, view) \
                or request.user.pk == obj.pk


class IsAdminOrGetRequest(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return super(IsAdminOrGetRequest, self).has_permission(request, view)
