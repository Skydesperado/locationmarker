from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.user.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ["-created_at"]
    list_display = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_active", "is_superuser"]
    search_fields = ["username", "email"]
    filter_horizontal = ["groups", "user_permissions"]
    readonly_fields = ["created_at", "updated_at", "last_login"]

    fieldsets = (
        ("Authentication", {
            "fields": ("email", "password"),
        }),
        ("Personal Info", {
            "fields": ("username", "first_name", "last_name"),
        }),
        ("Permissions", {
            "fields": ("is_active", "is_admin", "is_superuser", "groups", "user_permissions"),
        }),
        ("Important dates", {
            "fields": ("last_login", "created_at", "updated_at"),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2"),
        }),
    )
