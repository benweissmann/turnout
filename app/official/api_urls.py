from rest_framework import routers

from .api_views import RegionViewSet

router = routers.SimpleRouter()
router.register(r"region", RegionViewSet)

app_name = "api_official"
urlpatterns = router.urls
