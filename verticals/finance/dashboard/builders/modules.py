# verticals/finance/dashboard/builders/modules.py

from verticals.finance.dashboard.constants import modules


def build_modules():
    return [
        modules.balance_sheet,
        modules.trial_balance,
        modules.profit_loss,
        modules.cash_flow,
        modules.journal,
        modules.accounts,
        modules.ar_dashboard,
        modules.ar_invoices,
        modules.ar_payments,
        modules.ap_dashboard,
        modules.ap_invoices,
        modules.ap_payments,
        modules.fa,
        modules.fa_dashboard,
        modules.fa_depreciation,
        modules.fa_disposals,
        modules.fa_categories,
    ]
