# core/notifications/events.py

"""
Central Event Registry for Atzee Platform.

All business-level notification events must be registered here.
Do NOT use raw strings outside this module.
"""


# =========================================================
# Booking Events
# =========================================================

BOOKING_CREATED = "booking.created"
BOOKING_ACCEPTED = "booking.accepted"
BOOKING_REJECTED = "booking.rejected"
BOOKING_CANCELLED = "booking.cancelled"


# =========================================================
# Order Events
# =========================================================

ORDER_CREATED = "order.created"
ORDER_NEEDS_APPROVAL = "order.needs_approval"
ORDER_ACCEPTED = "order.accepted"
ORDER_REJECTED = "order.rejected"
ORDER_CANCELLED = "order.cancelled"
ORDER_COMPLETED = "order.completed"


# =========================================================
# Payment Events
# =========================================================

PAYMENT_PENDING = "payment.pending"
PAYMENT_SUCCESS = "payment.success"
PAYMENT_FAILED = "payment.failed"
PAYMENT_REFUNDED = "payment.refunded"


# =========================================================
# Session / Service Events
# =========================================================

SESSION_REMINDER = "session.reminder"
SESSION_STARTED = "session.started"
SESSION_COMPLETED = "session.completed"
SESSION_CANCELLED = "session.cancelled"


# =========================================================
# System Events
# =========================================================

SYSTEM_ANNOUNCEMENT = "system.announcement"
SYSTEM_MAINTENANCE = "system.maintenance"


# =========================================================
# Registry (for validation / admin / filtering)
# =========================================================

ALL_NOTIFICATION_EVENTS = [
    # Booking
    BOOKING_CREATED,
    BOOKING_ACCEPTED,
    BOOKING_REJECTED,
    BOOKING_CANCELLED,

    # Order
    ORDER_CREATED,
    ORDER_NEEDS_APPROVAL,
    ORDER_ACCEPTED,
    ORDER_REJECTED,
    ORDER_CANCELLED,
    ORDER_COMPLETED,

    # Payment
    PAYMENT_PENDING,
    PAYMENT_SUCCESS,
    PAYMENT_FAILED,
    PAYMENT_REFUNDED,

    # Session
    SESSION_REMINDER,
    SESSION_STARTED,
    SESSION_COMPLETED,
    SESSION_CANCELLED,

    # System
    SYSTEM_ANNOUNCEMENT,
    SYSTEM_MAINTENANCE,
]


# =========================================================
# Event Metadata
# =========================================================

EVENT_META = {
    BOOKING_CREATED: {"level": "info", "category": "booking"},
    BOOKING_ACCEPTED: {"level": "info", "category": "booking"},
    BOOKING_REJECTED: {"level": "warning", "category": "booking"},
    BOOKING_CANCELLED: {"level": "warning", "category": "booking"},

    ORDER_CREATED: {"level": "success", "category": "order"},
    ORDER_NEEDS_APPROVAL: {"level": "info", "category": "order"},
    ORDER_ACCEPTED: {"level": "success", "category": "order"},
    ORDER_REJECTED: {"level": "warning", "category": "order"},
    ORDER_CANCELLED: {"level": "warning", "category": "order"},
    ORDER_COMPLETED: {"level": "success", "category": "order"},

    PAYMENT_PENDING: {"level": "info", "category": "payment"},
    PAYMENT_SUCCESS: {"level": "info", "category": "payment"},
    PAYMENT_FAILED: {"level": "error", "category": "payment"},
    PAYMENT_REFUNDED: {"level": "warning", "category": "payment"},

    SESSION_REMINDER: {"level": "info", "category": "session"},
    SESSION_STARTED: {"level": "info", "category": "session"},
    SESSION_COMPLETED: {"level": "info", "category": "session"},
    SESSION_CANCELLED: {"level": "warning", "category": "session"},

    SYSTEM_ANNOUNCEMENT: {"level": "info", "category": "system"},
    SYSTEM_MAINTENANCE: {"level": "warning", "category": "system"},
}