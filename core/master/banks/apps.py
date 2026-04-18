# core/master/banks/apps.py

from django.apps import AppConfig


class BanksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.master.banks"
    label = "core_master_banks"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.bank_list import BankListEntity
        from .entities.bank_create import BankCreateEntity
        from .entities.bank_detail import BankDetailEntity
        from .entities.bank_update import BankUpdateEntity

        register_entity(BankListEntity())
        register_entity(BankCreateEntity())
        register_entity(BankDetailEntity())
        register_entity(BankUpdateEntity())