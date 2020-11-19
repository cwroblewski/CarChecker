from django.urls import (
    path,
    include
)

from .api import api_urls as cars_api_urls


urlpatterns = [
    path('api/', include(cars_api_urls))
]