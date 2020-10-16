from rest_framework import permissions


class ReportIsAdmin(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if view.action != 'categories':
            return super(ReportIsAdmin, self).has_permission(request, view)
        else:
            return True
