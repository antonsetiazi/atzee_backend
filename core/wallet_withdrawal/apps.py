from django.apps import AppConfig


class WalletWithdrawalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.wallet_withdrawal"
    label = "core_wallet_withdrawal"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.withdrawal_list import WithdrawalListEntity
        from .entities.withdrawal_detail import WithdrawalDetailEntity
        from .entities.withdrawal_approval import WithdrawalApprovalEntity

        register_entity(WithdrawalListEntity())
        register_entity(WithdrawalDetailEntity())
        register_entity(WithdrawalApprovalEntity())