from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    search_fields = ("username",)
    list_display = UserAdmin.list_display + ("avatar",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("avatar",)}),)
    )
