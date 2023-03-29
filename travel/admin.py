from django.contrib import admin
from .models import Travels

# Register your models here.

class TravelsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'create_ad', 'update_ad')

admin.site.register(Travels, TravelsAdmin)