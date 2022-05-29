from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdministrator(UserAdmin):
    list_display = ("username", "email", "fullname", "last_login","date_joined", "is_staff")
    search_fields = ("username", "email")
    readonly_fields = ("id", "date_joined", "last_login")
    filter_horizontal = ()
    filter_vertical = ()
    list_filter = ()

admin.site.register(Account, AccountAdministrator)