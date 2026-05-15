# verticals/finance/dashboard/builders/hero.py

from django.utils import timezone


def build_hero(user):

    current_hour = timezone.localtime().hour

    if current_hour < 12:
        greeting_time = "Good Morning"

    elif current_hour < 15:
        greeting_time = "Good Afternoon"

    elif current_hour < 21:
        greeting_time = "Good Evening"

    else:
        greeting_time = "Good Night"

    return {
        "badge": "ENTERPRISE FINANCE OVERVIEW",
        "greeting": f"{greeting_time}, {user.full_name} 👋",
        "title": "Enterprise Workspace",
        "subtitle": (
            "Monitor finance, operations, customers, "
            "and business performance in one unified dashboard."
        ),
        "description": (
            "Monitor cash flow, fixed assets, receivables, "
            "profitability, and accounting activities "
            "across your organization."
        ),
    }
