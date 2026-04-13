from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "tenant", "phone", "email", "rating_avg")
    search_fields = ("name", "phone", "email")
    list_filter = ("tenant",)