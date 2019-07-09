from django.urls import include, path

from . import urls

urlpatterns = [
    path('api/', include(urls.api_views)),
    path('app/', include(urls.app_views))
]
