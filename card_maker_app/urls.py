from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CardViewSet, CardCommentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cards', CardViewSet, basename='card')
router.register(r'comments', CardCommentViewSet, basename='comment')

urlpatterns = []

urlpatterns += router.urls
