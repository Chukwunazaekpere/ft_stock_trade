from email.headerregistry import Group
from django.contrib import admin

from django.contrib.auth.admin import (
    UserAdmin
)

from django.contrib.auth.models import Group

from .models import Users

from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm
)


class UsersAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['users_fullname', "email", "phone", "username", "address", "last_login", "date_registered"]
    list_filter = ["is_active"]


    fieldsets = [
        ("Bio-Data", {
            "fields": ["firstname", "lastname", "email", "phone",]
        })
    ]

    add_fieldsets = [
        ("Bio Details", {
            "fields": ["firstname", "lastname",  "username", "address"]
        }),
        ("Contact Details", {
            "fields": ["email", "phone",]
        })
    ]



    ordering = ["email"]

    





admin.site.register(Users, UsersAdmin)



admin.site.site_header = "FT Stocks"
admin.site.unregister(Group)
admin.site.site_title = "FT Stocks"
admin.site.index_title = "FT Stocks"