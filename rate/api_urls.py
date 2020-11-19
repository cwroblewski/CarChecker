from rest_framework.routers import DefaultRouter
from rate.api_views import RateViewSet

router = DefaultRouter()
router.register(r'', RateViewSet, basename='Car')

urlpatterns = [
]

urlpatterns += router.urls
