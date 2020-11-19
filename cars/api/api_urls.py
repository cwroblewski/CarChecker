from rest_framework.routers import DefaultRouter
from .api_views import CarViewSet

router = DefaultRouter()
router.register(r'', CarViewSet, basename='Car')

urlpatterns = [
]

urlpatterns += router.urls
