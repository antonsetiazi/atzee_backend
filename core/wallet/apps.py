from django.apps import AppConfig


class WalletConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.wallet"
    label = "core_wallet"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from core.wallet.entities.user_wallet_history import UserWalletHistoryEntity
        from core.wallet.entities.wallet_transaction_list import WalletTransactionListEntity

        register_entity(UserWalletHistoryEntity())
        register_entity(WalletTransactionListEntity())
