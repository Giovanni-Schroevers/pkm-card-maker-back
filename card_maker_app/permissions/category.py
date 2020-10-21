from .base import IsAuthenticated


class IsAuthenticatedCategory(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'detail']:
            return super(IsAuthenticatedCategory, self).has_permission(request, view)

        else:
            return False
