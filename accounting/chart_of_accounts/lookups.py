# accounting/chart_of_accounts/lookups.py

from accounting.chart_of_accounts.models import AccountType
from core.lookups.registry import register_lookup


def account_type_lookup():
    return [
        {"label": label, "value": value}
        for value, label in AccountType.choices
    ]


register_lookup("account_types", account_type_lookup)
