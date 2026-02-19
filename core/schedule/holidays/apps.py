# core/schedule/holiday/apps.py

from django.apps import AppConfig


class HolidaysConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.holidays"
    label = "core_schedule_holidays"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.holiday_list import HolidayListEntity
        from .entities.holiday_select_list import HolidaySelectListEntity

        register_entity(HolidayListEntity())
        register_entity(HolidaySelectListEntity())
