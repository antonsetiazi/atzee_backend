# core/ui/admin.py
from django.contrib import admin
from .models import UIMenu

@admin.register(UIMenu)
class UIMenuAdmin(admin.ModelAdmin):
    list_display = ("key", "label", "app", "resource", "action", "parent", "order")
    list_filter = ("app", "is_active")
    search_fields = ("key", "label")
