# verticals/finance/dashboard/builders/quick_actions.py

from verticals.finance.dashboard.constants import quick_actions


def build_quick_actions():
    return [
        quick_actions.create_invoice,
        quick_actions.receive_payment,
        quick_actions.customers,
        quick_actions.add_asset,
        quick_actions.reports,
    ]
