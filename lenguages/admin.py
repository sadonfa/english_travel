from django.contrib import admin
from .models import Lenguages

# Register your models here.
class LengAdmin(admin.ModelAdmin):
    readonly_fields = ('create_ad', 'update_ad')


admin.site.register(Lenguages, LengAdmin)