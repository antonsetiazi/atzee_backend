from django.db import models


class TransactionType(models.TextChoices):
    SALES = "sales", "Sales"
    PURCHASE = "purchase", "Purchase"
    ADJUSTMENT = "adjustment", "Stock Adjustment"
    TRANSFER = "transfer", "Stock Transfer"


class TransactionStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    CONFIRMED = "confirmed", "Confirmed"
    CANCELLED = "cancelled", "Cancelled"
    COMPLETED =  "completed", "Completed"
