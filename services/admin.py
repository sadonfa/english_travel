from django.contrib import admin
from .models import Service

# Register your models here.

class AdminServices(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'create_ad', 'update_ad')

admin.site.register(Service, AdminServices)
