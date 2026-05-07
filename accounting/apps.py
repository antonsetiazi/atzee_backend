# accounting/apps.py

from django.apps import AppConfig


class AccountingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounting"
    label = "accounting"

    def ready(self):
        from .ui import bootstrap

        from core.entities.registry import register_entity

        from .entities.account_list import AccountListEntity
        register_entity(AccountListEntity())

        from .entities.account_create import AccountCreateEntity
        register_entity(AccountCreateEntity())
        
        from .entities.account_detail import AccountDetailEntity
        register_entity(AccountDetailEntity())
        
        from .entities.account_update import AccountUpdateEntity
        register_entity(AccountUpdateEntity())
        
        from .entities.account_select_list import AccountSelectListEntity
        register_entity(AccountSelectListEntity())
        
        from .entities.journal_create import JournalCreateEntity
        register_entity(JournalCreateEntity())
        
        from .entities.journal_list import JournalListEntity
        register_entity(JournalListEntity())
        
        from .entities.journal_detail import JournalDetailEntity
        register_entity(JournalDetailEntity())
        
        from .entities.ledger_account import LedgerAccountEntity
        register_entity(LedgerAccountEntity())
        
        from .entities.trial_balance import TrialBalanceEntity
        register_entity(TrialBalanceEntity())
        
        from .entities.profit_loss import ProfitLossEntity
        register_entity(ProfitLossEntity())
        
        from .entities.balance_sheet import BalanceSheetEntity
        register_entity(BalanceSheetEntity())
        
        from .entities.cash_flow import CashFlowEntity
        register_entity(CashFlowEntity())

