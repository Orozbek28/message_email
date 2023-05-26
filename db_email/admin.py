from django.contrib import admin
from django.utils.safestring import mark_safe

from db_email.models import Email, Product



class AdminEmail(admin.ModelAdmin):
    list_display = ('name', 'message', 'email')
    ordering = ['name']


admin.site.register(Email, AdminEmail)





class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    ordering = ['name']


admin.site.register(Product, AdminProduct)
