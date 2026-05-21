# verticals/hr/dashboard/builders/hero.py

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
        "badge": "ENTERPRISE HUMAN RESOURCES",
        "greeting": f"{greeting_time}, {user.full_name} 👋",
        "title": "People & Workforce Workspace",
        "subtitle": (
            "Manage employees, attendance, payroll, "
            "recruitment, and workforce operations "
            "from one unified HR platform."
        ),
        "description": (
            "Monitor employee growth, attendance trends, "
            "organizational structure, leave management, "
            "and HR activities across your company."
        ),
    }
