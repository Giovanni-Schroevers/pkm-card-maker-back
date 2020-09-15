from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import card_maker_app.views
from card_maker import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('card_maker_app.urls')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^media/(?P<path>.*)', card_maker_app.views.media_access, name='media'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
