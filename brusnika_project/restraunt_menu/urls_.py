from django.urls import include, path

from .urls import (api_urls, app_urls)





urlpatterns = [
    path('api/', include(api_urls)),
    path('app/', include(app_urls)),
]
