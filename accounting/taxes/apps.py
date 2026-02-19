from django.apps import AppConfig


class TaxesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.taxes"
    label = "accounting_taxes"

    def ready(self):
        from .ui import bootstrap