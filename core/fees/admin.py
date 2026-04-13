# core/fees/admin.py

from django.contrib import admin
from .models import FeeConfig


@admin.register(FeeConfig)
class FeeConfigAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "tenant",
        "fee_type",
        "value",
        "applies_to",
        "category",
        "partner",
        "is_active",
    )

    list_filter = (
        "tenant",
        "fee_type",
        "applies_to",
        "is_active",
    )

    search_fields = ("name",)

    autocomplete_fields = ("tenant", "category", "partner")