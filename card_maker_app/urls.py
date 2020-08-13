from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, index

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


urlpatterns = []

urlpatterns += router.urls
