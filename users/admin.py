from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        ('Role Info', {'fields': ('role',)}),
    )
admin.site.register(User, UserAdmin)