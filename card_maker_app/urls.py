from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, get_card_options

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('card_options/', get_card_options)
]

urlpatterns += router.urls

