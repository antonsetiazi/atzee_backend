# verticals/ustadzku/seeds/notifications.py

from core.notifications.events import (
    SYSTEM_ANNOUNCEMENT,
    SESSION_REMINDER,
    PAYMENT_SUCCESS,
)

NOTIFICATIONS = [

    # 🔹 System Announcement
    {
        "event": SYSTEM_ANNOUNCEMENT,
        "title": "Welcome to Ustadzku Platform 🎉",
        "message": "We are excited to have you onboard.",
    },

    # 🔹 Session Reminder
    {
        "event": SESSION_REMINDER,
        "title": "Upcoming Session Reminder",
        "message": "You have a session scheduled tomorrow at 09:00 AM.",
        "entity_type": "session",
        "entity_id": "SES-001",
        "payload": {
            "redirect_to": "/dashboard/sessions/SES-001"
        }
    },

    # 🔹 Payment Success
    {
        "event": PAYMENT_SUCCESS,
        "title": "Payment Successful 💳",
        "message": "Your recent booking payment has been successfully processed.",
        "entity_type": "payment",
        "entity_id": "PAY-001",
        "payload": {
            "redirect_to": "/dashboard/payments/PAY-001"
        }
    },
]