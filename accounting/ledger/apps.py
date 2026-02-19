# accounting/ledger/apps.py

from django.apps import AppConfig


class LedgerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting.ledger"
    label = "accounting_ledger"


    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from accounting.ledger.entities.ledger_list import LedgerListEntity

        register_entity(LedgerListEntity())