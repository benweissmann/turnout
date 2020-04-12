from rest_framework import serializers

from .models import Region, Office, Address

class RegionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("name", "external_id")


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "address", "address2", "address3", "city", "state", "zipcode", 
            "website", "email", "phone", "fax", "is_physical", "is_regular_mail")


class OfficeSerializer(serializers.ModelSerializer):
    addresses =  AddressSerializer(source="address_set", many=True)

    class Meta:
        model = Office
        fields = ("hours", "notes", "addresses")


class RegionDetailSerializer(serializers.ModelSerializer):
    offices =  OfficeSerializer(source="office_set", many=True)

    class Meta:
        model = Region
        fields = ("external_id", "name", "county", "municipality", "offices")
