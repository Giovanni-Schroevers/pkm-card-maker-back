from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CardViewSet, CardCommentViewSet, ReportViewSet, CategoryViewSet, AppealViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'cards', CardViewSet, basename='card')
router.register(r'comments', CardCommentViewSet, basename='comment')
router.register(r'reports', ReportViewSet, basename='report')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'appeals', AppealViewSet, basename='appeal')

urlpatterns = []

urlpatterns += router.urls
