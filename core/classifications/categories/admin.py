# core/classifications/categories/admin.py

from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "scope", "tenant", "is_active")
    search_fields = ("name", "code")
    list_filter = ("tenant", "scope", "is_active")