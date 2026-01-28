from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.audit_logs.models import AuditLog
from core.audit_logs.mixins import AuditableModel

def get_instance_identifier(instance):
    return str(getattr(instance, "id", ""))


@receiver(post_save)
def audit_model_save(sender, instance, created, **kwargs):
    """
    Audit create & update for all models that have tenant.
    """
    if not issubclass(sender, AuditableModel):
        return

    # Skip core audit model itself
    if sender.__name__ == "AuditLog":
        return
    

    tenant = getattr(instance, "tenant", None)
    if not tenant:
        return
    
    action = "create" if created else "update"

    from core.audit_logs.context import get_current_user
    user = get_current_user()

    AuditLog.objects.create(
        tenant=tenant,
        user=user,
        action=action,
        resource=sender.__name__,
        resource_id=get_instance_identifier(instance),
    )
    

@receiver(post_delete)
def audit_model_delete(sender, instance, **kwargs):
    if sender.__name__ == "AuditLog":
        return
    
    tenant = getattr(instance, "tenant", None)
    if not tenant:
        return
    
    from core.audit_logs.context import get_current_user
    user = get_current_user()
    
    AuditLog.objects.create(
        tenant=tenant,
        user=user,
        action="delete",
        resource=sender.__name__,
        resource_id=get_instance_identifier(instance),
    )
