from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Event


@admin.register(Event)
class UserAdminModel(admin.ModelAdmin):
    list_display = ['title', 'description', 'start_date', 'end_date', 'location', 'image', 'is_active']
    