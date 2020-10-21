from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CardViewSet, CardCommentViewSet, ReportViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cards', CardViewSet, basename='card')
router.register(r'comments', CardCommentViewSet, basename='comment')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = []

urlpatterns += router.urls
