from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext as _


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("username",)
    list_filter = ("is_superuser", "groups")
    search_fields = ("username",)
    ordering = ("-date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
