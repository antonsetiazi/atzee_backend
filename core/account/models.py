# core/account/models.py

from django.db import models
from django.conf import settings
from core.geo.countries.models import Country
from core.geo.regions.models import Region
from core.geo.cities.models import City


class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="settings",
    )

    # UI Preferences
    theme = models.CharField(
        max_length=20,
        default="light",
    )

    language = models.CharField(
        max_length=10,
        default="en",
    )

    timezone = models.CharField(
        max_length=50,
        default="UTC",
    )

    # Notifications
    email_notifications = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_user_settings"

    def __str__(self):
        return f"Settings for {self.user.username}"


class UserAddress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="addresses",
    )

    tenant = models.ForeignKey(
        "core_tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="user_addresses",
    )

    label = models.CharField(max_length=100)  # Rumah, Kantor

    recipient_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)

    address_line = models.TextField()

    # New Geo Relation
    country_ref = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        related_name="user_addresses",
        null=True,
        blank=True,
    )

    region_ref = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="user_addresses",
        null=True,
        blank=True,
    )

    city_ref = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="user_addresses",
        null=True,
        blank=True,
    )

    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100)

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_user_addresses"
        ordering = ["-is_default", "-created_at"]
        indexes = [
            models.Index(fields=["user", "tenant"]),
            models.Index(fields=["user", "is_default"]),
        ]

    def __str__(self):
        return f"{self.label} - {self.user.username}"
    

class UserBankAccount(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bank_accounts",
    )

    tenant = models.ForeignKey(
        "core_tenants.Tenant",
        on_delete=models.CASCADE,
        related_name="user_bank_accounts",
    )

    bank = models.ForeignKey(
        "core_master_banks.Bank",
        on_delete=models.PROTECT,
        related_name="user_accounts",
        null=True,
        blank=True,
    )
    
    account_number = models.CharField(max_length=50)
    account_name = models.CharField(max_length=150)

    is_default = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "core_user_bank_accounts"
        ordering = ["-is_default", "-created_at"]
        indexes = [
            models.Index(fields=["user", "tenant"]),
            models.Index(fields=["user", "is_default"]),
        ]

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"    