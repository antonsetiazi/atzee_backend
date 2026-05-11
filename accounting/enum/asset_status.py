# accounting/enum/asset_status.py

from django.db import models


class AssetStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    ACTIVE = "active", "Active"
    FULLY_DEPRECIATED = "fully_depreciated", "Fully Depreciated"
    DISPOSED = "disposed", "Disposed"
