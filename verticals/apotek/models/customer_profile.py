# verticals/apotek/models/customer_profile.py

from django.db import models
from business.customers.models import Customer

class ApotekCustomerProfile(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name="apotek_profile"
    )

    medical_note = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    requires_prescription = models.BooleanField(default=False)


    class Meta:
        db_table = "verticals_apotek_customer_profile"
        verbose_name = "Apotek Customer Profile"
        verbose_name_plural = "Apotek Customer Profiles"

    def __str__(self):
        return f"{self.customer.full_name} Apotek Profile"