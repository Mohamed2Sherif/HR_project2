from django.contrib import admin
from django.contrib.auth.admin import UserAdmin , User
from .models import Account
from .models import Employee
class AccountAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_admin')
    search_fields = ('username', 'email')
    readonly_fields = ('password',)

    # useless but must be here

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class emp(admin.ModelAdmin):
    list_display = ('Name', 'accId')
    search_fields = ('Name', 'accId')


    # useless but must be here

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('Name',)


admin.site.register(Account,AccountAdmin)
admin.site.register(Employee,emp)