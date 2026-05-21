# hrms/enums/payroll_status.py

from django.db import models


class PayrollStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PROCESSED = "processed", "Processed"
    PAID = "paid", "Paid"
    CANCELLED = "cancelled", "Cancelled"
