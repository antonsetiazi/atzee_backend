from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.tenants.models import UserTenant
from core.dashboard.invalidate import invalidate_dashboard_for_tenant


@receiver([post_save, post_delete], sender=UserTenant)
def invalidate_dashboard_on_user_tenant_change(sender, instance, **kwargs):
    invalidate_dashboard_for_tenant(instance.tenant_id)
