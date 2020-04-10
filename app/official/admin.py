from django.contrib import admin

from official import models


class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(models.Office)
class OfficeInlineAdmin(ReadOnlyModelAdmin):
    model = models.Office
    fields = ("hours", "website", "email", "phone", "fax")


@admin.register(models.Address)
class AddressInlineAdmin(ReadOnlyModelAdmin):
    model = models.Address
    fields = ("address", "address2", "address3", "city", "state", "zipcode")


@admin.register(models.Region)
class RegionAdmin(ReadOnlyModelAdmin):
    list_display = ("name", "municipality", "county", "state",)
    list_filter = ("state",)
