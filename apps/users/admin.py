from django.contrib import admin
from .models import HemoscUser
from django.contrib.auth.admin import UserAdmin

class ListUserAdmin(UserAdmin):
    fieldsets=[(
        None,
        {
            "fields": ["location", "username", "password"],
        },
    )]

admin.site.register(HemoscUser, ListUserAdmin),