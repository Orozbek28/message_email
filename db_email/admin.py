from django.contrib import admin
from db_email.models import Email


class AdminEmail(admin.ModelAdmin):
    list_display = ('name', 'message', 'email')
    ordering = ['name']


admin.site.register(Email, AdminEmail)


