from rest_framework import serializers

from .models import Region, Office, Address

class RegionOfficeAddressSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Region
        fields = ("name", "municipality", "county", "state")