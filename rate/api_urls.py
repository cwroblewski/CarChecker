from rest_framework.routers import DefaultRouter
from rate.api_views import RateViewSet

router = DefaultRouter()
router.register(r'', RateViewSet)

urlpatterns = [
]

urlpatterns += router.urls
