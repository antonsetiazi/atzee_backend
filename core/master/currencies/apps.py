# core/master/currencies/apps.py

from django.apps import AppConfig


class CurrenciesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.master.currencies"
    label = "core_master_currencies"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.currency_list import CurrencyListEntity
        from .entities.currency_select_list import CurrencySelectListEntity

        register_entity(CurrencyListEntity())
        register_entity(CurrencySelectListEntity())
