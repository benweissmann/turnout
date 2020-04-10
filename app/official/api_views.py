from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Region, Office, Address
from .serializers import RegionOfficeAddressSerializer


class RegionViewSet(ReadOnlyModelViewSet):
    model = Region
    serializer_class = RegionOfficeAddressSerializer

    def get_queryset(self, pk):
        "gets regions for a particular state"
        state = self.kwargs['pk']
        return Region.objects.filter(state__code=state)
