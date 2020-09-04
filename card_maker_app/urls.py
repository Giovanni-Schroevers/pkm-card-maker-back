from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CardViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cards', CardViewSet, basename='card')

urlpatterns = []

urlpatterns += router.urls
