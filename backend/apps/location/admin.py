from django.contrib import admin
from apps.location.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "address", "latitude", "longitude", "created_at", "updated_at")
    list_filter = ("user",)
    search_fields = ("address", "latitude", "longitude")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (None, {
            "fields": (
                "user", "address", "latitude", "longitude", "created_at", "updated_at"
            )
        }),
    )
