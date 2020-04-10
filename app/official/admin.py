from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from official import models


class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class AddressInlineAdmin(ReadOnlyModelAdmin, NestedStackedInline):
    model = models.Address
    parent_model = models.Region
    fields = (
        "address", "address2", "address3", "city", "state", "zipcode",
        "website", "email", "phone", "fax",
        "is_physical", "is_regular_mail"
    )
    extra = 0

    def __init__(self, parent_model, admin_site):
        admin.TabularInline.__init__(self, parent_model, admin_site)


class OfficeInlineAdmin(ReadOnlyModelAdmin, NestedStackedInline):
    model = models.Office
    fields = ("hours", "notes")
    inlines = [AddressInlineAdmin]
    extra = 0

    def __init__(self, parent_model, admin_site):
        admin.TabularInline.__init__(self, parent_model, admin_site)


@admin.register(models.Region)
class RegionAdmin(ReadOnlyModelAdmin, NestedModelAdmin):
    list_display = ("name", "municipality", "county", "state",)
    list_filter = ("state",)
    inlines = [OfficeInlineAdmin]