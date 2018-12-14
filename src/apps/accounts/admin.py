from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group as AuthGroup

from .models import User, Group

class UserAdmin(admin.ModelAdmin):
    """..."""
    search_fields = (
        'city', 'email', 'first_name', 'last_name', 'middle_name', 'phone',
        'position'
    )
    list_display = (
        'image_tag', 'email', 'last_name', 'first_name', 'middle_name', 'position', 'city', 'phone',
        'date_joined',
    )
    ordering = ('-date_joined', )


admin.site.unregister(AuthGroup)
admin.site.register(User, UserAdmin)
admin.site.register(Group, admin.ModelAdmin)

