# business/products/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from business.products.models import Product
from core.dashboard.invalidate import invalidate_dashboard_for_tenant


@receiver([post_save, post_delete], sender=Product)
def invalidate_dashboard_on_product_change(sender, instance, **kwargs):
    invalidate_dashboard_for_tenant(instance.tenant_id)
