# business/booking/apps.py

from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "business.booking"
    label = "business_booking"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.booking_list import BookingListEntity

        register_entity(BookingListEntity())