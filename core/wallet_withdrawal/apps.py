from django.apps import AppConfig


class WalletWithdrawalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.wallet_withdrawal"
    label = "core_wallet_withdrawal"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.withdrawal_list import WithdrawalListEntity

        register_entity(WithdrawalListEntity())