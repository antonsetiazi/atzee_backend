from django.apps import AppConfig


class AuditLogsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.audit_logs"
    label = "core_audit_logs"

    
    def ready(self):
        import core.audit_logs.signals
