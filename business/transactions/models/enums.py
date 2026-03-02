# business/transactions/models/enums.py

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


class TransactionSubType(models.TextChoices):
    DIRECT = "direct", "Direct"
    ORDER = "order", "Order Based"
    MANUFACTURE = "manufacture", "Manufacturing"
    CONSIGNMENT = "consignment", "Consignment"
    SERVICE = "service", "Service"


class TransactionDirection(models.TextChoices):
    IN = "in"
    OUT = "out"
    INTERNAL = "internal"