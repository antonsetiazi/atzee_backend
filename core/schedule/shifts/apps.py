# core/schedule/shifts/apps.py

from django.apps import AppConfig


class ShiftsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.shifts"
    label = "core_schedule_shifts"

    def ready(self):
        from .ui import bootstrap
        from core.entities.registry import register_entity
        from .entities.shift_list import ShiftListEntity
        from .entities.shift_select_list import ShiftSelectListEntity

        register_entity(ShiftListEntity())
        register_entity(ShiftSelectListEntity())
