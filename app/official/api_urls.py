from rest_framework import routers
from django.urls import path

from .api_views import StateRegionsViewSet, RegionDetailViewSet

router = routers.SimpleRouter()
router.register(r"region", RegionDetailViewSet, basename="region")

app_name = "api_official"
urlpatterns = router.urls + [
    path("<slug:state>/", StateRegionsViewSet.as_view({'get': 'list'}), name="state_regions"),
]
