from django.contrib import admin
from django.urls import (
    path,
    include
)

from cars import api_urls as cars_urls
from cars.api_views import CarSortedBydPopularityListApiView
from rate import api_urls as rate_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include(cars_urls)),
    path('rate/', include(rate_urls)),
    path('popular/', CarSortedBydPopularityListApiView.as_view(), name='popular_list')
]
