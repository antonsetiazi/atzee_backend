# accounting/enum/depreciation_method.py

from django.db import models


class DepreciationMethod(models.TextChoices):
    STRAIGHT_LINE = "straight_line", "Straight Line"
    DECLINING_BALANCE = "declining_balance", "Declining Balance"
    MANUAL = "manual", "Manual"
