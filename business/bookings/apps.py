# business/bookings/apps.py

from django.apps import AppConfig


class BookingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.bookings"
    label = "business_bookings"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from business.bookings.entities.admin_bookings_list import AdminBookingsListEntity
        from business.bookings.entities.user_bookings_upcoming import UserBookingsUpcomingEntity
        from business.bookings.entities.user_bookings_recent import UserBookingsRecentEntity
        from business.bookings.entities.user_bookings_history import UserBookingsHistoryEntity
        from business.bookings.entities.partner_bookings_upcoming import PartnerBookingsUpcomingEntity

        register_entity(AdminBookingsListEntity())
        register_entity(UserBookingsUpcomingEntity())
        register_entity(UserBookingsRecentEntity())
        register_entity(UserBookingsHistoryEntity())
        register_entity(PartnerBookingsUpcomingEntity())