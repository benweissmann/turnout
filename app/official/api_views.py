from rest_framework import mixins, viewsets

from .models import Region, Office, Address
from .serializers import RegionNameSerializer, RegionDetailSerializer


class StateRegionsViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    model = Region
    serializer_class = RegionNameSerializer

    def get_queryset(self):
        state_code = self.kwargs['state']
        return Region.objects.filter(state__code=state_code)


class RegionDetailViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    model = Region
    serializer_class = RegionDetailSerializer
    queryset = Region.objects.all()
    lookup_field = "external_id"
