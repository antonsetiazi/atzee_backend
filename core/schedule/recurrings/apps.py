# core/schedule/recurring/apps.py

from django.apps import AppConfig


class RecurringsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.schedule.recurrings"
    label = "core_schedule_recurrings"

    def ready(self):
        from core.entities.registry import register_entity
        from .entities.recurring_list import RecurringListEntity
        from .entities.recurring_select_list import RecurringSelectListEntity

        register_entity(RecurringListEntity())
        register_entity(RecurringSelectListEntity())
